from platformdirs import user_data_dir

class PathData():
    def __init__(self):
        pass

    def data_path(self):
        return user_data_dir