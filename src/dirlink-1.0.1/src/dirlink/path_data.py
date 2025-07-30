from platformdirs import user_data_dir
from pathlib import Path

class PathData:
    
    def data_file():
        return Path(user_data_dir("DirLink", "BravestCheetah")) / "links.dl-dat"
