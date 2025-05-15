import requests
from concurrent.futures import ThreadPoolExecutor

PROXY_LIST_FILE = 'proxies.txt'
OUTPUT_FILE = 'results.txt'
TEST_URL = 'https://httpbin.org/ip'
TIMEOUT = 5

def load_proxies(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }
    try:
        response = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f'[✅] {proxy}')
            return proxy
    except:
        pass
    print(f'[❌] {proxy}')
    return None

def main():
    proxies = load_proxies(PROXY_LIST_FILE)
    print(f'[INFO] Checking {len(proxies)} proxies...\n')

    working = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_proxy, proxies)
        working = [proxy for proxy in results if proxy]

    with open(OUTPUT_FILE, 'w') as f:
        for proxy in working:
            f.write(proxy + '\n')

    print(f'\n[INFO] {len(working)} proxies saved to {OUTPUT_FILE}')

if __name__ == '__main__':
    main()
