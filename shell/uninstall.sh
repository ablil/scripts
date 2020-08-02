###########################################################
# Script Name	: uninstall.sh
# Description	:
# Arguments	: 
# Date		: 2020-08-02
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

sudo dnf remove "$@" && {
    current_time=$(date +%Y-%m-%d-%H:%M)
    echo "$current_time remove $@" >> /opt/packages
}
