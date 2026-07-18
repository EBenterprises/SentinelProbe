#!/data/data/com.termux/files/usr/bin/bash
for node in $(cat ~/sentinel_probe/data/nodes.list); do
    curl -X POST http://$node:5001/deploy
done
