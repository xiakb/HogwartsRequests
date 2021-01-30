import requests


def get_token():
    corp_id = 'ww24df69a5091eb6a5'
    corp_secret = 'g0VC-ouX3uYk04fL4mxlulmFf5Xg4Q0jnyfOocjb_og'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}'
    r = requests.get(url=url)
    return r.json()['access_token']


def test_add_member():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        'userid': 'zhangsan',
        'name': '张三',
        'mobile': '13800000000',
        'department': [2]
    }
    r = requests.post(url=url, json=data)
    print(r.json())
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == 'created'


def test_delete_member():
    userid = 'zhangsan'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid={userid}'
    r = requests.get(url=url)
    print(r.json())
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == 'deleted'
