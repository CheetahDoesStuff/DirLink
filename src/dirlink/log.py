from termcolor import colored

log_types = {
    "info": colored("[ INFO ]", "green"),
    "warn": colored("[ WARNING ]", "yellow"),
    "err": colored("[ ERROR ]", "red"),
    "succ": colored("[ SUCCESS ]", "light_green")
}

colored()

def log(type, message):
    # Example: [ DIRLINK ] [ INFO ] Sucessfully Saved Link
    print(f"{colored(" [ DIRLINK ] ", "blue")}{log_types[type]}{message}")