#!/bin/bash

usage() {
    echo "usage: bash $0 <app-name>";
    echo "    A directory with the same name app will be created";
    echo "";
    echo "    example: bash $0 my-app";
    exit 0;
}

# check arguments validity
[[ -z "$1" ]] && usage;
[[ "$1" = "-h" ]] && usage;
[[ ! -x "$(pwd)" ]] && { echo "You do NOT have exec permission on $(pwd)"; exit 1; }
[[ ! -r "$(pwd)" ]] && { echo "You do NOT have read permission on $(pwd)"; exit 1; }
[[ ! -w "$(pwd)" ]] && { echo "You do NOT have write permission on $(pwd)"; exit 1; }

# create app directory
appname="$1"
mkdir -p -v ./$appname
cd ./$appname

# init npm package and install dependencies
npm init -y
npm install express
npm install morgan
npm install cors
npm install nodemon
npm install .eslintrc.yml


# create app file structure
mkdir -p -v ./src/models/
mkdir -p -v ./src/routes/
mkdir -p -v ./src/config/
mkdir -p -v ./github/workflows/build.yml
mkdir -p -v ./docker-data/

touch ./src/index.js
touch ./docker-data/.gitkeep
touch .gitignore
touch .dockerignore
touch .env
touch .env.example
touch README.md
touch docker-compose.yml
touch Dockerfile

# .gitignore 
echo node_modules >> .gitignore
echo .env >> .gitignore


# .dockerignore
echo node_modules >> .dockerignore
echo .git >> .dockerignore
echo docker-data >> .dockerignore
