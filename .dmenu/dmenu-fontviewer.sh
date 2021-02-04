#!/bin/sh

# Dmenu scripts for viewing fonts

choice=$(fc-list | awk '{print $1}' | sed 's/://g' | dmenu -l 20 -p 'Font Viewer- ')
display "$choice"
