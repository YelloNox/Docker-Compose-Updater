import os
import dotenv

# Copy file. An attempt to fix odd permissions issue. Too lazy to revert. Also, only copy if not existing.
def copyFile(oldFile, newFile):
    if os.path.isfile(newFile):
        print(f"\"{newFile}\" already exists, Skipping...")
        return
    
    with open(oldFile, 'r') as file:
        filedata = file.read()
    with open(newFile, 'w') as file:
        file.write(filedata)

# Create .env if not exists
if (not os.path.isfile('.env')):
    print("Creating .env")
    copyFile('.env.example', '.env')

dotenv.load_dotenv()

# .env vars
gotify_notifications = True
GOTIFY_URL = os.getenv('GOTIFY_URL')
GOTIFY_TOKEN = os.getenv('GOTIFY_TOKEN')

if (GOTIFY_TOKEN == "XXXXXXXXXXXXXXX" or GOTIFY_TOKEN == None):
    gotify_notifications = False

# Other vars
buildDir = './script_builds'
debug = True
gotify_url_template = 'curl "<gotifyURL>/message?token=<gotifyTOKEN>" -F "title=${hostname} - Docker <logtype> Log: ${service}" -F "message=${runlog}" -F "priority=5"'

# Debugging
def debug(msg):
    if debug:
        print(msg)

def updateCurl(url=GOTIFY_URL, token=GOTIFY_TOKEN):
    global gotify_url_template
    gotify_url_template =  gotify_url_template.replace("<gotifyURL>", url)
    gotify_url_template =  gotify_url_template.replace("<gotifyTOKEN>", token)
    debug(f"Replaced GOTIFY_URL with {url} and GOTIFY_TOKEN with {token}")


# Checks tokens for status, update if not existing and user = "y"
def userGotifyDetails():
    global gotify_notifications
    if gotify_notifications:
        updateCurl()
        return
    
    print('Gotify token not found in .env')
    user = input('Would you like to enable gotify notifications? (y/n): ')
    if (user == 'y'):
        GOTIFY_URL = input(f'\nExample: http://192.168.0.1:8007\nEnter your GOTIFY_URL: ')
        GOTIFY_TOKEN = input(f'\nEnter your GOTIFY_TOKEN: ')
        
        # Remove / at the end of URL if exists
        if GOTIFY_URL[-1] == '/':
            GOTIFY_URL = GOTIFY_URL[:-1]
        
        appendEnv('.env', f'GOTIFY_URL={GOTIFY_URL}', 'GOTIFY_URL=http://192.168.0.1:8007')
        appendEnv('.env', f'GOTIFY_TOKEN={GOTIFY_TOKEN}', 'GOTIFY_TOKEN=XXXXXXXXXXXXXXX')
        updateCurl(GOTIFY_URL, GOTIFY_TOKEN)
            
        print("Gotify notifications enabled")
        gotify_notifications = True
        return
    
    
    print(f"Gotify notifications disabled\n")
    return


# List all files in a specified directory
def listDir(dir):
    return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

# Replace text in .env. Would make it for any file, but odd issue with permissions when specifying file with string.
def appendEnv(file, newText, oldText):
    with open(r'.env', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(oldText, newText)
    debug(f"Appending from {oldText} to {newText} in .env")
    with open(r'.env', 'w') as file:
        file.write(filedata)

# Appends .env variables into scripts.
# Also appends alternative commands based on variables.
def buildScript(script):
    if not os.path.exists(buildDir):
        os.makedirs(buildDir)
    scriptPath = (f"{buildDir}/{script}")
    copyFile(f"./script-templates/{script}", scriptPath)
    
    appendToScript(scriptPath)

# Gets all appendations for a script based on script name
# This is the "Big Important Part" with all the spicy functions that change things to other things. Cool, right???
# Note: add things to change other things here ⬇️
def getAppendations(scriptData, script):
    scriptVars = []         # Script vairable to be replaced
    scriptReplacements = [] # The replacements to be applied to said var
    
    if "#GOTIFYCURL-updatelog" in scriptData and gotify_notifications:
        scriptVars.append("#GOTIFYCURL-updatelog")
        urltemp = gotify_url_template.replace("<logtype>", "Update")
        scriptReplacements.append(urltemp)
        print(f"Appending Gotify Curl to {script}")
    if "#GOTIFYCURL-restartlog" in scriptData and gotify_notifications:
        scriptVars.append("#GOTIFYCURL-restartlog")
        urltemp = gotify_url_template.replace("<logtype>", "Restart")
        scriptReplacements.append(urltemp)
        print(f"Appending Gotify Curl to {script}")

    return scriptVars, scriptReplacements

# Append variable to script
def appendToScript(script):
    with open(script, 'r') as file:
            filedata = file.read()
    scriptVars, scriptReplacements = getAppendations(filedata, script)
    
    for i in range(len(scriptReplacements)):
        filedata = filedata.replace(scriptVars[i], scriptReplacements[i])
        with open(script, 'w') as file:
            file.write(filedata)

if __name__ == '__main__':
    userGotifyDetails()
            
    files = listDir('./script-templates')
    for file in files:
        debug(f"\nBuilding {file}")
        buildScript(f"{file}")

    print(f"\nDone!")