# -*- coding: utf-8 -*-
import json
from .db_helper import DBHelp


class UserInfo:
    db = DBHelp("user")

    def save_info(self,file_path):
        with open(file_path,"r",encoding="utf-8") as file:
            user = file.read()
            user = json.loads(user,encoding="utf-8")
            self.db.insert_one(user)