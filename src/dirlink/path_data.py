from platformdirs import user_data_dir

class PathData:
    
    def data_file():
        return user_data_dir("DirLink", "BravestCheetah") / "links.dl-dat"
