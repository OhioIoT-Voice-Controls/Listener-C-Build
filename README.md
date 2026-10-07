# Listener C Build<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

##### [(back to the Voice Controls organization page)](https://github.com/OhioIoT-Voice-Controls)

This is a container implementation for your custom Vosk listener to run on a Raspberry Pi.  

You can see this repo in use in the OhioIoT YouTube video [3 Steps To Your Custom Voice Control](https://youtu.be/_ERvoHMBDac).

## Installation
Pull the repo to your laptop:
```
git clone https://github.com/OhioIoT-Voice-Controls/Listener-C-Build listener
cd listener
```
Edit the `commands.py'.  It's a list of key/value pairs.  The key is what you "say", and the value is the command that goes out as the mqtt payload.  If you want to change the topic that the messages go out to, change it directly in listener.py.  

When you are done with the edits, edit `./_build` so that it points to your Docker Hub account, and then run it:
```
./_build
```
If your running the code on your Raspberry Pi with Watchtower running (see [Listener C](https://github.com/OhioIoT-Voice-Controls/Listener-C)), your updated container image should pull down and run automatically.

## Links
- [OhioIoT YouTube Channel](https://www.youtube.com/@ohioiot) - Agenda free tutorials showing you how to get started in IoT
- [OhioIoT GitHub Index](https://github.com/OhioIoT-Examples) - The central index of code examples available on GitHub

## About
<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

*OhioIoT is an IoT platform designed for small-scale IoT projects.  For more, check out our website at [www.OhioIoT.com](https://www.ohioiot.com).*
