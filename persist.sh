#!/bin/bash
while true; do
    if ! pgrep -f "orchestrator.py" > /dev/null; then
        nohup python ~/sentinel_probe/core/orchestrator.py > ~/sentinel_probe/v2.log 2>&1 &
    fi
    sleep 30
done
