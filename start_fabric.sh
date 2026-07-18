#!/bin/bash
# Lightweight Fabric Orchestrator for Termux
echo "[*] Initializing Sovereign Fabric..."
cd ~/sentinel_probe

# Launch core components
nohup python3 core/orchestrator.py > logs/orchestrator.log 2>&1 &
nohup python3 core/gossip_node.py > logs/gossip.log 2>&1 &
nohup python3 core/dashboard_server.py > logs/dashboard.log 2>&1 &
nohup ./scripts/sync_ledger.sh > logs/ledger.log 2>&1 &

echo "[!] Fabric operational. Run 'pgrep -f python' to verify."
