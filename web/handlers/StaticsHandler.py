import tornado


class StaticsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../statics/' + self.get_argument('path'))

    def post(self):
        self.get()

    def put(self):
        self.get()

    def delete(self):
        self.get()