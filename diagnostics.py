import requests

def check_fabric():
    try:
        response = requests.get('http://127.0.0.1:5001/status')
        print(f"Fabric Status: {response.json()}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    check_fabric()
