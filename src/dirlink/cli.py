import argparse
from pathlib import Path

from .link_manager import LinkManager

def main():
    parser = argparse.ArgumentParser(
                        prog="DirLink", 
                        description="A CLI Tool Developed In Python To More Quickly Navigate Your Filesystem", 
                        epilog="The Whole Tool Is Open Source On Github!"
                        )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    

    # New Link Command
    new = subparsers.add_parser("new", help="Create A New Directory Link")

    new.add_argument("name", help="The Name Of Your Link")
    new.add_argument("path", help="Path Your Link Will Lead To")


    # Remove Link Command
    remove = subparsers.add_parser("remove", help="Remove An Existing Directory Link")

    remove.add_argument("name", help="The Name Of The Link To Remove")


    # Load Link Command
    remove = subparsers.add_parser("load", help="Loads Your Link Command To Your Clipboard")
    remove.add_argument("name", help="Name Of The Link To Load")

    args = parser.parse_args()
    manager = LinkManager()
   
    if args.command == "new":
        manager.add_link(args.name, Path(args.path))
    elif args.command == "remove":
        manager.rm_link(args.name)
    elif args.command == "load":
        manager.load_link(args.name)

if __name__ == "__main__":
    main()
