#!/bin/bash
# Real-time metrics aggregator
echo "--- Fabric Telemetry Stream ---"
tail -f ~/sentinel_probe/fabric_metrics.log
