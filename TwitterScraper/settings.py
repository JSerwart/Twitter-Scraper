# User agent
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

# settings for spiders
BOT_NAME = 'TwitterScraper'
LOG_LEVEL = 'INFO'
DOWNLOAD_HANDLERS = {'s3': None, }  # from http://stackoverflow.com/a/31233576/2297751, TODO
RETRY_HTTP_CODES = [429]
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'TwitterScraper.middlewares.TooManyRequestsRetryMiddleware': 543,
}

# Time delay between the scraping of two sites
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = False

SPIDER_MODULES = ['TwitterScraper.spiders']
NEWSPIDER_MODULE = 'TwitterScraper.spiders'
ITEM_PIPELINES = {
    'TwitterScraper.pipelines.JsonWriterPipeline': 100,
}

# Settings for where to save data on disk
SAVE_TWEET_PATH = 'C:/Users/danie/Documents/TestScraper/Data/tweet/'
SAVE_USER_PATH = 'C:/Users/danie/Documents/TestScraper/Data/users/'