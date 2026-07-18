#!/bin/bash
# Package environment for production export
cd ~/sentinel_probe
tar -czvf sovereign_fabric_v1.tar.gz core/ scripts/ security/ manage.sh
echo "[!] Deployment package created at ~/sentinel_probe/sovereign_fabric_v1.tar.gz"
