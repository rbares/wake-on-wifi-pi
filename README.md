# wake-on-wifi-pi
Upgrade any Wake-on-LAN (WoL) device to wake via WiFi (WoWLAN), with the help of your Raspberry Pi.

## Installation instructions

The following instructions assume you are sitting at a prompt on a Raspberry Pi and have the contents of this repository copied to the current directory. This has been tested on a Raspberry Pi 3 running Raspbian stretch.

### Prepare the Raspberry Pi
- Connect the Ethernet port of the Raspberry Pi to the machine you want to wake
- [Configure the WiFi interface on the Pi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)

### Install the service
```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install -r requirements.txt
sudo cp run.py /usr/local/bin/wol-forward.py
sudo cp wol-forward.service /lib/systemd/system/
```

### Configure the service to start on boot
```
sudo systemctl daemon-reload
sudo systemctl enable wol-forward
sudo systemctl start wol-forward
```