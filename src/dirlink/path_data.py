from platformdirs import user_data_dir

class PathData():
    def __init__(self):
        pass

    def _data_path(self):
        return user_data_dir("DirLink", "CheetahsPrograms")
    
    def data_file(self):
        return _data_path() / "links.dl-dat"