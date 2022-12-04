import datetime
import re

import scrapy
from dateutil.parser import parse
from spider_steam.items import SpiderSteamItem


class SteamgamespiderSpider(scrapy.Spider):
    name = 'SteamGameSpider'
    allowed_domains = ['store.steampowered.com']
    start_urls = [
        'https://store.steampowered.com/search/?term=vr&page=1&category1=998',
        'https://store.steampowered.com/search/?term=vr&page=2&category1=998',
        'https://store.steampowered.com/search/?term=interesting&page=1&category1=998',
        'https://store.steampowered.com/search/?term=interesting&page=2&category1=998',
        'https://store.steampowered.com/search/?term=shooters&page=1&category1=998',
        'https://store.steampowered.com/search/?term=shooters&page=2&category1=998',
        'https://store.steampowered.com/search/?term=america&page=1&category1=998',
        'https://store.steampowered.com/search/?term=america&page=2&category1=998'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_games_response)

    def parse_games_response(self, response):
        game_urls = response.xpath('//*[@id="search_resultsRows"]/a/@href').getall()

        for game_url in game_urls:
            yield scrapy.Request(
                url=game_url,
                callback=self.parse_game_page,
                cookies={
                    "birthtime": '849387601',
                    "lastagecheckage": "1 - 0 - 1997"
                }
            )

    def parse_game_page(self, response):
        items = SpiderSteamItem()
        name = response.xpath('//*[@id="appHubAppName"]/text()').extract()

        categories = response.xpath(
            '//*[@id="tabletGrid"]/div[1]/div[2]/div[1]/div[1]/a/text()| \
             //*[@id="tabletGrid"]/div[1]/div[2]/div[1]/div[1]/a/span/text()').extract()

        reviews_number = response.xpath('//*[@id="userReviews"]/div[2]/div[2]/span[2]/text()').extract()
        if len(reviews_number):
            reviews_number = int(re.sub(r'(\d+),(\d+)', r'\g<1>\g<2>', reviews_number[0].strip()[1:-1]))

        overall_score = response.xpath('//*[@id="userReviews"]/div[2]/div[2]/span[1]/text()').extract()
        if len(overall_score):
            overall_score = overall_score[0].strip()

        release_date = response.xpath(
            '//*[contains(@class, "release_date")]/*[contains(@class, "date")]/text()').extract()
        if len(release_date):
            release_date = release_date[0].strip()
            if 'oming' not in release_date and 'nnounce' not in release_date:
                try:
                    release_date = parse(release_date)
                except:
                    try:
                        release_date = re.search(r'\d{4}', release_date)[0]
                    except:
                        release_date = 0

        developer = response.xpath('//*[@id="developers_list"]/a/text()').extract()
        if len(developer):
            developer = developer[0].strip()

        tags = response.xpath('//*[@id="glanceCtnResponsiveRight"]/div[2]/div[2]/a/text()').extract()
        for i in range(len(tags)):
            tags[i] = tags[i].strip()

        price = response.xpath(
            '//*[contains(@class, "game_purchase_action")]//*[contains(@class, "discount_final_price")]/text()'
        ).extract()
        if len(price) == 0:
            price = response.xpath(
                '//*[contains(@class, "game_area_purchase_game") and not(contains(@class, "demo_above_purchase"))]//*[contains(@class, "game_purchase_price price")]/text()'
            ).extract()
        if len(price) != 0:
            if re.search(r"([\d,]+)", price[0]):
                price = float('.'.join(re.search(r"([\d,]+)", price[0])[0].split(',')))
            elif re.search(r"Free", price[0])[0]:
                price = 0
            else:
                price = None

        available_platforms = response.xpath(
            '//*[contains(@class, "sysreq_tabs")]/*[contains(@class, "sysreq_tab")]/text()').extract()
        for i in range(len(available_platforms)):
            available_platforms[i] = available_platforms[i].strip()
        if len(available_platforms) == 0:
            requirements = response.xpath(
                '//*[contains(@class, "sysreq_contents")]//*[contains(@class, "bb_ul")]/li/text()').extract()
            for i in range(len(requirements)):
                if re.search(r'[Ww][Ii][Nn][Dd][Oo][Ww][Ss]', requirements[i]):
                    available_platforms.append('Windows')
                    break
                elif re.search(r'[Ll][Ii][Nn][Uu][Xx]', requirements[i]):
                    available_platforms.append('Linux')
                    break
                elif re.search(r'[Mm][Aa][Cc]', requirements[i]):
                    available_platforms.append('maxOS')
                    break

        if len(name):
            items['name'] = name[0]

        if len(categories):
            items['categories'] = categories

        if reviews_number:
            items['reviews_number'] = reviews_number

        if overall_score:
            items['overall_score'] = overall_score

        if release_date:
            items['release_date'] = release_date

        if developer:
            items['developer'] = developer

        if tags:
            items['tags'] = tags

        if price:
            items['price'] = price

        if available_platforms:
            items['available_platforms'] = available_platforms

        if type(release_date) == datetime.datetime:
            if release_date.year > 2000:
                yield items
        else:
            yield items
