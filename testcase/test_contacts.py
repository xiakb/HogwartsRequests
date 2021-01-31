import requests
from business.contacts import Contacts


class TestContacts:
    """通讯录测试类"""

    def setup_class(self):
        self.contacts = Contacts()
        self.userid = 'zhangsan'
        self.name = '张三'

    def test_create_member(self):
        """测试添加成员"""
        create_result = self.contacts.create_member(self.userid, self.name, '13800000000', [2])
        try:
            find_result = self.contacts.find_member(self.userid)
        finally:
            self.contacts.delete_member(self.userid)
        assert create_result['errcode'] == 0
        assert create_result['errmsg'] == 'created'
        assert find_result['name'] == self.name

    def test_update_member(self):
        """测试更新成员"""
        self.contacts.create_member(self.userid, self.name, '13800000000', [2])
        change = {'mobile': '13800000001'}
        update_result = self.contacts.update_member(self.userid, **change)
        try:
            find_result = self.contacts.find_member(self.userid)
        finally:
            self.contacts.delete_member(self.userid)
        assert update_result['errcode'] == 0
        assert update_result['errmsg'] == 'updated'
        assert find_result['mobile'] == '13800000001'

    def test_delete_member(self):
        """测试删除成员"""
        self.contacts.create_member(self.userid, self.name, '13800000000', [2])
        delete_result = self.contacts.delete_member(self.userid)
        assert delete_result['errcode'] == 0
        assert delete_result['errmsg'] == 'deleted'
