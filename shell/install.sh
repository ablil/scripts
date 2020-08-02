###########################################################
# Script Name	: install.sh
# Description	: Install package using dnf and keep track of packages
# Arguments	: 
# Date		: 2020-08-02
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

sudo dnf install "$@" && {
    current_time=$(date +%Y-%m-%d-%H:%M)
    echo "$current_time install $@" >> /opt/packages
}
