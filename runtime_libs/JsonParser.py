import json

class JsonParser:
    def __init__(self, json_str:str = "{}"):
        self.json_str = json_str
        self.json_dict = json.loads(self.json_str)

    def json_to_dict(self):
        return self.json_dict

    def dict_to_json(self, dict:dict = {}):
        return json.dumps(dict, ensure_ascii=False, indent=4)