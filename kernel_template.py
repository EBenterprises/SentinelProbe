import sys
# Virtualized Kernel Instance
def run(op, data):
    return f"PROC_ID:{sys.argv[1]} | OP:{op} | DATA:{data}"
if __name__ == "__main__":
    print(run(sys.argv[2], sys.argv[3]))
