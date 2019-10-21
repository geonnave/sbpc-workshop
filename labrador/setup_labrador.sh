#!/bin/bash

[ -z "$(grep 'alias python' ~/.bashrc)" ] && echo "alias python=python3" >> ~/.bashrc

echo will install basic tools...
sudo apt install openssh-server vim git python3-dev python3-pip python3-setuptools idle3

echo will install opencv...
sudo apt install libopencv-dev python3-opencv

echo will install pip3 requirements...
pip3 install -r requirements.txt
pip3 install idlex

read -p "Pronto."

exit 0

