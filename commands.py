

# edit these and then re-build your container image

# format:
#      "the command that you say": "the payload that goes out"

COMMANDS = {
    "lights on": "set_lights_on",
    "lights off": "set_lights_off",
    "turn the temperature up": "adjust_temp_up",
    "turn the temperature down": "adjust_temp_down",
}
