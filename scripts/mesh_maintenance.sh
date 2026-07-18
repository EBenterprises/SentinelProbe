#!/data/data/com.termux/files/usr/bin/bash
# Periodic mesh purge
while true; do
    curl -X POST http://127.0.0.1:5001/purge
    sleep 60
done
