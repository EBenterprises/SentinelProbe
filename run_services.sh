#!/bin/bash
# SentinelProbe Service Manager

echo "Starting Sentinel Services..."

# Launch Orchestrator
nohup python ~/sentinel_probe/core/orchestrator.py > ~/sentinel_probe/orchestrator.log 2>&1 &
ORCH_PID=$!

# Launch Scheduler
nohup python ~/sentinel_probe/core/scheduler.py > ~/sentinel_probe/scheduler.log 2>&1 &
SCHED_PID=$!

echo "Orchestrator [PID: $ORCH_PID] and Scheduler [PID: $SCHED_PID] started."
