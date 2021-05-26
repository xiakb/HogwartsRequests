import requests


class BaseApi:
    """基础类"""

    def __init__(self):
        """
        1.初始化session会话\n
        2.添加assess_token到session会话中\n
        """
        self.s = requests.Session()
        self.corp_id = 'ww24df69a5091eb6a5'
        self.corp_secret = 'g0VC-ouX3uYk04fL4mxlupu-z6XmvR7btVUMo2Ybsiw'
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

    def request(self, method, url, **kwargs):
        """
        request函数封装
        :param method: 接口请求方式
        :param url: 接口地址
        :param kwargs: 其他参数
        :return: 请求返回的结果
        """
        request_data = self.s.request(method, url, **kwargs)
        return request_data
