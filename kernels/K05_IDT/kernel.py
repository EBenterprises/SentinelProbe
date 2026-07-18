import sys
class Kernel:
    def __init__(self, name): self.name = name
    def run(self, op, val): return f"[{self.name}] OP: {op} | VAL: {val}"
if __name__ == "__main__":
    k = Kernel("K05_IDT")
    print(k.run(sys.argv[1], sys.argv[2]))
