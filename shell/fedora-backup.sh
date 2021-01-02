#!/bin/bash
# Author: ablil
# Description: Backup automation for config file on Linux system

function usage() {
    echo "Backup config file on Linux System"
    echo "Usage: bash $0 backupdir"
    echo ""
    echo "    backupdir: where to save files (created if does NOT exist)"
    exit 1;
}

if [[ $# != 1 ]]; then
    usage;
fi

backupdir=$1

# ssh
if [[ -d ~/.ssh ]]; then
    mkdir -p "$backupdir/ssh"
    cp ~/.ssh/* "$backupdir/ssh/"
fi

# gpg
if [[ -d ~/.gnupg ]]; then
    mkdir -p "$backupdir/gpg"
    gpg --armor --export > "$backupdir/gpg/publickey.asc";
    gpg --armor --export-secret-key > "$backupdir/gpg/secretkey.asc";
    gpg --export-ownertrust > "$backupdir/gpg/dbtrust.txt"
fi

# shell and vim
mkdir -p "$backupdir/shell"
[[ -f ~/.bashrc ]] && cp ~/.bashrc "$backupdir/shell/"
[[ -f ~/.zshrc ]] && cp ~/.zshrc "$backupdir/shell/"
[[ -f ~/.bash_aliases ]] && cp ~/.bash_aliases "$backupdir/shell/"
[[ -f ~/.aliases ]] && cp ~/.aliases "$backupdir/shell/"
[[ -f ~/.vimrc ]] && cp ~/.vimrc "$backupdir/shell/"
[[ -f ~/.tmux.conf ]] && cp ~/.tmux.conf "$backupdir/shell/"

# vscode
mkdir -p "$backupdir/vscode"
[[ -f ~/.config/Code/User/settings.json ]] && cp ~/.config/Code/User/settings.json "$backupdir/vscode"
[[ -d ~/.config/Code/User/snippets ]] && cp -r ~/.config/Code/User/snippets/ "$backupdir/vscode/"

# personal directory
