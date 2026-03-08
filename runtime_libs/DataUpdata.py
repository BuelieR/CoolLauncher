import json
import runtime_libs.LogModule as LogModule

class DataUpdata:
    def __init__(self, file_path:str = "runtime_libs/Settings.json"):
        self.file_path = file_path
        self.default_context = {
            "version_json_url": "http://launchermeta.mojang.com/mc/game/version_manifest.json",
            "geometry": "640x480",
            "java_url": "https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/java_17.jar",
            "java_path": "runtime_libs/java_runtime/java.exe"
        }
        
    def updata(self,context:str = self.default_context):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(context, indent=4, ensure_ascii=False))
                f.close()
            return LogModule.LogModule(200).info_log(
                f"模块 [DataUpdata] 成功更新 {self.file_path}",
                f"{self.file_path}"
            )
        except:
            return LogModule.LogModule(404).error_log(
                f"模块 [DataUpdata] 未找到 {self.file_path}",
                f"{self.file_path}"
            )
