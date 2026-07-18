import sys, os
class Kernel:
    def __init__(self, id): self.id = id
    def compile_titan(self, code): return f"[{self.id}] COMPILING_TITAN: {code[:10]}..."
    def signal(self, target, msg): 
        with open(f"/data/data/com.termux/files/home/sentinel_probe/bus/{target}.msg", "a") as f:
            f.write(f"FROM_{self.id}:{msg}\n")
    def execute(self, op, val): return f"[{self.id}] {op} | {val}"

k = Kernel("K007")
if __name__ == "__main__":
    if len(sys.argv) > 2: print(k.execute(sys.argv[1], sys.argv[2]))
