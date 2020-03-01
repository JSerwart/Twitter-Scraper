# Twitter Scraper
## Introduction
Scraper based on the code of [jonbakerfish](https://github.com/jonbakerfish/TweetScraper).
The main modifications to his code are:
* scrape also emoticons in text of tweets
* avoid being blocked by Twitter's rate limits
* save all results into a single json-file

## Set-up
The code was written with Python 3.6 and `scrapy=1.8.0`. In order to install the required modules, 
navigate to the root of this project and run `pip install -r requirements.txt`.

## Usage
In order to scrape for a specific keyword, navigate to `./TwitterScraper` and run
```
scrapy crawl TwitterCrawler -a query="foo" -a lang="en" -a file_name="foo_tweets"
```
where `query` defines for what to search, `lang` defines the language of the tweets (default ' '), and 
`file_name` is the name of the json-file where the tweets are saved. Additional (optional) parameters are
`crawl_user` which defines whether also the information regarding the users should be saved, and 
`top_tweet` which defines whether only the top tweets should be scraped. The `query` value can follow Twitter's
advanced search operators (see table below).

| Operator | Finds tweets... |
| --- | --- |
| twitter search | containing both "twitter" and "search". This is the default operator. |
| **"** happy hour **"** | containing the exact phrase "happy hour". |
| love **OR** hate | containing either "love" or "hate" (or both). |
| beer **-** root | containing "beer" but not "root". |
| **#** haiku | containing the hashtag "haiku". |
| **from:** alexiskold | sent from person "alexiskold". |
| **to:** techcrunch | sent to person "techcrunch". |
| **@** mashable | referencing person "mashable". |
| "happy hour" **near:** "san francisco" | containing the exact phrase "happy hour" and sent near "san francisco". |
| **near:** NYC **within:** 15mi | sent within 15 miles of "NYC". |
| superhero **since:** 2010-12-27 | containing "superhero" and sent since date "2010-12-27" (year-month-day). |
| ftw **until:** 2010-12-27 | containing "ftw" and sent up to date "2010-12-27". |
| movie -scary **:)** | containing "movie", but not "scary", and with a positive attitude. |
| flight **:(** | containing "flight" and with a negative attitude. |
| traffic **?** | containing "traffic" and asking a question. |
| hilarious **filter:links** | containing "hilarious" and linking to URLs. |
| news **source:twitterfeed** | containing "news" and entered via TwitterFeed |

## Twitter scraping limitations
According to it's [robots.txt](https://twitter.com/robots.txt), Twitter requires a delay of 1 second
between page requests. In order to achieve this, in `settings.py` set `DOWNLOAD_DELAY=1` and 
`RANDOMIZE_DOWNLOAD_DELAY = False`. This ensures that the delay required by Twitter is respected and avoids
being banned.
 