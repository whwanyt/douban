# -*- coding: utf-8 -*-

import random
import base64

from settings import USER_AGENTS
from settings import PROXIES

class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent",useragent)

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_password'] is None:
            request.meta['proxy'] = "http://"+proxy['ip_port']
        else:
            base_userpawd = base64.b64encode(proxy['user_password'])
            request.meta['proxy'] = "http://"+proxy['ip_port']
            request.headers['Proxy-Authorization'] = 'Basic' +base_userpawd