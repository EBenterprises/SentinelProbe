#!/bin/bash
# Final deployment orchestrator
echo "[*] Deploying Sovereign Fabric Infrastructure..."
chmod +x ~/sentinel_probe/scripts/*.sh ~/sentinel_probe/core/*.py
~/sentinel_probe/manage.sh stop
~/sentinel_probe/manage.sh start
nohup ~/sentinel_probe/scripts/sync_ledger.sh > ~/sentinel_probe/ledger_sync.log 2>&1 &
echo "[!] Sovereign Fabric is fully provisioned and secured."
