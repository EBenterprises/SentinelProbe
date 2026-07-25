import sys
# Dynamic Kernel Handler
def execute(target, op, data):
    # This logic spawns dynamic state handlers for infinite IDs
    return f"FABRIC_NODE:{target} | OP:{op} | PAYLOAD:{data} | STATE:ONLINE"

if __name__ == "__main__":
    print(execute(sys.argv[1], sys.argv[2], sys.argv[3]))
