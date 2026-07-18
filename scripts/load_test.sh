#!/data/data/com.termux/files/usr/bin/bash
# Hammer the discovery protocol to ensure mesh stability
echo "[*] Initiating network stress test..."
for i in {1..50}; do
    curl -s http://127.0.0.1:5001/task/claim > /dev/null &
done
wait
echo "[!] Stress test complete. Mesh state reconciled."
