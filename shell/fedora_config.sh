###########################################################
# Script Name	: fedora_config.sh
# Description	:
# Arguments	: 
# Date		: 2019-12-07
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

if [[ $(id -u) != 0 ]]; then
    echo "Run as Root"
    exit
fi

# Before intallation
touch init_intalled_pkgs.txt
dnf list --intalled > init_intalled_pkgs.txt
init_intalled_pkgs=$(wc -l init_installed_pkgs.txt)
init_disk_usage=$(du -d 0 -h /)

pkgs=(
    'gnome-tweak-tool'
    'httpd'
    'python3'
    'vlc'
    'wireshark'
    'nmap'
    'vim'
    'php'
    'irssi'
    'gcc'
    'g++'
    'openssh-clients'
    'openssh-server'
    'qt5-designer'
    'tor'
    'xmlcopyeditor'
    'gparted'
    'bleachbit'
    'transmission'
    'git'
    'proxychains'
    'curl'
    'rar unrar'
    'python3-pip'
    'ShellCheck'
)


# Update package & and new repository
dnf check-update
dnf upgrade
dnf update


# Install some necessary tools
function install_packages(){
    for pkg in "${pkgs[@]}"; do
        echo ""
        echo -e "Installing package: \e[91m$pkg\e[0m"
        dnf -y install $pkg

        if [[ $? != 0 ]];then
            echo "Failed to install: $pkg"
        fi
    done

    dnf clean all
}

install_packages

# get bashrc and bash_aliases
git clone https://github.com/ablil/bash /tmp/bash
cp /tmp/bash/bash_aliases ~/.bash_aliases
echo "source ~/.bash_aliases" >> ~/.bashrc

# Install third party tools

# # install chrome
wget -O /tmp/chrome.rpm https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
dnf -y install /tmp/chrome.rpm
dnf -f /tmp/chrome.rpm

# Install VScode
wget -O /tmp/code.rpm 
dnf -y install /tmp/code.rpm
rm -f /tmp/code.rpm

# After installation
touch /init_intalled_pkgs.txt
dnf list --intalled > /init_intalled_pkgs.txt
newely_intalled_pkgs=$(wc -l /init_installed_pkgs.txt)
newely_disk_usage=$(du -d 0 -h /)
