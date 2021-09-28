from mitmproxy import ctx

class App:
    def __init__(self):
        '''
        具体事件，查阅官网文档。
        https://docs.mitmproxy.org/stable/api/events.html
        '''

    def load(self, loader):
        '''
        [生命周期事件]
        插件第一次被加载执行
        '''
        ctx.log.info('on load')

    def running(self):
        '''
        [生命周期事件]
        '''
        ctx.log.info('on running')

    def configure(self, updated):
        '''
        [生命周期事件]
        '''
        ctx.log.info('on configure')

    def done(self):
        '''
        [生命周期事件]
        '''
        ctx.log.info('on done')

    def client_connected(self, client):
        '''
        [连接事件]
        客户端连接完成
        '''
        ctx.log.info('on client_connected')

    def client_disconnected(self, client):
        '''
        [连接事件]
        客户端断开连接
        '''
        ctx.log.info('on client_disconnected')

    def server_connect(self, data):
        '''
        [连接事件]
        服务器连接
        '''
        ctx.log.info('on server_connect')

    def server_connected(self, data):
        '''
        [连接事件]
        服务器连接完成
        '''
        ctx.log.info('on server_connected')

    def server_disconnected(self, data):
        '''
        [连接事件]
        服务器断开连接
        '''

        ctx.log.info('on server_disconnected')

    
    def request(self, flow):
        ctx.log.info(f'on request {flow.response}')

addons = [App()]