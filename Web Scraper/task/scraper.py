import requests
import string
import os
from bs4 import BeautifulSoup


class WebScrapper:
    @staticmethod
    def scrape_url(pages, article_kind):
        for i in range(pages):
            page_number = i + 1
            directory = f"{os.getcwd()}{os.sep}Page_{page_number}"
            if not os.path.exists(directory):
                os.mkdir(directory)
            url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page_number}'
            response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
            if response:
                main_html_parser = HtmlParser(response.content)
                articles = []
                for article in main_html_parser.get_article(article_kind):
                    anchor = article.find('h3', 'c-card__title').find('a')
                    href = f"https://www.nature.com{anchor.get('href')}"
                    sanitized_title = "_".join(anchor.string.translate(str.maketrans('', '', string.punctuation)).split())
                    filename = f"{directory}{os.sep}{sanitized_title}.txt"
                    response = requests.get(href, headers={'Accept-Language': 'en-US,en;q=0.5'})
                    if response:
                        article_html_parser = HtmlParser(response.content)
                        with open(filename, "w", encoding="UTF-8") as article_file:
                            article_file.write(article_html_parser.get_article_body())
                            articles.append(filename)
        print("Saved all articles.")


class HtmlParser:
    def __init__(self, html_content):
        self.parser = BeautifulSoup(html_content, 'html.parser')

    def get_article(self, kind):
        for article in self.parser.find_all('article'):
            span = article.find('span', 'c-meta__type')
            if span and span.string == kind:
                yield article

    def get_article_body(self):
        body = self.parser.find('div', 'c-article-body')
        if body:
            return body.get_text().strip()


WebScrapper.scrape_url(int(input()), input())
