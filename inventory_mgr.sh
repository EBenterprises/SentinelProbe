#!/bin/bash
# Global Asset Tracker
KERNEL=\$1
ITEM=\$2
STATUS=\$3
python3 "$ROOT/\$KERNEL/kernel.py" "INV" "\$ITEM" "\$STATUS"
