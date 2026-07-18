#!/bin/bash
# SentinelProbe Suite Initialization

# 1. Mesh Query Tool
cat <<'EOF_TOOL' > ~/sentinel_probe/scripts/mesh_query.sh
#!/bin/bash
echo "[*] Querying Mesh Nodes..."
for node in $(cat ~/sentinel_probe/data/nodes.list); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://$node:5001/task/claim)
    echo "Node $node: Status $STATUS"
done
EOF_TOOL

# 2. Fabric-wide Deployment Trigger
cat <<'EOF_TOOL' > ~/sentinel_probe/scripts/fabric_deploy.sh
#!/bin/bash
echo "[*] Broadcasting Deployment to Mesh..."
for node in $(cat ~/sentinel_probe/data/nodes.list); do
    curl -X POST http://$node:5001/deploy
    echo "Broadcasted to $node"
done
EOF_TOOL

# 3. Mesh Stats Aggregator
cat <<'EOF_TOOL' > ~/sentinel_probe/scripts/mesh_stats.sh
#!/bin/bash
echo "[*] Mesh Ledger Size: $(wc -l < ~/sentinel_probe/data/mesh.ledger) lines"
echo "[*] Pending Tasks: $(grep -c "pending" ~/sentinel_probe/data/mesh.ledger)"
EOF_TOOL

# Finalize permissions
chmod +x ~/sentinel_probe/scripts/*.sh
echo "[!] Suite initialized. Use '~/sentinel_probe/scripts/mesh_query.sh' to audit."
