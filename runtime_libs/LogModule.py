class LogModule:
    def __init__(self, code: int = 200):
        self.code:int = code
        self.log:dict = {
            "code": self.code,
            "log": "",
            "out":"",
            "out_path":""
        }

    def info_log(self, log:str = "", out:str = "", out_path:str = ""):
        self.log["code"] = self.code
        self.log["log"] = "[Launcher | INFO] " + log
        self.log["out"] = out
        self.log["out_path"] = out_path
        return self.log

    def error_log(self, log:str = "", out:str = "", out_path:str = ""):
        self.log["code"] = 404
        self.log["log"] = "[Launcher | ERROR] " + log
        self.log["out"] = out
        self.log["out_path"] = out_path
        return self.log

    def warning_log(self, log:str = "", out:str = "", out_path:str = ""):
        self.log["code"] = 400
        self.log["log"] = "[Launcher | WARNING] " + log
        self.log["out"] = out
        self.log["out_path"] = out_path
        return self.log

    def log_folder_check(self) -> bool:
        # TODO:Check if there is a folder that is used to save log files.
        pass