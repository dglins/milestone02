#!/usr/bin/env bash
set -euo pipefail

# Define o diretório base
BASE_DIR="mod00"

# Cria o diretório base e as subpastas ex0..ex7
for i in {0..7}; do
  mkdir -p "${BASE_DIR}/ex${i}"
done

echo "Estrutura criada em ${BASE_DIR}/ex0..ex7"
