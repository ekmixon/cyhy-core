#!/bin/bash

set -o nounset
set -o errexit
set -o pipefail

IMAGE_NAME="ncats/cyhy-core"
IMAGE_TAG="latest"

if [ $# -eq 1 ]
then
  IMAGE_TAG=$1
elif [ $# -eq 2 ]
then
  IMAGE_NAME=$1
  IMAGE_TAG=$2
fi

IMAGE_OUTPUT_FILE="ncats_cyhy_core_docker_image_$(date +'%Y%m%d').tgz"

docker build --tag "$IMAGE_NAME:$IMAGE_TAG" \
             --build-arg maxmind_license_type="full" \
             --build-arg maxmind_license_key="$(< maxmind_license.txt)" .
docker save "$IMAGE_NAME:$IMAGE_TAG" | gzip > "$IMAGE_OUTPUT_FILE"
