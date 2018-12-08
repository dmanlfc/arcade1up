# Arcade 1Up scripts

Here I provide a couple of Python scripts to use the Power &amp; Volume buttons of the Arcade 1Up with a Raspberry Pi 3B+ assuming you have done similar mods to ETA Prime like so... https://www.youtube.com/watch?v=09DQCOr6zQM

These scripts run in the background monitoring the toggle switches & then take appropriate action accordingly.

#### Note: Older generation Raspberry Pi boards with the same GPIO layout should also work.

## Firstly, wire up you Raspberry Pi 3B+ with the following pin layout:

I used 150mm Plug to Socket Jumper Leads to reach from the existing connectors to the Rasberry Pi munted on the side of the Arcade 1Up.

### Power switch
Connect the black wire to Pin 5 (GPIO3) & the red wire to Pin 6 (Ground) of the GPIO header

### Volume switch
Connect the brown wire to Pin 7 (GPIO4), red wire to Pin 9 (Ground) & the black wire to Pin 11 (GPIO17) of the GPIO header.

#### Note: I use the audio out from the Pi directly to my amp (mini phono to 2x RCA)

## Install

I created a directory called arcade1up under my home folder.
These instructions will do the same.
Hit F4 to exit out of RetroPie / Emulation Station to the terminal.

Type:

git clone https://github.com/dmanlfc/arcade1up.git

#### Note: If you don't have git, you can download by typing sudo apt install git

Once complete you will have a directory under your home directory (/home/pi) called arcade1up.
Next we edit your rc.local file like so...type:

sudo nano /etc/rc.local

In nano scroll down to after fi line but before exit 0 & add the lines as so...

(sudo python /home/pi/arcade1up/shutdown.py) &

(sudo python /home/pi/arcade1up/volume.py) &

Save the file (CTRL x, then y, then enter)

We also need to install the GPIO & Python packages for this to work.
Type:

sudo apt install python-rpi.gpio python3-rpi.gpio

Reboot & profit! (sudo reboot)

### Special notes

The power switch will only power down the Raspberry Pi & not the monitor or speakers. You still need to physically power off at the wall. I haven't done anything with something like an IoT relay yet.

If you power off at the wall please ensure before you start the Pi to toggle the switch back to on & then start the Pi by turning on at the wall otherwise within 10 seconds the Pi will power off again (the script see's the switch in the off position).

If you find the volume is too high (or low) for the toggle switch settings edit the % values of the script to you liking.
i.e. press F4

nano /home/pi/arcade1up/volume.py

edit the line such as: call(["amixer", "set", "PCM", "96%"])

If you have a boot splash screen & decent speaker through an amp you may want to adjust omxplayers volume.
By default omxplayer will play at 0db (96% on the Pi)
For example I have a systemd service which starts a script called asplashscreen.sh
Therefore to fix so we play at 75% volume we have to adjust the millibel volume to -2259 on the Pi

i.e. sudo nano /opt/retropie/supplementary/splashscreen/asplashscreen.sh

edit the line #### omxplayer -o both -b --layer 10000 "$line"
to read like so #### omxplayer -o both -b --vol -2259 --layer 10000 "$line"
