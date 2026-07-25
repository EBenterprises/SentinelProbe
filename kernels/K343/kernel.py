import sys, json
def manage_inv(item, status):
    with open("/data/data/com.termux/files/home/sentinel_probe/inventory.db", "a") as f:
        f.write(f"ID:{sys.argv[0].split('/')[-2]} | ITEM:{item} | STATUS:{status}\n")
    return "INV_UPDATE_SUCCESS"

if __name__ == "__main__":
    if len(sys.argv) > 3: print(manage_inv(sys.argv[2], sys.argv[3]))
