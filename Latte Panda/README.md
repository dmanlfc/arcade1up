# A set of scripts, config files etc

These files assist with getting the Latte Panda working within the Arcade 1UP cabinet

## Details

### music.py
A python script to be called at Ubuntu startup to play music which EMulation Station is running
This will also mute when a game starts accordingly

### power&vol-LP-arduino
An Arduino program to detect changes to the connected switches & take actions
The power pins are used in conjunction with a Relay to send power signals to the SW pins on the Latte Panda

### volume-lattepanda.py
Another python script to be run a startup which will detect the output from Arduino ragrding the volume button changes
This script will adjust the PCM volume accordingly

Note: The other folders have their own README.md files
