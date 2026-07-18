#!/bin/bash
# No registry required. Maps ID to Blueprint dynamically.
TARGET=$1
ACTION=$2
DATA=$3

# Execute dispatch in virtual context
python3 "$BASE_DIR/blueprint.py" "$TARGET" "$ACTION" "$DATA"
