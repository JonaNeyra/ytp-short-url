#!/bin/bash

curl --request POST \
  --url http://localhost:8081/shorting_url \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
	"url": "http://localhost:8081/ping_to_redis"
}'
