#!/data/data/com.termux/files/usr/bin/bash
# Cryptographic integrity auditor
BASE_DIR="~/sentinel_probe"
BASELINE="~/sentinel_probe/data/integrity.base"

if [ ! -f $BASELINE ]; then
    find $BASE_DIR -type f -exec sha256sum {} + > $BASELINE
    echo "[*] Integrity baseline established."
else
    sha256sum -c $BASELINE --quiet > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "[!] TAMPERING DETECTED: Triggering Lockout Protocol."
        ~/sentinel_probe/scripts/kill_switch.sh
    fi
fi
