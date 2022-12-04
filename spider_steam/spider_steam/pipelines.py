# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from datetime import datetime

from dateutil.parser import parse
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class SpiderSteamPipeline:
    def open_spider(self, spider):
        self.file = open("items.json", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item).asdict()
        line = json.dumps(adapter) + "\n"
        if adapter.get('release_date').year > 2020:
            self.file.write(line)
        else:
            raise DropItem(f"Too old game")
        return item
