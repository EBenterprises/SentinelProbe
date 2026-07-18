#!/bin/bash
# SentinelProbe Unified Controller

case "$1" in
    start)
        echo "[*] Initializing Sovereign Fabric..."
        nohup python3 ~/sentinel_probe/core/orchestrator.py > ~/sentinel_probe/orchestrator.log 2>&1 &
        nohup python3 ~/sentinel_probe/core/glb.py > ~/sentinel_probe/glb.log 2>&1 &
        nohup python3 ~/sentinel_probe/persist.sh > ~/sentinel_probe/persistence.log 2>&1 &
        echo "[!] All services active."
        ;;
    stop)
        echo "[*] Terminating Fabric..."
        pkill -f python
        rm -f ~/sentinel_probe/*.pid
        echo "[!] Fabric terminated."
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        ;;
esac

    audit)
        ~/sentinel_probe/scripts/audit_engine.sh
        ;;

    dashboard)
        nohup python3 ~/sentinel_probe/core/dashboard_server.py > ~/sentinel_probe/dashboard.log 2>&1 &
        echo "[!] Dashboard active on port 8080."
        ;;

    resilience_inject)
        # Deploy Gossip and Vault services
        nohup python3 ~/sentinel_probe/core/gossip_node.py > ~/sentinel_probe/gossip.log 2>&1 &
        python3 ~/sentinel_probe/core/vault.py
        echo "[!] Resilience layers injected."
        ;;
