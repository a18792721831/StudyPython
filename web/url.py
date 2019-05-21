import sys
from handlers.IndexHandler import IndexHandler
from handlers.LoginHandler import LoginHandler

url =[
    (r'/', IndexHandler),
    (r'/login', LoginHandler)
]