# google_parser_demo.py

import requests
from lxml import html
from bs4 import BeautifulSoup


def fetch_html(url: str) -> bytes:
    headers = {
        "User-Agent": "Chrome/5.0 (QA Parser Demo)",
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.content


def parse_with_lxml_xpath(html_content: bytes):
    print("\n========== lxml + XPath ==========")

    tree = html.fromstring(html_content)

    title = tree.xpath("//title/text()")[0]
    print("Title:", title)

    links = tree.xpath("//a/@href")
    for link in links[:10]:  # тільки перші 10
        print("Link:", link)


def parse_with_lxml_findtext(html_content: bytes):
    print("\n========== lxml + findtext ==========")

    tree = html.fromstring(html_content)

    title = tree.findtext(".//title")
    print("Title:", title)

    links = tree.xpath(".//a/@href")
    for link in links[:10]:
        print("Link:", link)


def parse_with_bs4_css(html_content: bytes):
    print("\n========== BeautifulSoup + CSS selectors ==========")

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.select_one("title").text
    print("Title:", title)

    links = soup.select("a")
    for a in links[:10]:
        print("Link:", a.get("href"))



def extract_25_universal_locators(html_content: bytes):
    tree = html.fromstring(html_content)

    elements = tree.xpath("//*")[:25]

    for i, el in enumerate(elements, start=1):
        tag = el.tag

        xpath = f"(//{tag})[{i}]"
        css = f"{tag}:nth-of-type({i})"

        print(f"{i}. CSS: {css}")
        print(f"   XPath: {xpath}\n")


def main():
    url = "https://www.google.com"

    html_content = fetch_html(url)

    # parse_with_lxml_xpath(html_content)
    # parse_with_lxml_findtext(html_content)
    # parse_with_bs4_css(html_content)

    extract_25_universal_locators(html_content)


if __name__ == "__main__":
    main()


xpath = "/html/body/div[1]/main/div[2]/article/section[3]/h2/a"