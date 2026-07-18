#!/bin/bash
REGISTRY="$BASE_DIR/kernel_registry.idx"
K_TARGET=$1
ACTION=$2
DATA=$3

# O(1) path resolution
PATH_TO_K=$(grep "^$K_TARGET:" "$REGISTRY" | cut -d':' -f2)
python3 "$PATH_TO_K" "$K_TARGET" "$ACTION" "$DATA"
