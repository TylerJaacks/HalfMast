import datetime

import requests

from bs4 import BeautifulSoup
from lxml import etree


class HalfStaffScrapper:
    def __init__(self):
        self.url = "https://www.halfstaff.org/"
        self.soup = None
        self.dom = None

    def get_soup(self):
        r = requests.get(self.url, verify=False)
        self.soup = BeautifulSoup(r.text, 'html.parser')
        self.dom = etree.HTML(str(self.soup))

    def get_date(self):
        year = datetime.datetime.year
        month = self.dom.xpath('//*[@id="month"]/text()')
        day = self.dom.xpath('//*[@id="day"]/text()')

        return year, month, day

    def get_post_title(self):
        post_title = self.dom.xpath('//*[@id="posttitle"]/div[2]/span[1]/a/text()')

        return post_title

    def get_post_content(self):
        post_content = self.dom.xpath('//*[@id="postcontent"]//text()')

        return post_content
