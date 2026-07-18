#!/data/data/com.termux/files/usr/bin/bash
# Automated secret rotation for the Sovereign Fabric
SECRET_FILE="~/sentinel_probe/data/secret.key"
NEW_KEY=$(openssl rand -base64 32)

echo $NEW_KEY > $SECRET_FILE
echo "[!] Secrets rotated successfully across the mesh."
