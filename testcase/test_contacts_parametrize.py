from api.contacts import Contacts
import pytest
from utils.common_fun import Utils


class TestContactsParametrize:
    """通讯录测试类"""

    def setup_class(self):
        self.contacts = Contacts()

    @pytest.mark.parametrize(
        "userid, name, mobile, department",
        Utils.get_data("contacts.yaml", "yaml"),
        ids=[f"create_{i[1]}" for i in Utils.get_data("contacts.yaml", "yaml")]
    )
    def test_create_member(self, userid, name, mobile, department):
        """测试添加成员"""
        create_result = self.contacts.create_member(userid, name, mobile, department)
        try:
            find_result = self.contacts.find_member(userid)
        finally:
            self.contacts.delete_member(userid)
        assert create_result['errcode'] == 0
        assert create_result['errmsg'] == 'created'
        assert find_result['name'] == name

    @pytest.mark.parametrize(
        "userid, name, mobile, department",
        Utils.get_data("contacts.yaml", "yaml"),
        ids=[f"update_{i[1]}" for i in Utils.get_data("contacts.yaml", "yaml")]
    )
    def test_update_member(self, userid, name, mobile, department):
        """测试更新成员"""
        self.contacts.create_member(userid, name, mobile, department)
        change = {'mobile': '13800000000'}
        update_result = self.contacts.update_member(userid, **change)
        try:
            find_result = self.contacts.find_member(userid)
        finally:
            self.contacts.delete_member(userid)
        assert update_result['errcode'] == 0
        assert update_result['errmsg'] == 'updated'
        assert find_result['mobile'] == '13800000000'

    @pytest.mark.parametrize(
        "userid, name, mobile, department",
        Utils.get_data("contacts.yaml", "yaml"),
        ids=[f"delete_{i[1]}" for i in Utils.get_data("contacts.yaml", "yaml")]
    )
    def test_delete_member(self, userid, name, mobile, department):
        """测试删除成员"""
        self.contacts.create_member(userid, name, mobile, department)
        delete_result = self.contacts.delete_member(userid)
        assert delete_result['errcode'] == 0
        assert delete_result['errmsg'] == 'deleted'
