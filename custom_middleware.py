import random
import logging

class CustomMiddleware(object):

    proxy_pool = ['49.236.220.238:52840',  '181.112.41.50:33381', '50.235.111.161:45126']

    def process_request(self, request, spider):

        request.meta['proxy'] = “http://“ + random.choice(self.proxy_pool)


    def process_response(self, request, response, spider):

        if response.status in [503]:
            logging.error("%s found for %s so retrying"%(response.status, response.url))
            req = request.copy()
            req.dont_filter = True
            req.meta['proxy'] =  “http://“ + random.choice(self.proxy_pool)
            return req
        else:
            return response