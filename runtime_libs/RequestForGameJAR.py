import runtime_libs.DataGet as DataGet
import runtime_libs.JsonParser as JsonParser
import runtime_libs.LogModule as LogModule
import urllib.request

class RequestForGameJAR:
    def __init__(
        self, version:str = "1.0", year:bool = False, 
        latest:bool = False):
        
        self.version_json_url:str = DataGet.DataGet(
            "version_json_url").get_launcher_data()
        self.year:bool = year
        self.latest_version:bool = latest

    def get_game_download_url(self):
        try:
            # 先判断是否联网
            try:
                return_url = urllib.request.urlretrieve(
                    self.version_json_url,
                    "runtime_libs/versions.json"
                )
            except:
                pass
            finally:
                with open("runtime_libs/versions.json", "r") as f:
                    version_json = JsonParser.JsonParser(
                        f.read()).json_to_dict()
                    f.close()
                for i in version_json["versions"]:
                    if i["id"] == self.version:
                        return_version_url = i["url"]
                        break

                return LogModule.LogModule(200).info_log(
                    f"模块 [RequestForGameJAR] 成功获取"+
                    f"{self.version_json}\n内容：\n{return_url}\n",
                    f"{return_version_url}"
                )
        except:
            return_url = LogModule.LogModule(404).error_log(
                f"模块 [RequestForGameJAR] 未找到 runtime_libs/versions.json",
                f"{return_version_url}"
            )