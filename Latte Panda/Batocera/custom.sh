#!/bin/sh

logfile=/userdata/system/logs/scriptlog.txt

log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> "$logfile"
}

case "$1" in
  start)
    log "Starting custom script"
    
    # Wait for WiFi connection
    log "Waiting for WiFi"
    sleep 5
    
    # Retrieve and set the date
    datetext=$(curl -Is 'http://1.1.1.1/' 2>/dev/null | awk '/^Date:/ {print $3" "$4" "$5" "$6" "$7}')
    if [ -n "$datetext" ]; then
        log "Date Retrieved = $datetext"
        date -s "$datetext" +"%Y-%m-%d %H:%M:%S" >/dev/null 2>&1
    else
        log "Failed to retrieve date"
    fi
    
    # Set the timezone
    log "Now set the timezone"
    TZ=Australia/Brisbane
    hwclock --systz --localtime
    
    # Run the volume Python script
    log "Running the volume Python script"
    python /userdata/system/volume.py >/dev/null 2>&1 &
    log "You should now be able to control the volume..."
    ;;

  stop)
    log "Stopping custom script"
    
    # Kill the Python script
    pids=$(pgrep -f "python /userdata/system/volume.py")
    if [ -n "$pids" ]; then
        log "Killing Python script"
        kill $pids
    else
        log "Python script not found"
    fi
    ;;

  *)
    echo "Usage: $0 {start|stop}"
    exit 1
    ;;
esac

exit 0
