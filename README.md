# Listener C Build<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

##### [(back to the Voice Controls organization page)](https://github.com/OhioIoT-Voice-Controls)

This is a container implementation for your custom Vosk listener to run on a Raspberry Pi.  It's possible to store your commands in a file on the Raspberry Pi, and edit those commands from time to time (see [Listener B](https://github.com/OhioIoT-Voice-Controls/Listener-B)).  But that's not always convenient, and it depends on a container image that I (Larry) built.  To take control of the container image and make command editing more convenient, you pull down this repo, where you can edit the Python code at your will, in addition to the commands themselves.

This repo was showcased in the OhioIoT YouTube video [3 Steps To Your Custom Voice Control](https://youtu.be/_ERvoHMBDac).

## Installation
Pull the repo to your laptop:
```
git clone https://github.com/OhioIoT-Voice-Controls/Listener-C-Build listener_c_build
cd listener_c_build
```
Edit `_build` so that it points to your desired Docker Hub account and container name (defaulted to listener_c):

Edit the `commands.py`.  It's a list of key/value pairs.  The key is what you "say", and the value is the command that goes out as the mqtt payload.  If you want to change the topic that the messages go out to, change it directly in listener.py.  

When you are done with the edits, re-build and re-push your Docker container image:
```
./_build
```
Once your container image has been pushed to Docker Hub, navigate to the [Listener-C](https://github.com/OhioIoT-Voice-Controls/Listener-C) repo to install your listener on your Raspberry Pi.


## Links
- [OhioIoT YouTube Channel](https://www.youtube.com/@ohioiot) - Agenda free tutorials showing you how to get started in IoT
- [OhioIoT GitHub Index](https://github.com/OhioIoT-Examples) - The central index of code examples available on GitHub

## About
<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

*OhioIoT is an IoT platform designed for small-scale IoT projects.  For more, check out our website at [www.OhioIoT.com](https://www.ohioiot.com).*
