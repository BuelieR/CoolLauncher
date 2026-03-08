import runtime_libs.JsonParser as JsonParser
import runtime_libs.LogModule as LogModule

class DataGet:
    def __init__(self, data:str = "False"):
        self.data = data

    def get_launcher_data(self, file_path:str = "runtime_libs/Settings.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                GetData = JsonParser.JsonParser(content).json_to_dict()
                ReturnGetData = LogModule.LogModule(200).info_log(
                    f"模块 [DataGet] 成功获取 {self.data}",
                    GetData[self.data]
                )
                return ReturnGetData
        except Exception as e:
            self.data = LogModule.LogModule(404).error_log(
                f"模块 [DataGet] 未找到 {self.data}",
                f"{self.data}"
            )
            return self.data
