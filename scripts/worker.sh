#!/data/data/com.termux/files/usr/bin/bash
# Worker daemon consuming queued tasks
while true; do
    TASK=<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    if [[ $TASK != *"no_tasks"* ]]; then
        echo "Processing Task: $TASK"
        # Execute payload logic here
    fi
    sleep 10
done
