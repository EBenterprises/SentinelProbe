#!/bin/bash
# Master Bootstrap for Sovereign Fabric

# 1. Cleanup
pkill -f python3

# 2. Setup Permissions
chmod -R 700 ~/sentinel_probe/
termux-fix-shebang ~/sentinel_probe/scripts/*.sh

# 3. Launch Services
echo "[*] Launching Fabric Stack..."
cd ~/sentinel_probe
nohup python3 core/orchestrator.py > logs/orchestrator.log 2>&1 &
nohup python3 core/gossip_node.py > logs/gossip.log 2>&1 &
nohup python3 core/heuristic_engine.py > logs/heuristic.log 2>&1 &
nohup python3 core/cognitive_balancer.py > logs/balancer.log 2>&1 &
nohup python3 core/dashboard_server.py > logs/dashboard.log 2>&1 &
nohup ./scripts/sync_ledger.sh > logs/ledger.log 2>&1 &
nohup ./scripts/background_monitor.sh > logs/monitor.log 2>&1 &

echo "[!] Fabric fully initialized."
