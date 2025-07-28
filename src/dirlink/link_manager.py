from dirlink.path_data import PathData
from dirlink.log import log

from pathlib import Path
import json

# Avoid importing all of the library for performance but not confuse as copy is such a common keyword
from pyperclip import copy as pyperclip_copy

class LinkManager():
    def __init__(self):
        pass


    # Returns Boolean, true: exit the process (error occured), false: keep going
    def add_link(self, link: str, link_path: Path) -> bool:
        data_path = PathData.data_file()

        if self.verify_link(link):
            log("err", "Could Not Create Link: Link Already Exists. Error Code: 2")
            return True

        with open(data_path, "w+") as f:
            data = json.load(f)
            if data == None:
                data = {}
            
            data[link] = link_path

            json.dump(data, f)
        
        log("info", "Successfully Saved Link")
        return False
    

    # Returns Boolean, true: exit the process (error occured), false: keep going
    def rm_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        if not self.verify_link(link):
            log("err", "Could Not Remove Link: Link Doesnt Exist. Error Code: 1")
            return True

        with open(data_path, "w+") as f:
            data = json.load(f)
            data.pop(link)
            json.dump(data, f)
        
        return False
    

    # Returns Boolean, true: link exists, false: link doesnt exist
    def verify_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        with open(data_path, "r") as f:
            data = json.load(f)
        
        if link in data:
            return True  
        return False


    # Returns Boolean, true: exit the process (error occured), false: keep going
    def load_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        if not self.verify_link(link):
            log("err", "Could Not Load Link: Link Doesnt Exist. Error Code: 1")
            return True

        with open(data_path, "r"):
            data = json.load(f)
        
        command = f"cd {data[link]}"
        pyperclip_copy(command)

        log("info", "Successfully Copied Command To Clipboard")
