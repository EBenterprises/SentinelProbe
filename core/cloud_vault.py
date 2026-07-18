import subprocess
import os

def backup_ledger():
    # Compress, encrypt with GPG, and push to remote
    ledger = os.path.expanduser("~/sentinel_probe/data/mesh.ledger")
    subprocess.run(["tar", "-czf", "vault.tar.gz", ledger])
    subprocess.run(["gpg", "-c", "--batch", "--passphrase", "SECRET_PASS", "vault.tar.gz"])
    # Trigger remote push (placeholder for SCP/S3)
    print("[*] Ledger vault encrypted and staged.")
