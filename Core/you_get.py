import subprocess
import tkinter.messagebox

import Tool.menu as m

# 指令列表
cmd_list = ['you-get']


def video_url(url):
    """
    填写网址
    :param url: 视频网址
    :return: 不返回值
    """
    cmd_list.append(url)


def run_cmd(cmd: list):
    """
    运行指令 demo
    :param cmd: 指令列表
    :return: stdout
    """
    # 运行指令
    cmd = subprocess.run(
        cmd,
        capture_output=True)

    # 返回信息
    if cmd.stdout.decode("utf-8") != "":
        return cmd.stdout.decode("utf-8")
    elif cmd.stderr.decode("utf-8") != "":
        return cmd.stderr.decode("utf-8")


def download_video(*args):
    """
    启动下载
    :param args:不用填形参
    :return: 返回执行结果
    """
    run_cmd(cmd_list)
    # 停止进度条
    m.progressbarOne.stop()
    # 显示对话框
    tkinter.messagebox.showinfo(title="下载完成", message='下载完成')
    # 解除禁用控件
    m.makesure_Button['state'] = 'active'
    m.combobox['state'] = 'readonly'


def info(url):
    """
    获得视频清晰度等信息
    :param url: 视频网址
    :return: 返回信息
    """
    # print(run_cmd(['you-get', '-i', url]))
    return run_cmd(['you-get', '-i', url])


def get_url(url):
    """
    获得解析出的url
    :param url: 视频网址
    :return: 返回信息
    """
    print(run_cmd(['you-get', '-u', url]))


def get_version(*args):
    """
    获得版本号
    :return: 返回版本号
    """
    return run_cmd(['you-get', '-V'])


def get_help(*args):
    """
    获得帮助
    :return: 返回帮助
    """
    return run_cmd(['you-get', '-h'])


def get_json(url: str):
    """
    获得json
    :param 网页链接
    :return: 返回json
    """
    return run_cmd(['you-get', url, '--json'])


def no_merge(*args):
    """
    不将分段下载的视频合并
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append("--no-merge")
    return None


def no_caption(*args):
    """
    不下载字幕，歌词等
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--no-caption')
    return None


def postfix(*args):
    """
    使用唯一标识符修复文件
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--postfix')
    return None


def force(*args):
    """
    强制覆盖重名文件
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--force')
    return None


def skip_existing_file_size_check(*args):
    """
    跳过大小检查
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--skip-existing-file-size-check')
    return None


def stream_id(stream: str):
    """
    指定视频清晰度
    :param stream:清晰度代码
    :return: 无返回值
    """
    cmd_list.append('--format')
    cmd_list.append(stream)
    return None


def filename(name: str):
    """
    指定视频下载名称
    :param name:文件名称
    :return: 无返回值
    """
    cmd_list.append('--output-filename')
    cmd_list.append(name)
    return None


def output_dir(path: str):
    """
    指定视频清晰度
    :param path:输出路径
    :return: 无返回值
    """
    cmd_list.append('--output-dir')
    cmd_list.append(path)
    return None


def player(player_name: str):
    """
    指定视频清晰度
    :param player_name:播放器名称
    :return: 无返回值
    """
    cmd_list.append('--player')
    cmd_list.append(player_name)
    return None


def cookies_file(path: str):
    """
    上传 cookies 以便于下载更高清晰度的视频
    :param path:cookies存放路径
    :return: 无返回值
    """
    cmd_list.append('--cookies')
    cmd_list.append(path)
    return None


def seconds(second: str):
    """
    指定延时时长
    :param second:秒数
    :return: 无返回值
    """
    cmd_list.append('--timeout')
    cmd_list.append(second)
    return None


def debug(*args):
    """
    指定视频清晰度
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--debug')
    return None


def playlist(*args):
    """
    下载多P视频列表
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--playlist')
    return None


def auto_rename(*args):
    """
    重复文件名自动重命名
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--auto-rename')
    return None


def insecure(*args):
    """
    忽略不安全的 SSL 链接错误
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--insecure')
    return None


def m3u8(*args):
    """
    使用 m3u8 链接下载 m3u8 视频
    :param args:不用填形参
    :return: 无返回值
    """
    cmd_list.append('--m3u8')
    return None


def http_proxy(host: str, port: str):
    """
    对下载使用 http 代理
    :param host:主机名
    :param port: 端口
    :return: 无返回值
    """
    cmd_list.append("--socks-proxy")
    cmd_list.append("%s:%s" % (host, port))
    return None


def extractor_proxy(host: str, port: str):
    """
    只使用一个 http 代理提取
    :param host:主机名
    :param port: 端口
    :return: 无返回值
    """
    cmd_list.append("--extractor-proxy")
    cmd_list.append("%s:%s" % (host, port))
    return None


def socks5_hp(host: str, port: str):
    """
    使用 socks5 代理并使用 HOST:PORT 模式下载
    :param host:主机名
    :param port: 端口
    :return: 无返回值
    """
    cmd_list.append("--socks-proxy")
    cmd_list.append("%s:%s" % (host, port))
    return None


def socks5_up(username: str, password: str, host: str, port: str):
    """
    使用 socks5 代理并使用 USERNAME:PASSWORD@HOST:PORT 模式下载
    :param username: 用户名
    :param password: 密码
    :param host:主机名
    :param port: 端口
    :return: 无返回值
    """
    cmd_list.append("--socks-proxy")
    cmd_list.append("%s:%s@%s:%s" % (username, password, host, port))
    return None


def get_cmd_information():
    cmd_string = ""
    for i in cmd_list:
        cmd_string += " " + i
    return cmd_string


if __name__ == '__main__':
    # print(info("https://www.bilibili.com/video/BV1gg411s728/?spm_id_from=333.1007.tianma.1-2-2.click"))
    # filename("test")
    # get_cmd_information()
    pass
