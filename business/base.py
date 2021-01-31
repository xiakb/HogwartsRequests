import requests


class Base:
    """基础类"""

    def __init__(self):
        """
        1.初始化session会话\n
        2.添加assess_token到session会话中\n
        """
        self.s = requests.Session()
        self.corp_id = 'ww24df69a5091eb6a5'
        self.corp_secret = 'g0VC-ouX3uYk04fL4mxlulmFf5Xg4Q0jnyfOocjb_og'
        self.s.params['access_token'] = self.get_token().get('access_token')

    def get_token(self, corp_id=None, corp_secret=None):
        """
        获取access_token
        :param corp_id: 企业ID
        :param corp_secret: 指定应用的secret
        :return: 获取的access_token信息
        """
        if corp_id is None:
            corp_id = self.corp_id
        if corp_secret is None:
            corp_secret = self.corp_secret
        params = {'corpid': corp_id, 'corpsecret': corp_secret}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url=url, params=params)
        return r.json()
