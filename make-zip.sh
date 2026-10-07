#!/bin/bash

## a convenience script to package your code to send to AI
## you need to install tar for this to work

rm -f *.tar.gz   ## remove the previously created file, if there

tar -czf listener.tar.gz _build +run .dockerignore docker.compose.rpi.yml Dockerfile listener.py commands.py requirements.txt