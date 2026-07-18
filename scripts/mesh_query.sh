#!/data/data/com.termux/files/usr/bin/bash
for node in $(cat ~/sentinel_probe/data/nodes.list); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://$node:5001/task/claim)
    echo "Node $node: Status $STATUS"
done
