import tornado.web
import os
from url import url

setting = dict(
)

application = tornado.web.Application(
    handlers=url,
    **setting
)

tornado.web.Application(handlers=None,default_host='',transforms=None,**setting)