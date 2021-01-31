#!/bin/sh
# /userdata/system/custom
case "$1" in
  start)
    # first wait for wifi
    sleep 5
    # now set the time
    datetext=$(curl -I 'http://1.1.1.1/' 2>/dev/null | grep "Date:" |sed 's/Date: [A-Z][a-z][a-z], //g'| sed 's/\r//') ; echo "Date Retrieved = $datetext" ; echo -n "Date set = " ; date -s "$datetext" -D'%d %b %Y %T %Z'
    # now get the python extras we need
    echo "Getting pyserial"
    curl https://files.pythonhosted.org/packages/1e/7d/ae3f0a63f41e4d2f6cb66a5b57197850f919f59e558159a4dd3a818f5082/pyserial-3.5.tar.gz -o pyserial-3.5.tar.gz
    echo "Extracting pyserial"
    gunzip pyserial-3.5.tar.gz
    tar x -f pyserial-3.5.tar
    cd pyserial-3.5
    echo "Installing pyserial"
    python setup.py install
    # now run the volume python script
    echo "Running volume python script"
    python /userdata/system/volume.py & 
    ;;
  stop)
    echo "Stopping example"
    # kill application you want to stop
    kill $(ps aux | grep “python /userdata/system/volume.py” | awk ‘{print $2}’)
    ;;
  *)
    echo "Usage: /userdata/system/custom{start|stop}"
    exit 1
    ;;
esac
 
exit 0
