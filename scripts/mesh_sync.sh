#!/data/data/com.termux/files/usr/bin/bash
# Syncs node table across the fabric
NODE_FILE="~/sentinel_probe/data/nodes.list"
# Scans local net and updates node registry
hostname -I | awk '{print $1}' > $NODE_FILE
