#!/data/data/com.termux/files/usr/bin/bash
# Sync local ledger with peers and hash-verify
while true; do
    HASH=$(sha256sum ~/sentinel_probe/data/mesh.ledger | awk '{print $1}')
    for node in $(cat ~/sentinel_probe/data/nodes.list); do
        curl -s -X POST http://$node:5001/ledger/verify -d "hash=$HASH"
    done
    sleep 60
done
