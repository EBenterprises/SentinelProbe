import sys
def execute(cmd, data):
    return f"[{K}] PROCESSED: {cmd} | DATA: {data}"
if __name__ == "__main__":
    print(execute(sys.argv[1], sys.argv[2]))
