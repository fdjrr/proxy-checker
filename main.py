import time
from concurrent.futures import ThreadPoolExecutor

import requests
from loguru import logger

PROXY_LIST_FILE = "proxies.txt"
OUTPUT_FILE = "results.txt"
TEST_URL = "https://httpbin.org/ip"
TIMEOUT = 5


def load_proxies(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def check_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }

    try:
        start_time = time.time()
        response = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)

        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            logger.info(f"[✅] {proxy} - OK - {elapsed_time:.2f} detik")
            return proxy
        else:
            logger.info(f"[❌] {proxy} - Gagal dengan status {response.status_code}")
    except Exception as e:
        logger.error(f"[❌] {proxy} - Error: {e}")

    return None


def main():
    proxies = load_proxies(PROXY_LIST_FILE)
    logger.info(f"[INFO] Checking {len(proxies)} proxies...\n")

    working = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_proxy, proxies)
        working = [proxy for proxy in results if proxy]

    with open(OUTPUT_FILE, "w") as f:
        for proxy in working:
            f.write(proxy + "\n")

    logger.info(f"\n[INFO] {len(working)} proxies saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
