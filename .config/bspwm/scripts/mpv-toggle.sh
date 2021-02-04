#!/bin/bash
if pgrep -x "mpv" > /dev/null
then
	killall mpv && notify-send "MPV is Stopped"
else
	mpv
fi
