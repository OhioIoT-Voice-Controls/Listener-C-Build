# Listener C<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

##### [(back to the Voice Controls organization page)](https://github.com/OhioIoT-Voice-Controls)

This is a container implementation for your custom Vosk listener to run on a Raspberry Pi.  

You can see this repo in use in the OhioIoT YouTube video [3 Steps To Your Custom Voice Control](https://youtu.be/_ERvoHMBDac).

## Installation
Run the following commands.  It works on Git Bash on Windows:
```
git clone https://github.com/OhioIoT-Voice-Controls/Vosk-Listener-MQTT.git vosk-mqtt
cd vosk-mqtt
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
Edit the IP address on line 16 of `listener.py` to match the IP address of the MQTT broker that you are running.

Then run:
```
./+run
```
If the script says `listening...`, it means you have successfully attached to the MQTT broker and are using the default microphone.  If you say "lights on" or "lights off", you will see that an MQTT messages is sent to the broker with topic `voice/command' and then payload `set_lights_on` or `set_lights_off`.

When you are comfortable that everything is in order, start running the container in the background:
```
docker compose up -d
```
## Links
- [OhioIoT YouTube Channel](https://www.youtube.com/@ohioiot) - Agenda free tutorials showing you how to get started in IoT
- [OhioIoT GitHub Index](https://github.com/OhioIoT-Examples) - The central index of code examples available on GitHub

## About
<a href="https://www.ohioiot.com"><img src="https://www.ohioiot.com/logo_150.jpg" width="40" ></a>

*OhioIoT is an IoT platform designed for small-scale IoT projects.  For more, check out our website at [www.OhioIoT.com](https://www.ohioiot.com).*
