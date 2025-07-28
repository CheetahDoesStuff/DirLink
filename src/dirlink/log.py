from termcolor import colored

log_types = {
    "info": colored("[ INFO ]", "green"),
    "warn": colored("[ WARNING ]", "yellow"),
    "err": colored("[ ERROR ]", "red")
}

colored()

def log(type, message):
    # Example: [ DIRLINK ] [ INFO ] Sucessfully Saved Link
    print(f"{colored(" [ DIRLINK ] ")}{log_types[type]}{message}")