#!/data/data/com.termux/files/usr/bin/bash
# Emergency Kill Switch: Wipes all sensitive fabric keys
echo "[!!!] EMERGENCY BREACH DETECTED: PURGING KEYS..."
rm -f ~/sentinel_probe/security/certs/*.key
rm -rf ~/sentinel_probe/security/nodes/*/*.key
rm -f ~/sentinel_probe/data/secret.key
pkill -f python
echo "[!!!] Fabric keys purged and services terminated."
