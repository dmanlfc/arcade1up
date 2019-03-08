# A set of configuration files to run the Sega Model 3 emulator 'Supermodel' under RetroPie
Note: This is for x64 systems only

## Supermodel build instructions under Ubuntu linux

1. Install the required build packages

sudo apt-get install subversion build-essential libsdl1.2-dev libglew1.5-dev zlib1g-dev

2. Create the directory for the source code.

mkdir Supermodel

cd Supermodel

3. Download the latest build using svn like so 

svn checkout https://svn.code.sf.net/p/model3emu/code/trunk

4. Move to the trunk directory

cd trunk

5. Now choose the correct Makefile for linux & 'make' 

ln -s Makefiles/Makefile.UNIX Makefile

make

6. Now move to the binary directory to create directories & ini file 

cd bin

mkdir Config NVRAM Saves

cp ../Config/Supermodel.ini Config

7. Once complete copy the contents of the bin directory to /opt/retropie/emulators/model3/

mkdir /opt/retropie/emulators/model3

sudo cp . /opt/retropie/emulators/model3/

## Configuration files

Place the emulators.cfg file in the /opt/retropie/configs/model3/ directory
### Note: You'll have to create this dir

Place the model3.sh bash script into the /opt/retropie/emulators/model3 directory
### Note: You'll need to also create this directory

Take the contexts of the es_systems.cfg file and edit Emulation Stations es_systems.cfg located at /etc/emulationstation 
