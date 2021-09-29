import requests


class WebScrapper:
    @staticmethod
    def save_content_to_file(url):
        print()
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if response:
            with open('source.html', 'wb') as source_file:
                source_file.write(response.content)
                print('Content saved.')
        else:
            print(f"The URL returned {response.status_code}")


print("Input the URL:")
WebScrapper.save_content_to_file(input())
