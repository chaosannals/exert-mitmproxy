from mitmproxy import ctx

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num += 1
        ctx.log.info(f'we seen {self.num} flows')

addons = [
    Counter()
]