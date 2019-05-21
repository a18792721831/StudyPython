import tornado


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../statics/html/index.html')

    def post(self):
        self.get()

    def put(self):
        self.get()

    def delete(self):
        self.get()
