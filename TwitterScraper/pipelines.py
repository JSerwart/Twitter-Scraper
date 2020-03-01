# -*- coding: utf-8 -*-
# from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
import logging
import json

from TwitterScraper.utils import mkdirs
from TwitterScraper.items import Tweet, User


logger = logging.getLogger(__name__)
settings = get_project_settings()


class JsonWriterPipeline(object):
    """
    Class that handles the returned items: Tweet-Items are save in a json file.
    The so created json file can easly be converted in a pandas DataFrame and
    exported as csv. Note: when exporting the data as a csv, we need to seprate
    the columns by tabs and use the utf-8-sig encoding.
    """

    def __init__(self):
        # Get path to folder where tweets are saved:
        self.savePath_tweets = settings['SAVE_TWEET_PATH']
        # Get path to folder where users are saved:
        self.savePath_users = settings['SAVE_USER_PATH']
        # Ensure the path exists
        mkdirs(self.savePath_tweets)
        mkdirs(self.savePath_users)
        # Initialize files:
        self.file_tweets = None
        self.file_users = None

    def open_spider(self, spider):
        # Open/create Json file:
        self.file_tweets = open(self.savePath_tweets + spider.file_name + '.jl', 'w')
        self.file_users = open(self.savePath_users + spider.file_name + '.jl', 'w')

    def close_spider(self, spider):
        # Close Json files:
        self.file_tweets.close()
        self.file_users.close()

    def process_item(self, item, spider):
        # Insert new entry in Json file: Tweet-items are converted to dictonaries
        # Each entry is separated by a line break
        if isinstance(item, Tweet):
            line = json.dumps(dict(item)) + "\n"
            self.file_tweets.write(line)
        elif isinstance(item, User):
            line = json.dumps(dict(item)) + "\n"
            self.file_users.write(line)

        return item
