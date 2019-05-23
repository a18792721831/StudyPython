import sys
from handlers.IndexHandler import IndexHandler
from handlers.LoginHandler import LoginHandler
from handlers.StaticsHandler import StaticsHandler

url =[
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/statics', StaticsHandler)
]