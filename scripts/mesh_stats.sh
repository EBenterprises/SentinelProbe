#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Mesh Ledger Size: $(wc -l < ~/sentinel_probe/data/mesh.ledger) lines"
echo "[*] Pending Tasks: $(grep -c "pending" ~/sentinel_probe/data/mesh.ledger)"
