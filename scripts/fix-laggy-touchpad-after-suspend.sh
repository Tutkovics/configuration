#!/bin/sh

case $1 in
  post)
    /sbin/rmmod i2c_hid && /sbin/modprobe i2c_hid 
  ;;
esac

# locate: /lib/systemd/system-sleep/
