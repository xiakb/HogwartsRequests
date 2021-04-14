from typing import List
from api.base_api import BaseApi


class Contacts(BaseApi):
    """通讯录"""

    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        """
        创建成员
        :param userid: 成员userid
        :param name: 成员名称
        :param mobile: 成员电话
        :param department: 成员所属部门id
        :param kwargs: 成员的其他信息
        :return: 对应状态信息
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        method = 'post'
        data = {
            'userid': userid,
            'name': name,
            'mobile': mobile,
            'department': department
        }
        data.update(kwargs)
        # r = self.s.post(url=url, json=data)
        r = self.request(method=method, url=url, json=data)
        return r.json()

    def find_member(self, userid: str):
        """
        读取成员信息
        :param userid: 指定成员的userid
        :return: 成员的信息
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        method = 'get'
        params = {'userid': userid}
        # r = self.s.get(url=url, params=params)
        r = self.request(method=method, url=url, params=params)
        return r.json()

    def update_member(self, userid: str, **kwargs):
        """
        更新成员信息
        :param userid: 对应成员的userid
        :param kwargs: 成员的其他信息
        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        method = 'post'
        data = {
            'userid': userid
        }
        data.update(kwargs)
        # r = self.s.post(url=url, json=data)
        r = self.request(method=method, url=url, json=data)
        return r.json()

    def delete_member(self, userid: str):
        """
        删除指定的成员
        :param userid: 指定成员的userid
        :return: 对应状态信息
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        method = 'get'
        params = {'userid': userid}
        # r = self.s.get(url=url, params=params)
        r = self.request(method=method, url=url, params=params)
        return r.json()


