#!/data/data/com.termux/files/usr/bin/bash
# Command all nodes to apply firewall rules based on global ledger
NODES=$(cat ~/sentinel_probe/data/nodes.list)
for node in $NODES; do
    curl -X POST http://$node:5001/remediate -d "action=apply_firewall"
done
