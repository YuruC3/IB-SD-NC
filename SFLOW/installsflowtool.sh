#!/bin/bash


sudo apt install git autoreconf -y


git clone https://github.com/sflow/sflowtool.git

cd sflowtool
./boot.sh
./configure
make
sudo make install


