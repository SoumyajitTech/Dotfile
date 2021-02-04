#!/bin/bash
if pgrep -x "picom" > /dev/null
then
	killall picom && notify-send "Picom is Stopped"
else
	picom -b --config ~/.config/picom/picom.conf && notify-send "Picom" "Enjoy Your transparent windows"
fi
