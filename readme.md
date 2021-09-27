# exert-mitmproxy

```bash
# 查看版本信息
mitmproxy --version

# 打开 web 界面
mitmweb
# 启动代理后，设置系统的代理为 mitmweb 的连接和地址
# http://mitm.it 这个地址在启动代理可以看到。
# 安装指定的证书，就可以使用。
# 证书要安装成 受信任的根证书颁发机构
# https 锁标志可以看到证书的颁发者是 mitmproxy 就说明安装成功。
```
