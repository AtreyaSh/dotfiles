#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
[[ -f ~/.profile ]] && . ~/.profile

# update environmental variables
export GPG_TTY="$(tty)"
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
export EDITOR="vim"
export TERMINAL="termite"
export R_PROFILE_USER="$HOME/.Rprofile"
export QT_QPA_PLATFORMTHEME="qt5ct"

# update PATH variable
export PATH="$PATH:$HOME/bin:$HOME/.local/bin"
export PATH="$PATH:$(ruby -e 'puts Gem.user_dir')/bin"