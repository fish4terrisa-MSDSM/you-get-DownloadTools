import threading
import tkinter
import tkinter.ttk
from tkinter import filedialog

import Core.you_get as c
import Tool.menu as m
import os
import json
import Tool.constants as v
from tkinter import messagebox

# 获得父目录
pwd = os.getcwd()
fathe_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# 获得用户主目录
home = os.path.expanduser('~')
# 是否通过检查
flag = 1


def save_path_command(*args):
    """
    实现打开目录操作
    :param args:不用填形参
    :return:返回用户打开的路径
    """
    open_save_path = filedialog.askdirectory(title='打开保存路径', initialdir=home)
    print(open_save_path)
    m.save_path_var.set(open_save_path)
    return open_save_path


def open_cookies(*arg):
    """
    上传 cookies 操作
    :param arg:不用填形参
    :return:用户选择的文件路径
    """
    cookies_file = filedialog.askopenfilename(title='打开 cookies 存储路径', initialdir=home)
    print(cookies_file)
    m.cookiespath_var.set(cookies_file)
    return cookies_file


def disabled_startdownload(check: tkinter.IntVar):
    """
    禁止启动下载操作
    :param check: 检查按钮，以便获得状态
    :return: 不返回值
    """
    if check.get() == 1:
        m.downlaod_Button['state'] = 'disabled'
    else:
        m.downlaod_Button['state'] = 'active'


def write(filename, string):
    """
    写入操作函数
    :param filename: 文件路径
    :param string: 写入内容
    :return: 无返回值
    """
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(string)


def load_json():
    """
    加载 json 文件
    :return: 返回转换好的对象
    """
    with open('%s/Date/video_json.json' % fathe_path, 'r', encoding='utf-8') as f:
        video_json = json.load(f)
        print(video_json)
        return video_json


def download_json(url: str):
    """
    下载视频 json 到本地
    :param url: 视频链接
    :return: 无返回值
    """
    video_json = c.get_json(url)
    write("%s/Date/video_json.json" % fathe_path, video_json)


def set_cmd(*args):
    global flag
    """
    准备指令
    :param args: 不需要填形参
    :return: 无返回值
    """

    # 检查视频链接输入框是否有填写
    if m.url_Entry.get() != "" and m.url_Entry.get() != '视频下载链接':
        # 设为常量
        v.URL = m.url_Entry.get()
        # 填入链接
        c.video_url(v.URL)
    else:
        messagebox.showerror(message="请输入视频链接")
        flag = 0

    # 检查输出文件名称输入框是否有填写
    if m.filename_Entry.get() != "" and m.filename_Entry.get() != '输出文件名称':
        # 设为常量
        v.FILENAME = m.filename_Entry.get()
        # 填入文件名
        c.filename(v.FILENAME)
    else:
        pass

    # 检查文件保存路径输入框是否有填写
    if m.filepath_Entry.get() != "" and m.filepath_Entry.get() != '文件保存路径':
        # 设为常量
        v.SAVE_PATH = m.filepath_Entry.get()
        # 填入保存路径
        c.output_dir(v.SAVE_PATH)
    else:
        result = messagebox.askquestion(message="默认以用户目录作为下载位置，是否继续")
        if result == "yes":
            v.SAVE_PATH = home
        else:
            flag = 0

    # 检查cookies保存路径输入框是否有填写
    if m.cookiespath_Entry.get() != "" and m.cookiespath_Entry.get() != 'cookies 路径':
        # 设为常量
        v.COOKIES_PATH = m.cookiespath_Entry.get()
        # 填入cookies位置
        c.cookies_file(v.COOKIES_PATH)
    else:
        result = messagebox.askquestion(message="未填写 cookies 将无法下载会员和高清视频，是否继续")
        print(result)
        if result == "yes":
            pass
        else:
            flag = 0

    # 检查指定播放器输入框是否有填写
    if m.player_Entry.get() != "" and m.player_Entry.get() != '指定播放链接视频的本地播放器':
        # 设为常量
        v.PLAYER_NAME = m.player_Entry.get()
        # 填入指定播放器
        c.player(v.PLAYER_NAME)
    else:
        pass

    # 检查套接字延时输入框是否有填写
    if m.second_Entry.get() != "" and m.second_Entry.get() != '套接字延时':
        # 设为常量
        v.SECONDS = m.second_Entry.get()
        # 填入延迟秒数
        c.seconds(v.SECONDS)
    else:
        pass

    # 检查http_host输入框是否有填写
    if m.httphost_Entry.get() != "" and m.httphost_Entry.get() != 'HOST' and m.httpport_Entry.get() != "" and m.httpport_Entry.get() != 'PORT':
        # 设为常量
        v.HTTP_HOST = m.httphost_Entry.get()
        v.HTTP_PORT = m.httpport_Entry.get()
        # 填入http
        c.http_proxy(v.HTTP_HOST, v.HTTP_PORT)
    else:
        pass

    if m.sockshost_Entry.get() != "" and m.sockshost_Entry.get() != 'HOST' and m.socksport_Entry.get() != "" \
            and m.socksport_Entry.get() != 'PORT' and m.socksusername_Entry.get() != "" \
            and m.socksusername_Entry.get() != 'USERNAME' and m.sockspassword_Entry.get() != "" \
            and m.sockspassword_Entry.get() != 'PASSWORD':
        # 设为常量
        v.SOCKS_HOST = m.sockshost_Entry.get()
        v.SOCKS_PORT = m.socksport_Entry.get()
        v.SOCKS_USERNAME = m.socksusername_Entry.get()
        v.SOCKS_PASSWORD = m.sockspassword_Entry.get()
        # 填入socks
        c.socks5_up(v.SOCKS_HOST, v.SOCKS_PORT, v.SOCKS_USERNAME, v.SOCKS_PASSWORD)

    # 检查socks_host输入框是否有填写
    elif m.sockshost_Entry.get() != "" and m.sockshost_Entry.get() != 'HOST' and m.socksport_Entry.get() != "" and m.socksport_Entry.get() != 'PORT':
        # 设为常量
        v.SOCKS_HOST = m.sockshost_Entry.get()
        v.SOCKS_PORT = m.socksport_Entry.get()
        # 填入socks
        c.socks5_hp(v.SOCKS_HOST, v.SOCKS_PORT)

    else:
        pass

    # 开启自动重命名
    if m.autorename_var.get() == 1:
        c.auto_rename()
    else:
        pass

    # 开启多P下载
    if m.playlist_var.get() == 1:
        c.playlist()
    else:
        pass

    # 开启忽略SSL错误
    if m.skipssl_var.get() == 1:
        c.insecure()
    else:
        pass

    # 开启 m3u8
    if m.m3u8_var.get() == 1:
        c.m3u8()
    else:
        pass

    # 开启调试
    if m.debug_var.get() == 1:
        c.auto_rename()
    else:
        pass

    # 关闭下载字幕
    if m.caption_var.get() == 0:
        c.no_caption()
    else:
        pass

    # 开启校验文件
    if m.check_var.get() == 1:
        c.postfix()
    else:
        pass

    # 关闭合并视频
    if m.merge_var.get() == 1:
        c.no_merge()
    else:
        pass

    # 关闭检查大小
    if m.checksize_var.get() == 0:
        c.skip_existing_file_size_check()
    else:
        pass

    # 获得信息
    if m.getinformation_var.get() == 1:
        v.GET_INFORMATION = c.info(v.URL)
        m.downlaod_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_INFORMATION)
    else:
        m.downlaod_Button['state'] = 'active'

    # 获得解析 url
    if m.geturl_var.get() == 1:
        v.GET_URL = c.get_url(v.URL)
        m.downlaod_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_URL)
    else:
        m.downlaod_Button['state'] = 'active'

    # 获得解析 json
    if m.getjson_var.get() == 1:
        v.GET_JSON = c.get_json(v.URL)
        m.downlaod_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_JSON)
    else:
        m.downlaod_Button['state'] = 'active'

    # 查看版本号
    if m.getversion_var.get() == 1:
        v.GET_VERSION = c.get_json(v.URL)
        m.downlaod_Button['state'] = 'disabled'
        m.output_cmd.insert('insert', v.GET_VERSION)
    else:
        m.downlaod_Button['state'] = 'active'

    # 是否覆盖重名文件
    if m.getjson_var.get() == 1:
        c.force()
    else:
        pass


def makesure_command(*args):
    """
    确认信息
    :return: 无返回值
    """
    global flag

    # 清空列表
    c.cmd_list = ['you-get']
    # 创建确认信息线程
    setcmd = threading.Thread(target=set_cmd())
    # 启动确认信息线程
    setcmd.start()

    if flag == 1:
        # 设置下拉框可用
        m.combobox['state'] = 'readonly'
        # 设置下载按钮可用
        m.downlaod_Button['state'] = 'active'
        # 清除信息
        v.CMD = ''
        # 获得指令内容
        v.CMD = c.get_cmd_information()
        m.cmd_var.set("生成指令")

        # 显示指令
        m.cmd_var.set(v.CMD)

    else:
        flag = 1
        c.cmd_list = ['you-get']
        m.cmd_var.set("生成指令")


def download_command(*args):
    """
    发送下载请求
    :param args:不用填形参
    :return:不返回值
    """

    def start_download(*args):
        """
        启动下载方法
        :param args:不用填形参
        :return: 无返回值
        """
        cmd = c.download_video()
        m.output_cmd.insert('insert', cmd)

    # 下载过程中禁止调用
    m.makesure_Button['state'] = 'disabled'
    m.combobox['state'] = 'disabled'

    m.progressbarOne.start()
    cmd_thread = threading.Thread(target=start_download)
    cmd_thread.start()


def get_firfox_cookie_path(*args):
    """
    从火狐获得cookies路径
    :param args: 不用填写
    :return: 返回cookies路径
    """
    cookiepath_common = os.environ['APPDATA'] + r"\Mozilla\Firefox\Profiles"
    folds_arr = os.listdir(cookiepath_common)
    folds_end = [os.path.splitext(file)[-1][1:] for file in folds_arr]

    if 'default-release' in folds_end:
        cookie_fold_index = folds_end.index('default-release')
    else:
        cookie_fold_index = folds_end.index('default')
    cookie_fold = folds_arr[cookie_fold_index]
    cookie_path = os.path.join(cookiepath_common, cookie_fold)
    v.COOKIES_PATH = os.path.join(cookie_path, 'cookies.sqlite')
    m.cookiespath_var.set(v.COOKIES_PATH)
    return os.path.join(cookie_path, 'cookies.sqlite')


if __name__ == '__main__':
    pass
