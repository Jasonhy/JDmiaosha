# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from .random_user_agent import user_agents


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(user_agents)
        request.headers["User-Agent"] = agent
