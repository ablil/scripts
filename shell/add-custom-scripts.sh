###########################################################
# Script Name	: add-custom-scripts.sh
# Description	: add all executable function in directory (current or given)
#           to ~/.local/bin as user-defined commands (whithout .sh suffix)
# Arguments	: 
# Date		: 2020-10-22
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################


usage() {
    echo "Usage: bash $(basename $0) <direcotyr>"
    echo -e "\tadd .sh scripts as custom command to ~/.local/bin"
    echo ""
    echo -e "\texample: bash $(basename $0) /my/directory/containing/bash/scripts/"
    echo "Do not forget to add ~/.local/bin to your PATH variable"
    exit 1;
}

# check cli arguments
directory="$1"
[[ "$1" = "-h" ]] && usage;
[[ -z "$1" ]] &&  {
    directory="$(pwd)";
    echo "Using the current directory";
}
[[ ! -r "$directory" ]] && { echo "You do NOT have read permission on $(pwd)"; exit 1; }
[[ ! -w "$directory" ]] && { echo "You do NOT have write permission on $(pwd)"; exit 1; }


# parse directory for .sh scripts
cd "$directory"
for f in $(ls *.sh); do
    filename=$(basename -s '.sh' "$f")
    cp -v -u "$f" ~/.local/bin/$filename
    chmod +x ~/.local/bin/$filename
done;
cd -
