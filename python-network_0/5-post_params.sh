#!/bin/bash
# Send a POST request with email and subject parameters and display the response
curl -sX POST -d "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
