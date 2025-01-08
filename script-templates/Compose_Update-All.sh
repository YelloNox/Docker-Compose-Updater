# Docker Update

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

  pulllog="/tmp/dockerlog-pulllog.log"
  uplog="/tmp/dockerlog-uplog.log"


  docker compose pull > $pulllog 2>&1
  docker compose up -d > $uplog 2>&1

  runlog=$(cat $pulllog && cat $uplog)

  rm $pulllog
  rm $uplog

  echo $runlog

  #GOTIFYCURL-updatelog
done