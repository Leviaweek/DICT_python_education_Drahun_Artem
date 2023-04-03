"""Web page parser module"""
import os
import re
import requests
from bs4 import BeautifulSoup

class WebParser:
    """Web page parser"""
    def __init__(self, url: str, pages_numer: int, pages_type: str):
        self.url = url
        self.pages_number = pages_numer
        self.pages_type = pages_type

    @staticmethod
    def __get_page(url: str) -> str:
        """Get page from url

        Args:
            url (str): string with url

        Raises:
            ValueError: if status code is not 200

        Returns:
            str: page content
        """
        page = requests.get(url, timeout=10)
        if page.status_code != 200:
            raise ValueError("Invalid URL")
        return page.text

    def __save_pages(self, content: dict, page_number: int) -> None:
        """Save pages to files

        Args:
            content (dict): titles and links
            page_number (int): page number for path name
        """
        for _, links in content.items():
            if not os.path.exists(f'PAGE_{page_number}'):
                os.mkdir(f'PAGE_{page_number}')
            for link in links:
                page = self.__get_page(link)
                soup = BeautifulSoup(page, "html.parser")
                parsed_text = soup.get_text()
                name = soup.find('title').text
                text = re.sub(r"\n+", "\n", parsed_text)
                file_path = os.path.join(os.getcwd(), f'PAGE_{page_number}', f"{name}.txt")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)

    def parse(self) -> None:
        """Parse pages"""
        for i in range(1, self.pages_number + 1):
            page = self.__get_page(self.url)
            soup = BeautifulSoup(page, "html.parser")
            content = {}
            for elem in soup.find_all(class_='u-full-height c-card c-card--flush'):
                link = f"https://www.nature.com{elem.find('a')['href']}"
                title = elem.find(class_='c-meta__type').text
                if title.startswith(self.pages_type):
                    if title not in content:
                        content[title] = []
                    content[title].append(link)
                    print(f'Title: {title}')
                    print(f'Link: {link}')
            self.__save_pages(content, i)
            new_url = soup.find(attrs={'data-test':'page-next'}).find('a')['href']
            self.url = f"https://www.nature.com{new_url}"
            print(content)
