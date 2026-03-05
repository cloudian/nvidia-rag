#!/usr/bin/env bash

set -euxo pipefail

#cd "$(dirname "$0")"

docker build -t rag_server src/nvidia_rag/rag_server
docker run -d --name rag_server_container -p 8000:8000 rag_server
