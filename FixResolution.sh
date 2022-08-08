#!/bin/bash

read -p "  Width: " WIDTH
read -p " Height: " HEIGHT
read -p "Refresh: " REFRESH


GTF=$(gtf $WIDTH $HEIGHT $REFRESH | grep Modeline | sed -e 's/^.*Modeline\ //g')
MODE=$(echo $GTF | awk -F'[[:space:]]' '{print $1}')


xrandr --newmode $GTF
xrandr --addmode Virtual1 $MODE
