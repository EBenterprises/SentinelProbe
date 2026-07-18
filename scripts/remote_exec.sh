#!/data/data/com.termux/files/usr/bin/bash
# Execute command across all nodes in the mesh
CMD=$1
NODES=$(cat ~/sentinel_probe/data/nodes.list)

for node in $NODES; do
    echo "[*] Executing on $node: $CMD"
    curl -s -X POST http://$node:5002/command          -H "Content-Type: application/json"          -d "{\"cmd\": \"$CMD\"}"
done
