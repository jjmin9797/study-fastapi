import requests


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    with requests.Session() as session:
        responses = [fetcher(session, url) for url in urls]

        return responses


if __name__ == "__main__":
    print(main())
