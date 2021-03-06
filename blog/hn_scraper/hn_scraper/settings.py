# -*- coding: utf-8 -*-

# Scrapy settings for hn_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hn_scraper'

SPIDER_MODULES = ['hn_scraper.spiders']
NEWSPIDER_MODULE = 'hn_scraper.spiders'

#--------------------------------------------------------------------------
# Frontier Settings
#--------------------------------------------------------------------------
SPIDER_MIDDLEWARES = {}
DOWNLOADER_MIDDLEWARES = {}
SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 999
}, )
DOWNLOADER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware':
    999
})
SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'
FRONTERA_SETTINGS = 'hn_scraper.frontera_settings'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hn_scraper (+http://www.yourdomain.com)'
