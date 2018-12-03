# Arcade 1Up scripts

A couple of Python scripts to use the Power &amp; Volume buttons of the Arcade 1Up with a Raspberry Pi 3B+
Note: Older generation Raspberry Pi boards with the same GPIO layout should also work.

## Firstly, wire up you Raspberry Pi 3B+ with the following pin layout:

I used 150mm Plug to Socket Jumper Leads to reach from the existing connectors to the Rasberry Pi munted on the side of the Arcade 1Up.

### Power switch
Connect the black wire to Pin 5 (GPIO3) & the red wire to Pin 6 (Ground) of the GPIO header

### Volume switch
Connect the brown wire to Pin 7 (GPIO4), red wire to Pin 9 (Ground) & the black wire to Pin 11 (GPIO17) of the GPIO header.

Note: I use the audio out from the Pi directly to my amp (mini phone to 2x RCA)

## Install
I created a directory called scripts under my home folder.
Copy your files there then edit your rc.local file like so...

sudo nano /etc/rc.local

In nano scroll down to after fi but before exit 0 & add the lines
(sudo python /home/pi/scripts/shutdown.py) &
(sudo python /home/pi/scripts/volume.py) &

Save the file (CTRL x, y, enter)

## Reboot & profit!
