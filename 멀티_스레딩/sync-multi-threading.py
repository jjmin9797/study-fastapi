import requests
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session, url = params
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    excutor = ThreadPoolExecutor(max_workers=1)

    with requests.Session() as session:
        # responses = [fetcher(session, url) for url in urls]
        params = [(session, url) for url in urls]
        result = list(excutor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    main()
