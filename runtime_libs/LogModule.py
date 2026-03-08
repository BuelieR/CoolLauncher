class LogModule:
    def __init__(self, code: int = 200):
        self.code:int = code
        self.log:dict = {
            "code": self.code,
            "log": "",
            "url":"",
            "out_path":""
        }

    def info_log(self, log:str = "", url:str = "", out_path:str = ""):
        self.log["code"] = self.code
        self.log["log"] = "[Launcher | INFO] " + log
        self.log["url"] = url
        self.log["out_path"] = out_path
        return self.log

    def error_log(self, log:str = "", url:str = "", out_path:str = ""):
        self.log["code"] = 404
        self.log["log"] = "[Launcher | ERROR] " + log
        self.log["url"] = url
        self.log["out_path"] = out_path
        return self.log

    def warning_log(self, log:str = "", url:str = "", out_path:str = ""):
        self.log["code"] = 400
        self.log["log"] = "[Launcher | WARNING] " + log
        self.log["url"] = url
        self.log["out_path"] = out_path
        return self.log