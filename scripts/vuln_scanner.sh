#!/data/data/com.termux/files/usr/bin/bash
# Scan local services and report findings to the Mesh Ledger
TARGETS=("127.0.0.1:21" "127.0.0.1:22" "127.0.0.1:80")
LOG_FILE="~/sentinel_probe/data/mesh.ledger"

for target in ${TARGETS[@]}; do
    if nc -z -w 2 ${target%%:*} ${target#*:} > /dev/null 2>&1; then
        echo "[!] Vulnerability detected on $target: Open Port" >> $LOG_FILE
    fi
done
