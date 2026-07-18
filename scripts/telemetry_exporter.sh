#!/data/data/com.termux/files/usr/bin/bash
# Stream fabric health data to remote aggregator
while true; do
    METRICS="{\"cpu\": \"u0_a230\", \"status\": \"healthy\"}"
    curl -s -X POST -H "Content-Type: application/json" -d "$METRICS" http://telemetry.internal:9000/ingest
    sleep 30
done
