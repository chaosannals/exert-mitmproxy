import typing
from mitmproxy import command, ctx, flow, http

class MyCmd:
    @command.command('mycmd.addheader')
    def addheader(self, flows: typing.Sequence[flow.Flow]) -> None:
        for f in flows:
            if isinstance(f, http.HTTPFlow):
                f.request.headers['mycmd'] = 'hello'
        ctx.log.alert('done')

addons = [MyCmd()]
