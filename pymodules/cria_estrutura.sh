#!/usr/bin/env bash
set -euo pipefail

read -rp "Nome da pasta principal (parent): " BASE_DIR
read -rp "Quantas pastas de exercício criar (ex0..exN)? " COUNT

if [[ -z "${BASE_DIR}" ]]; then
  echo "❌ Nome da pasta principal não pode ser vazio."
  exit 1
fi

if ! [[ "${COUNT}" =~ ^[0-9]+$ ]]; then
  echo "❌ Quantidade deve ser um número inteiro."
  exit 1
fi

mkdir -p "${BASE_DIR}"
for ((i = 0; i < COUNT + 1; i++)); do
  mkdir -p "${BASE_DIR}/ex${i}"
done

echo "Estrutura criada em ${BASE_DIR}/ex0..ex$((COUNT))"
