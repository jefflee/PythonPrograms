import requests
import time

def do_requests():
    resp = requests.get('https://example.com')
    print('example.com =>', resp.status_code)


def main():
    start = time.time()
    for _ in range(0, 10):
        do_requests()

    print(f"time: {time.time() - start} (s)")


if __name__ == '__main__':
    main()