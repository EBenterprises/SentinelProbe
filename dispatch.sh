#!/bin/bash
# Dispatches to the specific isolated Kernel
KERNEL_PATH="/data/data/com.termux/files/home/sentinel_probe/kernels/$1/kernel.py"
python3 -c "import sys; sys.path.append('$(dirname $KERNEL_PATH)'); from kernel import execute; print(execute('$2', '$3'))"
