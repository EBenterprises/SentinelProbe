import uuid
import time
from ledger import write_record, read_ledger

def push_task(task_name, payload):
    task_id = str(uuid.uuid4())
    task_entry = {
        "id": task_id,
        "task": task_name,
        "payload": payload,
        "status": "pending",
        "timestamp": time.time()
    }
    write_record(task_id, task_entry)
    return task_id

def claim_tasks():
    ledger = read_ledger()
    for t_id, entry in ledger.items():
        if entry.get("status") == "pending":
            entry["status"] = "processing"
            write_record(t_id, entry)
            return entry
    return None
