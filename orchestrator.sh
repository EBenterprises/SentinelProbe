#!/bin/bash
# Multi-Kernel Orchestrator for 100+ Nodes
TARGET=$1
ACTION=$2
DATA=$3
python3 "$ROOT/$TARGET/kernel.py" "$ACTION" "$DATA"
