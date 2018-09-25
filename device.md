# Raspberry Pi Setup

[Offical Instructions](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md)

## Identify USB Drive

```bash
# run with out usb sd card carrier
lsblk

# run with usb sd card carrier
lsblk

sdc      8:32   1   7.4G  0 disk 
└─sdc1   8:33   1   7.4G  0 part /media/randomsilo/RPI

```

## Install Image

```bash

# start copy
cd /shop/randomsilo/rpi/images
sudo dd bs=4M if=2018-03-13-raspbian-stretch.img of=/dev/sdc conv=fsync

# open new terminal
# check progress
sudo dd bs=4M if=2018-03-13-raspbian-stretch.img of=/dev/sdc status=progress conv=fsync

#confirm image

# copy file off of sd card
sudo dd bs=4M if=/dev/sdc of=from-sd-card.img 

# dd copies full disk, truncate both images so we can compare
sudo truncate --reference 2018-03-13-raspbian-stretch.img from-sd-card.img

# compare with diff
sudo diff -s 2018-03-13-raspbian-stretch.img from-sd-card.img

# should see
Files 2018-03-13-raspbian-stretch.img and from-sd-card.img are identical

# sync before unplugging drive
sync

# pull USB Carrier
# put SD Card into RPI
```

## Windows

[Create RPI SD Card from Windows](https://howtoraspberrypi.com/create-raspbian-sd-card-raspberry-pi-windows/)

Use Win32 Disk Imager to write the latest RPI OS to the Sd Card.

## Configure as Workstation

Plug in a monitor, USB hub, keyboard, mouse, and power cable.
Boot the RPI device and use the wireless icon in the upper right to connect the device to your local network.

## Setup Device Environment 

```
sudo apt update
sudo apt upgrade
sudo apt install python3
```


