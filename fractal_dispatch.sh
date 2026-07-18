#!/bin/bash
# Usage: ./fractal_dispatch.sh [Branch/Leaf] [Action] [Payload]
python3 "$BASE_DIR/fractal_engine.py" "$1" "$2" "$3"
