#!/usr/bin/env bash
# this will launch the model3 emulator with specific settings
# requires the compiled supermodel binary
# the Config, NVRAM & Saves folders need to be in here too
# make the script executable chmod +x

ROM="$1"
# ensure supermodel runs from the correct directory - fails otherwise
cd /opt/retropie/emulators/model3

# we use -legacy3d as the intel graphics card doesn't work well with the new 3d engine
./supermodel -fullscreen -res=1280,1024 -legacy3d -multi-texture - quad-rendering "$ROM"
