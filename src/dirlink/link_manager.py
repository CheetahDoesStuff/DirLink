from src.dirlink.path_data import PathData
from src.dirlink.log import log

class LinkManager():
    def __init__(self):
        pass


    # Returns Boolean, true: exit the process (error occured), false: keep going
    def add_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        if verify_link(link):
            return True

        with open(data_path, "a") as f:
            f.write(link)
            f.close()
        
        log("info", "Successfully Saved Link")
        return False
    

    # Returns Boolean, true: exit the process (error occured), false: keep going
    def rm_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        with open(data_path, "w+") as f:
            data = f.readlines()

            for link in data:
                if link.strip("\n") != link:
                    f.write(link)
    

    # Returns Boolean, true: link exists, false: link doesnt exist
    def verify_link(self, link: str) -> bool:
        data_path = PathData.data_file()

        with open(data_path, "r") as f:
            data = f.readlines()

            for loop_link in data:
                if loop_link.strip("\n") == link:
                    return True
            
            return False
