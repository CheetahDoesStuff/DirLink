from src.dirlink.path_data import PathData
from src.dirlink.log import log

class LinkManager():
    def __init__(self):
        pass

    # Returns Boolean, true: exit the process (error occured), false: keep going
    def add_link(self, link: str) -> bool:
        data_path = PathData.data_path()

        with open(data_path / "links.dlink", "a+") as f:

            data = f.read()
            data = data.split("\n")

            if link in data:
                log("err", "Link Already Exists. Error code: 1")
                f.close()
                return True
            
            f.write(link)
            f.close()
        
        log("info", "Successfully Saved Link")
        return False
            
