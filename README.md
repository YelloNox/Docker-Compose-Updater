# Docker-Compose-Updater

> Scripts I use with [Remotely](https://github.com/immense/Remotely) to automate Docker Compose containers in bulk across hosts.


Do you know of an easy method to update multiple Docker Compose containers, all on multiple hosts? If so, message me! I am using [Remotely](https://github.com/immense/Remotely) to automate the scripts over a control node. It's the best I got (-﹏- ;)


## 📦 Requirements

-   [Python](https://www.python.org/) If you intend to run `setup.py` (not needed, but handy)
-   [Docker Compose](https://docs.docker.com/compose/install/linux/)


## 🪴 Getting Started

> 📎 Note: You are
 still able to use the scripts in `script-templates` without running `setup.py`.

Clone `.env.example` and set the variables with services you want to connect.

Clone the repo, install the requirements, and build the scripts:

```bash
git clone https://github.com/YelloNox/asuratoon-dl
pip install -r requirements.txt
python setup.py
```

-> All final scripts are located in `./script_builds`


## 🔨 Script Functions

`Compose_Restart-All.sh` - Restarts all active Docker Compose containers.

`Compose_Update-All.sh` - Updates all active Docker Compose containers.

`docker-image-prune.sh`, `docker-system-prune.sh` - Does exactly what they sound like. Docker stuff.


## ✅ ToDo:

-   [ ] Add an option for the standalone `docker-compose` for those who dare.
-   [ ] ~~Stop overdoing basic functions, like sleeping... Or start them, idk...~~
-   [ ] Double check at a later (not tired time) to see if this README.md is up to my standards.
-   [ ] Support for a `.dockerupdateignoorefile.file` to disable updates for certain services... Or a list in the script itself... Or both for those special cases.


## 🤔 What does `setup.py` actually do?

The primary purpose of the script is to automatically embed functions into `./script-templates/*` and is easy(ish) to expand in the future. Also, you do not actually need to run it. The scripts in `./script-templates` just work!

### What does `setup.py` actually do currently?

The script actually does the following so far:

-   Enable notifications for [Gotify](https://github.com/gotify/server) notifications.
-   ...

Yeah, I... Umm... THERE WILL PROBABLY BE UPDATES IN THE FUTURE. IT DIDN'T TAKE THAT LONG (maybe) TO WRITE AND IS TOTALLY WORTH THE TIME (ง •̀_•́)ง


## ❓ Q&A

### Why did I write this?

My Docker setup consists of multiple `docker-compose.yml` scripts, all over multiple directories, and on multiple nodes. As you might assume, it gets quite annoying to keep everything up-to-date. Therefore, I setup these scripts to improve QOL by using [Remotely](https://github.com/immense/Remotely) to bulk update all active and running containers.

### No like, actually... Why did you write this?

yes.

### Why are the first lines of the scripts so goofy???

You must be questioning the first line of most scripts... plz stop (╥﹏╥)

[Remotely](https://github.com/immense/Remotely) just has an annoying problem where it doesn't show the name of the script ran in the log overview. This is to combat the problem. It's (probably) the only solution.


### Doesn't [watchtower](https://github.com/containrrr/watchtower) exists?

Yes, but I am looking for more manual control over my updates. Especially if there are bugs or compatibility issues in later versions.

### Will I actually implement all items on the ToDo list?

Most likely not. I am currently in school with limited time and will most likely spend it daddling new or more in-depth projects.

## 🌟 Thanks

-   [Remotely](https://github.com/immense/Remotely)
-   [Remotely](https://github.com/immense/Remotely#yes-this-is-a-second-link...no-questions!!!)
-   [Gotify](https://github.com/gotify/server)
-   [Docker Compose](https://docs.docker.com/compose/install/linux/)
-   [You](https://www.youtube.com/watch?v=MPfYg4ASx78)


---

<sub>Good Night 🌙</sub>
