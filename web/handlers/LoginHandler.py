import tornado


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        print('get')

    def post(self):
        print('post')

    def put(self):
        print('put')

    def delete(self):
        print('delete')
