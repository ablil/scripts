###########################################################
# Script Name	: oracle_xe.sh
# Description	: Install Orace Xe on Fedora (tested on Fedore 31)
# Arguments	: 
# Date		: 2020-01-18
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################
function check_root(){
		if [[ $(id -u) != 0 ]];then
				echo -e "${RED}[-] run as root ${END}"
				exit
		fi
};

function check_requirement(){
	if [[ ! -s oracle-database-xe-18c-1.0-1.x86_64.rpm ]];then
		echo "[-] oracle-database-xe-18c-1.0-1.x86_64.rpm NOT FOUND";
		echo "[?]Download from: https://www.oracle.com/database/technologies/xe-downloads.html"
		echo  "[-] Aborting ... ";
	fi
	exit 1
}

function install_dependencies(){
	# install dependencies
	# this could be different based on the user configuration and environement

	# install compat-libcap1
	echo "[?] Downloading compat-libcap1-1.10-7.el7.i686.rpm ...";
	curl http://mirror.centos.org/centos/7/os/x86_64/Packages/compat-libcap1-1.10-7.el7.i686.rpm --output compat-libcap1.rpm

	echo "[?] Installing compat-libcap1-1.10-7.el7.i686.rpm ...";
	rpm -i compat-libcap1.rpm

	# install compat-libstdc++-33 
	echo "[?] Downloading compat-libstdc+ ...";
	curl https://www.rpmfind.net/linux/fedora-secondary/releases/30/Everything/i386/os/Packages/c/compat-libstdc++-33-3.2.3-68.16.fc26.1.i686.rpm --output compat-libstdc.rpm

	echo "[?] Installing compat-libstdc+ ..."
	rpm -i compat-libstdc.rpm

}

function install_oracle(){
	# Check the offcial docs for more information
	# https://docs.oracle.com/en/database/oracle/oracle-database/18/xeinl/installation-guide.html#GUID-31891F22-B1FA-4489-A1C5-195E6B3D89C8

	echo "[?] Downloading oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm ...";
	curl -o oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm https://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm

	echo "[?] Installing oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm ..."
	yum -y localinstall oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm

	# download oracle from official website then run
	yum -y localinstall oracle-database-xe-18c-1.0-1.x86_64.rpm

	# configure oracle xe database
	# You could change parameters on configuration file: /etc/sysconfig/oracle-xe-18c.conf
	# leave empty for default parameters
	/etc/init.d/oracle-xe-18c configure

	# setup oracle xe env variable
	export ORACLE_SID=XE
	export ORAENV_ASK=NO
	. /opt/oracle/product/18c/dbhomeXE/bin/oraenv
	
}

check_root
check_requirement
install_dependencies
install_oracle