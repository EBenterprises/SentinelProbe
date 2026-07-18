#!/data/data/com.termux/files/usr/bin/bash
while true; do
    # Verify core processes exist
    SERVICES=("orchestrator.py" "gossip_node.py" "dashboard_server.py")
    for s in "${SERVICES[@]}"; do
        if ! pgrep -f "$s" > /dev/null; then
            echo "[!] $s dead. Reviving..."
            python3 ~/sentinel_probe/core/$s > ~/sentinel_probe/logs/${s%.py}.log 2>&1 &
        fi
    done
    ~/sentinel_probe/scripts/audit_engine.sh
    sleep 60
done
