#!/bin/bash
# Author: ablil
# Description: auto generate Entity, repository, service and resource for spring app

# exit on any error
set -e

function usage() {
    echo "Generate Entity, EntityRepository, EntityServcie and EntityResource";
    echo "Usage:"
    echo "    bash $0 entityname packagename app_directory_path"
    echo ""
    echo "Example:"
    echo "    bash $0 user com.mypackage.myapp ~/project/mypackage/app/";
    exit 1;
}

template_dir=~/Templates/spring/
entityname=$1
packagename=$2
appdir=$3

# verifying arguments

if [[ ! -d $template_dir ]]; then
    echo "Template directory $template_dir does NOT exist";
    exit 2;
fi

if [[ $# != 3 ]]; then
    usage
fi

if [[ ! -d $appdir ]]; then
    echo "app/ directory does NOT exist or you don't have permission";
    exit 1;
else
    if [[ ! -d "$appdir/src/" ]]; then
        echo "$appdir/src/ does NOT exist";
    fi
fi

# create package sub directories
package_dir="$appdir/src/main/java/$(echo $packagename | sed 's/\./\//g')";

domain_dir="$package_dir/domain";
entity_file="$package_dir/domain/${entityname^}.java";

repositories_dir="$package_dir/repositories";
repository_file="$package_dir/repositories/${entityname^}Repository.java";

services_dir="$package_dir/services";
service_file="$package_dir/services/${entityname^}Service.java";

web_dir="$package_dir/web";
web_file="$package_dir/web/${entityname^}Resource.java";

mkdir -p $domain_dir $repositories_dir $services_dir $web_dir;

# copy templates 
cp -u "$template_dir/Entity.java" $entity_file
cp -u "$template_dir/EntityRepository.java" $repository_file
cp -u "$template_dir/EntityService.java" $service_file
cp -u "$template_dir/EntityResource.java" $web_file

# Replate Entity keyword with user entity
sed -i "s/packagename/$packagename/g" $entity_file $repository_file $service_file $web_file
sed -i "s/entity/$entityname/g" $entity_file $repository_file $service_file $web_file
sed -i "s/entities/${entityname}s/g" $entity_file $repository_file $service_file $web_file
sed -i "s/Entity/${entityname^}/g" $entity_file $repository_file $service_file $web_file
