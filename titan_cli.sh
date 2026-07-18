#!/bin/bash
case "$1" in
    "core")    python3 -c "from clusters.sentinel_core import SentinelCore; SentinelCore().$2()" ;;
    "commerce") python3 -c "from clusters.commerce_engine import CommerceEngine; CommerceEngine().$2('$3', '$4')" ;;
    "utility")  python3 -c "from clusters.utility_fabric import UtilityFabric; UtilityFabric().$2('$3')" ;;
    *) echo "Usage: ./titan_cli.sh [core|commerce|utility] [method] [args...]" ;;
esac
