#!/bin/bash
# Multi-Kernel Dispatcher
KERNEL=$1
ACTION=$2
PAYLOAD=$3
python3 "$ROOT/$KERNEL/kernel.py" "$ACTION" "$PAYLOAD"
