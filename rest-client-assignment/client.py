import requests
import json

BASE = "http://127.0.0.1:5000"

def pretty(resp):
    try:
        return json.dumps(resp.json(), indent=2, ensure_ascii=False)
    except:
        return resp.text

def main():
    print("== Health check ==")
    r = requests.get(f"{BASE}/health")
    print(r.status_code, pretty(r))

    print("\n== List users ==")
    r = requests.get(f"{BASE}/users")
    print(r.status_code, pretty(r))

    print("\n== Get user id=2 ==")
    r = requests.get(f"{BASE}/users/2")
    print(r.status_code, pretty(r))

    print("\n== List products ==")
    r = requests.get(f"{BASE}/products")
    print(r.status_code, pretty(r))

    print("\n== Create order (user_id=1, product_ids=[1,3]) ==")
    payload = {"user_id": 1, "product_ids": [1, 3]}
    r = requests.post(f"{BASE}/orders", json=payload)
    print(r.status_code, pretty(r))

    print("\n== List orders ==")
    r = requests.get(f"{BASE}/orders")
    print(r.status_code, pretty(r))

if __name__ == '__main__':
    main()
