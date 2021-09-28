# exert-mitmproxy

```bash
# 查看版本信息
mitmproxy --version

# 通过 mitmdump 或 mitmweb 命令启动代码
# 启动代理后，设置系统的代理为 mitmproxy 的连接和地址
# http://mitm.it 这个地址在启动代理可以看到。
# 安装指定的证书，就可以使用。
# 证书要安装成 受信任的根证书颁发机构
# https 锁标志可以看到证书的颁发者是 mitmproxy 就说明安装成功。
```

## mitmproxy

```bash
# 添加命令扩展脚本
mitmproxy -s ./mycmd.py

# 这个界面类似 vim 和 metasploit 之列
# 通过 冒号 输入命令
# 按住 tab 可以切换查看命令

# 列表模式下命令
# 回车 选中信息
# q 退出程序

# 信息页模式
# q 退出，回到列表
# p 跳上一个信息

# 调用自定义命令
# 指定选中
:mycmd.addheader @focus
# 指定全部
:mycmd.addheader @all
# 指定域名
:mycmd.addheader ~baidu.com
```

## mitmdump

```bash
# -w 指定数据输出
mitmdump -w "D:\mitmdump.data"

# -s 指定脚本
mitmdump -s ./app.py
```

## mitmweb

```bash
# 打开 web 界面
mitmweb

# -s 指定脚本
mitmweb -s ./app.py
```
