# Docker Restart

#!/bin/bash

# Get the list of services defined in docker-compose.yml
dockerjson=$(docker compose ls --format json)

dirs=$(jq '.[] | .ConfigFiles' <<< $dockerjson)
services=$(jq '.[] | .Name' <<< $dockerjson)
hostname=$(cat /etc/hostname)
i=0

for dir in $dirs; do
  i=$((i+1))

  service=$(echo $services | cut -d" " -f$(echo $i))
  service=$(echo $service| tr -d '"')

  dir=$(echo $dir | tr -d '"')
  dir=$(dirname $dir)

  cd $dir

  echo "service: $service, dir: $dir, $(pwd)" # Live debug

  downlog="/tmp/dockerlog-downlog.log"
  uplog="/tmp/dockerlog-uplog.log"


  docker compose down > $downlog 2>&1 
  docker compose up -d > $uplog 2>&1 

  runlog=$(cat $downlog && cat $uplog)

  rm $downlog
  rm $uplog
  
  echo $runlog

  #GOTIFYCURL-restartlog
done