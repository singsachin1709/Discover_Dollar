#!/usr/bin/env bash
set -euo pipefail

# run on remote VM as deploy user (or via ssh action)
cd /opt/myapp || mkdir -p /opt/myapp && cd /opt/myapp
# ensure docker-compose.yml exists in /opt/myapp (e.g., git clone or scp)
git pull || true
# pull images from Docker Hub, recreate containers
docker compose pull
docker compose up -d --remove-orphans
docker image prune -f

