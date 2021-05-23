import requests


# 使用 pytest 的收集钩子，在 pytest 执行用例收集时会自动调用
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        # 取出收集到的每一个用例，将用例 nodeid 和路径发送到创建用例接口，实现用例的生成
        # print(
        # item.name.encode("utf-8").decode("unicode_escape"),
        # item.nodeid.encode("utf-8").decode("unicode_escape"))
        requests.post(
            "http://localhost:5000/test_case",
            json={
                "name": item.name.encode("utf-8").decode("unicode_escape"),
                "nodeid": item.nodeid.encode("utf-8").decode("unicode_escape"),
                "description": item.fspath.strpath
            }
        )
