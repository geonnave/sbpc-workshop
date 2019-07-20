#!/bin/bash

sudo apt install -y curl

mkdir -p ~/tmp
cd ~/tmp
curl -k 'https://downloads.arduino.cc/arduino-1.8.9-linuxarm.tar.xz' > arduino.tar.xz
tar -xvf arduino.tar.xz
cd arduino-1.8.9/
./install.sh
cd -

sudo usermod -a -G dialout $(whoami)
echo Now log out and log in again to be able to use the Arduino via serial

read -p "Pronto."

exit 0
