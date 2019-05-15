# http协议
import tornado.httpserver
# 非阻塞socket循环
import tornado.ioloop
# 命令行解析:日志
import tornado.options
# Web框架与异步，扩展大量连接，长轮训
import tornado.web
from tornado.options import define, options

# 命令行解析工具：监听8000端口的请求
define("port", default=8000, help="run on the given port", type=int)

# 继承RequestHandler
# 请求-处理类
# 习惯：类名首字母大写，请求-处理类以Handler结尾
# 重新方法：rest:get|post|delete|put
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # get_argument(attrName,defaultValue)获取请求的参数（？是否支持rest风格）
        greeting = self.get_argument('greeting', 'Hello')
        # 返回结果写入
        self.write(greeting + ', welcome you to read: www.itdiffer.com')

if __name__ == "__main__":
    # 执行tornado的命令行解析：可执行导入模块的完整性检查
    tornado.options.parse_command_line()
    # 创建mapping集合 key: parten ,value: class
    # r : 是否转义
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # 回调Handler的方法
    http_server = tornado.httpserver.HTTPServer(app)
    # 提供原路径响应:8000，或者说监听某个端口的请求
    http_server.listen(options.port)
    # 启动多进程的http服务
    tornado.ioloop.IOLoop.instance().start()