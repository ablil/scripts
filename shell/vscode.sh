###########################################################
# Script Name	: scripts/shell/vscode_extensions.sh
# Description	: install extension and import settings.json from gist
# Date		: 2020-03-25
# Author	: ablil
# Email		: ablil@protonmail.com
###########################################################
code --install-extension bmewburn.vscode-intelephense-client
code --install-extension CoenraadS.bracket-pair-colorizer-2
code --install-extension DotJoshJohnson.xml
code --install-extension ecmel.vscode-html-css
code --install-extension fabianlauer.vs-code-xml-format
code --install-extension felixfbecker.php-intellisense
code --install-extension felixfbecker.php-pack
code --install-extension formulahendry.vscode-mysql
code --install-extension Gruntfuggly.todo-tree
code --install-extension hollowtree.vue-snippets
code --install-extension jcbuisson.vue
code --install-extension LaurentTreguier.vscode-simple-icons
code --install-extension mikestead.dotenv
code --install-extension ms-python.python
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension ms-vscode-remote.remote-ssh-edit
code --install-extension ms-vscode.cpptools
code --install-extension octref.vetur
code --install-extension ritwickdey.live-sass
code --install-extension ritwickdey.LiveServer
code --install-extension RobbOwen.synthwave-vscode
code --install-extension sibiraj-s.vscode-scss-formatter
code --install-extension tomoki1207.pdf
code --install-extension vscode-icons-team.vscode-icons
code --install-extension vscodevim.vim
code --install-extension xyz.plsql-language
code --install-extension yzhang.markdown-all-in-one

wget https://gist.githubusercontent.com/ablil/2bce18ba864eee1300b9264e469467e0/raw/d6a029c19fc5e5aadab6a8e1b591c66dcab5881c/settings.json
mv settings.json ~/.config/Code/User/
