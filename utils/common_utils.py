import yaml
import json


class CommonUtils:
    """实用工具"""

    @classmethod
    def get_data(cls, file_name, file_type):
        """
        读取文件数据
        :param file_name: 文件的名称
        :param file_type: 读取文件的类型；yaml、json
        :return:
        """
        file_path = "../data/" + file_name
        with open(file_path, "rb") as file:
            data = file.read()
            if file_type == "yaml":
                result = yaml.safe_load(data)
            if file_type == "json":
                result = json.loads(data)
        return result
