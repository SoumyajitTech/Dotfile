typeset -U PATH path

# Other XDG paths
export XDG_DATA_HOME=${XDG_DATA_HOME:="$HOME/.local/share"}
export XDG_CACHE_HOME=${XDG_CACHE_HOME:="$HOME/.cache"}
export XDG_CONFIG_HOME=${XDG_CONFIG_HOME:="$HOME/.config"}
export JAVA_HOME=${JAVA_HOME:="/usr/share/java"}

# Doesn't seem to work
export ANDROID_SDK_HOME="$XDG_CONFIG_HOME"/android
export ANDROID_AVD_HOME="$XDG_DATA_HOME"/android
export ANDROID_EMULATOR_HOME="$XDG_DATA_HOME"/android
export ADB_VENDOR_KEY="$XDG_CONFIG_HOME"/android

# Disable files
export LESSHISTFILE=-

# Fixing Paths
export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc
export XSERVERRC="$XDG_CONFIG_HOME"/X11/xserverrc
export GEM_PATH="$XDG_DATA_HOME/ruby/gems"
export GEM_SPEC_CACHE="$XDG_DATA_HOME/ruby/specs"
export GEM_HOME="$XDG_DATA_HOME/ruby/gems"
export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc
export GOPATH="$XDG_DATA_HOME"/go
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export ZDOTDIR=$HOME/.config/zsh
export HISTFILE="$XDG_DATA_HOME"/zsh/zsh_history
export CARGO_HOME="$XDG_DATA_HOME"/cargo

# Scaling
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_SCALE_FACTOR=1
export QT_SCREEN_SCALE_FACTORS="1;1;1"
export GDK_SCALE=1
export GDK_DPI_SCALE=1

# Default Apps
export EDITOR="nvim"
export READER="zathura"
export VISUAL="nvim"
export TERMINAL="st"
export BROWSER="brave"
export VIDEO="mpv"
export IMAGE="sxiv"
export COLORTERM="truecolor"
export OPENER="xdg-open"
export PAGER="less"
export WM="bspwm"

export CM_SELECTIONS="clipboard"
export CM_DEBUG=0
export CM_OUTPUT_CLIP=1
export CM_MAX_CLIPS=10

# Path
path=("$HOME/.local/bin" "$HOME/.local/bin/statusbar" "$HOME/scripts/dragon" "$HOME/.local/bin/i3cmds" "$HOME/scripts/i3" "$HOME/scripts/pulse"
	"$HOME/.scripts" "$HOME/.local/bin/bspwm" "$HOME/scripts/bspwm" "$HOME/scripts/lemonbar" "$HOME/.local/bin/transmission"
	"$HOME/bin/tweetdeck-linux-x64" "$XDG_DATA_HOME/gems/bin" "$HOME/go/bin" "$HOME/.cargo/bin"
	"$XDG_DATA_HOME/npm/bin" "$path[@]")
export PATH

export FFF_TRASH_CMD="trash-put"
export FFF_TRASH=~/.local/share/Trash/files
export FFF_KEY_MKDIR="f"
export FFF_KEY_MKFILE="i"
export FFF_TRASH=~/.local/share/Trash/files
export FFF_FAV1=~/videos/anime
export FFF_FAV2=~/documents/Uni
export FFF_FAV3=~/pictures/Wallpapers/wallpapers
export FFF_MARK_FORMAT="> %f"
export FFF_FILE_FORMAT=" %f"

export NNN_BMS='v:~/videos;a:~/videos/anime'
export NNN_TRASH=1
export NNN_PLUG='o:fzopen'

# Start blinking
export LESS_TERMCAP_mb=$(tput bold; tput setaf 2) # green
# Start bold
export LESS_TERMCAP_md=$(tput bold; tput setaf 2) # green
# Start stand out
export LESS_TERMCAP_so=$(tput bold; tput setaf 3) # yellow
# End standout
export LESS_TERMCAP_se=$(tput rmso; tput sgr0)
# Start underline
export LESS_TERMCAP_us=$(tput smul; tput bold; tput setaf 1) # red
# End Underline
export LESS_TERMCAP_ue=$(tput sgr0)
# End bold, blinking, standout, underline
export LESS_TERMCAP_me=$(tput sgr0)
