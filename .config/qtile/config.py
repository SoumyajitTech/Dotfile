# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
terminal = "urxvt"
myConfig = "/home/argha/.config/qtile/config.py"    # The Qtile config file location

keys = [
         Key([mod], "t",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "r",
             lazy.spawncmd(),
             desc='Launch Terminal Command'
             ),
         Key([mod], "e",
             lazy.spawn(myTerm+ " -e ranger"),
             desc='Launches My Terminal'
             ),
         Key([mod], "w",
             lazy.spawn("qutebrowser"),
             desc='Launches My Terminal'
             ),
         Key([mod], "d",
             lazy.spawn("dmenu_run -i -nf '#fcfcfc' -nb '#292d3e' -sf '#fcfcfc' -sb '#0077bb' -p 'Run: '"),
             desc='Dmenu Run Launcher'
             ),
         Key(["mod1", "control"], "d",
             lazy.spawn("dmenufm"),
             desc='Dmenufm Run Launcher'
             ),
         Key([mod], "z",
             lazy.spawn("morc_menu"),
             desc='Morc_menu Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key(["control"], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "c",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.spawn("arcolinux-logout"),
             desc='Shutdown Qtile'
             ),
         Key([mod, "mod1"], "r",
             lazy.spawn("prompt 'Do you want to reboot' reboot"),
             desc='Restart'
             ),
         Key([mod, "mod1"], "q",
             lazy.spawn("prompt 'Do you want to shutdown' poweroff"),
             desc='Shutdown'
             ),
         Key([mod], "Return",
             lazy.spawn("emacs"),
             desc='Doom Emacs'
             ),
         Key([mod, "control"], "x",
             lazy.spawn("xkill"),
             desc='Launch xkill'
             ),
         Key([mod], "s",
             lazy.spawn("i3-scrot"),
             desc='Take Full Screenshots'
             ),
         Key([mod], "x",
             lazy.spawn("lock"),
             desc='Lock Screen'
             ),
### Terminal based application KeyBindings
         Key([mod], "F1",
             lazy.spawn("pavucontrol"),
             desc='Pavucontrol'
             ),
         Key([mod], "F2",
             lazy.spawn(terminal+" -e alsamixer"),
             desc='Alsamixer Launcher'
             ),
         Key([mod], "F3",
             lazy.spawn("./.local/bin/dmenumount"),
             desc='Mount Android or USB'
             ),
         Key([mod], "F4",
             lazy.spawn("./.local/bin/dmenuumount"),
             desc='Unmount Android or USB'
             ),
         Key([mod], "F5",
             lazy.spawn(myTerm+" -e mocp"),
             desc='Mocp player Launcher'
             ),
         Key([mod], "F9",
             lazy.spawn("./.local/bin/dmenuunicode"),
             desc='Mocp player Launcher'
             ),

### Variety Keys With PYWAL
    #     key(["mod1", "shift"], "f",
    #         lazy.spawn("variety -f && wal -i $(cat $HOME/.config/variety/wallpaper/wallpaper.jpg.txt"),
    #         desc='variety 1'
    #         ),          
    #     key(["mod1", "shift"], "n",
    #         lazy.spawn("variety -n && wal -i $(cat $HOME/.config/variety/wallpaper/wallpaper.jpg.txt"),
    #         desc='variety 2'
    #         ),          
    #     key(["mod1", "shift"], "p",
    #         lazy.spawn("variety -p && wal -i $(cat $HOME/.config/variety/wallpaper/wallpaper.jpg.txt"),
    #         desc='variety 3'
    #         ),          
    #     key(["mod1", "shift"], "t",
    #         lazy.spawn("variety -t && wal -i $(cat $HOME/.config/variety/wallpaper/wallpaper.jpg.txt"),
    #         desc='variety 4'
    #        ),          

### KeyBindings for Brightness
         Key([], "XF86MonBrightnessUp",
             lazy.spawn("xbacklight -inc 5"),
             desc='Increase the brightness'
             ),
         Key([], "XF86MonBrightnessDown",
             lazy.spawn("xbacklight -dec 5"),
             desc='Decrease the brightness'
             ),

### KeyBindings for Sounds
         Key([], "XF86AudioMute",
             lazy.spawn("amixer -q set Master toggle"),
             desc='Mute'
             ),
         Key([], "XF86AudioLowerVolume",
             lazy.spawn("amixer -c 0 sset Master 1- unmute"),
             desc='Volume Low'
             ),
         Key([], "XF86AudioRaiseVolume",
             lazy.spawn("amixer -c 0 sset Master 1+ unmute"),
             desc='Volume Up'
             ),
         Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
         Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
         Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
         Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),


### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),

### Change Focus
         Key([mod], "Down",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "Up",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod], "Left",
             lazy.layout.left(),
             desc='Move focus Left in current stack pane'
             ),
         Key([mod], "Right",
             lazy.layout.right(),
             desc='Move focus Right in current stack pane'
             ),
### Shift Windows in group
         Key([mod, "shift"], "Right",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "Left",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),

### Resize window
         Key([mod, "control"], "Right",
             lazy.layout.grow_right(),
             lazy.layout.grow(),
             lazy.layout.increase_ratio(),
             lazy.layout.delete(),
             ),
         Key([mod, "control"], "Left",
             lazy.layout.grow_left(),
             lazy.layout.shrink(),
             lazy.layout.decrease_ratio(),
             lazy.layout.add(),
             ),
         Key([mod, "control"], "Up",
             lazy.layout.grow_up(),
             lazy.layout.grow(),
             lazy.layout.decrease_nmaster(),
             ),
         Key([mod, "control"], "Down",
             lazy.layout.grow_down(),
             lazy.layout.shrink(),
             lazy.layout.increase_nmaster(),
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),

### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
### Dmenu scripts launched with ALT + CTRL + KEY
    
         Key(["mod1", "control"], "e",
             lazy.spawn("./.dmenu/dmenu-edit-configs.sh"),
             desc='Dmenu script for editing config files'
             ),
         Key(["mod1", "control"], "m",
             lazy.spawn("./.dmenu/dmenu-sysmon.sh"),
             desc='Dmenu system monitor script'
             ),
         Key(["mod1", "control"], "p",
             lazy.spawn("passmenu"),
             desc='Passmenu'
             ),
         Key(["mod1", "control"], "r",
             lazy.spawn("./.dmenu/dmenu-reddio.sh"),
             desc='Dmenu reddio script'
             ),
         Key(["mod1", "control"], "w",
             lazy.spawn("./.dmenu/dmenu-surfraw.sh"),
             desc='Dmenu surfraw script'
             ),
         Key(["mod1", "control"], "t",
             lazy.spawn("./.dmenu/dmenu-trading.sh"),
             desc='Dmenu trading programs script'
             ),
         Key(["mod1", "control"], "s",
             lazy.spawn("./.dmenu/dmenu-scrot.sh"),
             desc='Dmenu scrot script'
             ),
]

#     keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name), lazy.group[i.name].toscreen())) # Send current window to another group & move
groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
# group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["WWW", "DEV", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX", "?",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "floating", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1", "control"], "Right", lazy.screen.next_group()),
        Key(["mod1", "control"], "Left", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "control"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #########################################################
    ################ assgin apps to groups ##################
    #########################################################
    d["1"] = ["qutebrowser", "qutebrowser"]
    d["2"] = [ "Terminator", "terminator"]
    d["3"] = ["libreoffice-writer", "libreoffice"]
    d["4"] = ["Pcmanfm", "pcmanfm"]
    d["5"] = ["Gimp", "gimp"]

    ##########################################################
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            # client.group.cmd_toscreen()

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "f2072a",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]

colors = [["#292d3e", "#292d3e"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

###################################
##### DEFAULT WIDGET SETTINGS #####
###################################
widget_defaults = dict(
    font="FontAwesome",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 10,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 3,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[5],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.Pacman(
                       update_interval = 1800,
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('pamac-manager')},
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = "Updates",
                       padding = 5,
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       foreground = colors[2],
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              # widget.textbox(
              #          text = " 🌡",
              #          padding = 2,
              #          foreground = colors[2],
              #          background = colors[5],
              #          fontsize = 11
              #          ),
              widget.CPU(
                       format = 'CPU {load_percent}%',
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e bashtop')},
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[4],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net(
                       interface = "wlp1s0",
                       format = '{down}↓↑{up}',
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Battery(
                       format = '{percent:2.0%}',
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = " ",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 2
                       ),
              widget.Volume(
                       channel = 'Master',
                       volume_app = 'alsamixer',
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[4],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       format = "%a, %b %d [%I:%M%P]"
                       # mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' ')},
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[0],
                       background = colors[5]
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
             
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=18)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.9, size=18)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=18))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'URxvt'},
    {'wmclass': 'GParted'},
    {'wmclass': 'Lxappearance'},
    {'wmclass': 'Nitrogen'},
    {'wmclass': 'Pamac-manager'},
    {'wmclass': 'Pavucontrol'},
    {'wmclass': 'Simple-scan'},
    {'wmclass': 'Font-manager'},
    {'wmclass': 'Manjaro Settings Manager'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
