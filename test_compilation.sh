#!/bin/bash

# Script para validar compilação de todas as soluções do Exam 02
# Compila com flags: -Wall -Wextra -Werror

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "Validação de Compilação - Exam 02"
echo "Flags: -Wall -Wextra -Werror"
echo "=========================================="
echo ""

total_files=0
success_count=0
error_count=0
warning_count=0
errors_log=""

# Função para compilar um arquivo
compile_file() {
    local file=$1
    local level=$2
    
    echo -n "Compilando $file... "
    
    # Compilar com as flags requeridas
    output=$(gcc -Wall -Wextra -Werror "$file" -o /tmp/test_compile_$$ 2>&1)
    result=$?
    
    if [ $result -eq 0 ]; then
        echo -e "${GREEN}✓ OK${NC}"
        rm -f /tmp/test_compile_$$
        return 0
    else
        echo -e "${RED}✗ ERRO${NC}"
        errors_log="${errors_log}\n${RED}[ERRO]${NC} $file:\n$output\n"
        return 1
    fi
}

# Compilar Level 0
echo "=== Level 0 (Básico) ==="
for file in exam-02-solutions/level-0/*.c; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
        if compile_file "$file" "0"; then
            success_count=$((success_count + 1))
        else
            error_count=$((error_count + 1))
        fi
    fi
done
echo ""

# Compilar Level 1
echo "=== Level 1 (Intermediário) ==="
for file in exam-02-solutions/level-1/*.c; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
        if compile_file "$file" "1"; then
            success_count=$((success_count + 1))
        else
            error_count=$((error_count + 1))
        fi
    fi
done
echo ""

# Compilar Level 2
echo "=== Level 2 (Avançado) ==="
for file in exam-02-solutions/level-2/*.c; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
        if compile_file "$file" "2"; then
            success_count=$((success_count + 1))
        else
            error_count=$((error_count + 1))
        fi
    fi
done
echo ""

# Compilar Level 3
echo "=== Level 3 (Expert) ==="
for file in exam-02-solutions/level-3/*.c; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
        if compile_file "$file" "3"; then
            success_count=$((success_count + 1))
        else
            error_count=$((error_count + 1))
        fi
    fi
done
echo ""

# Resumo
echo "=========================================="
echo "RESUMO DA VALIDAÇÃO"
echo "=========================================="
echo "Total de arquivos: $total_files"
echo -e "${GREEN}Sucessos: $success_count${NC}"
echo -e "${RED}Erros: $error_count${NC}"
echo ""

# Mostrar erros se houver
if [ $error_count -gt 0 ]; then
    echo "=========================================="
    echo "DETALHES DOS ERROS"
    echo "=========================================="
    echo -e "$errors_log"
fi

# Status final
if [ $error_count -eq 0 ]; then
    echo -e "${GREEN}✓ Todas as soluções compilaram com sucesso!${NC}"
    exit 0
else
    echo -e "${RED}✗ Algumas soluções falharam na compilação.${NC}"
    exit 1
fi
