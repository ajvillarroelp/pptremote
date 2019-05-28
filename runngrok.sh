#!/bin/bash
./pptremote.py > output.txt &
rm pylinuxbot.log
ngrok http 5050 --log ./pylinuxbot.log --log-level debug
