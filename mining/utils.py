# !/usr/bin/env python 3
# encoding: utf-8
# utils.py create by zander on 2017/8/16 14:03
import uuid
import _md5
import os


def handle_file_upload(file):
    """
    保存上传文件到服务器
    :param file: 上传文件
    :return: f_name
    """
    base_dir = os.path.dirname(os.path.abspath(__name__))
    pic_dir = os.path.join(base_dir, "static", "upload")
    uid = "".join(str(uuid.uuid4()).split("-")[:2])

    f_name = ".".join([uid,file.name.split(".")[1]])
    f_path = os.path.join(pic_dir, f_name)
    with open(f_path, "wb+") as pic:
        for chunk in file.chunks():
            pic.write(chunk)
    return f_name
