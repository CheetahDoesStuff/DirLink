import tomllib, shutil, tarfile
from src.dirlink.log import log # using the package to make the package, nice

# Begin hardcoded data
PKG_NAME = "dirlink" # The name of the package to generate
SRC_DIR = "DirLink" # The name of the root folder (the one containing this script)

class builder:

    def get_version():
        with open("pyproject.toml", "r") as f:
            data = tomllib.load()
        
        version = data["project"]["version"]
        log("info", f"Fetching Version: {version}")
        return version


def main():
    version = builder.get_version()


if __name__ == "__main__":
    pass