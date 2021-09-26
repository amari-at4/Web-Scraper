import requests
from bs4 import BeautifulSoup


class WebScrapper:
    @staticmethod
    def check_url_quote(url):
        print()
        try:
            if "https://www.imdb.com/title/" not in url:
                raise RuntimeError("Invalid movie page!")
            response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
            if response:
                movie = dict()
                html_parser = HtmlParser(response.content)
                movie['title'] = html_parser.get_title()
                movie['description'] = html_parser.get_description()
                print(movie)
            else:
                print("Invalid movie page!")
        except RuntimeError as e:
            print(str(e))


class HtmlParser:
    def __init__(self, html_content):
        self.parser = BeautifulSoup(html_content, 'html.parser')

    def get_title(self):
        title = self.parser.find('title')
        if title is None or not title.text.endswith(' - IMDb'):
            raise RuntimeError("Invalid movie page!")
        return title.text.replace(' - IMDb', '', 1)

    def get_description(self):
        description = self.parser.find('meta', {'name': 'description'})
        if description is None:
            raise RuntimeError("Invalid movie page!")
        return description.get('content')


print("Input the URL:")
WebScrapper.check_url_quote(input())
