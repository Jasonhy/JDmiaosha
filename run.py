# -*- coding: utf-8 -*-
from scrapy import cmdline
from JDmiaosha.register import UserInfo
from JDmiaosha.db_helper import DBHelp


db = DBHelp("miaosha")

def clear_db():
    """
    情况数据
    :return:
    """
    db.remove()

def cmd():
    cmdline.execute("scrapy crawl JD".split())

def save_user():
    user = UserInfo()
    user.save_info("./user.txt")

if __name__ == '__main__':
    # save_user()
    # cmd()
    clear_db()