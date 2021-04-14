import yaml
import json


class Utils:

    @classmethod
    def get_data(cls, file_name, file_type):
        file_path = "../data/" + file_name
        with open(file_path, "rb") as file:
            data = file.read()
            if file_type == "yaml":
                result = yaml.safe_load(data)
            if file_type == "json":
                result = json.loads(data)
        return result
