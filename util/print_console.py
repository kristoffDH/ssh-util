from colorama import Fore, Style
from include.global_var import *


def error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)


def show_list(configs):
    if not configs:
        print(Fore.RED + f"File is empty..." + Style.RESET_ALL)
        return False

    for index, config in enumerate(configs):
        print(Fore.YELLOW + f"[Index : {index}]" + Style.RESET_ALL)

        for key, value in config.items():
            tab = "" if key == SSH_CONFIG_KEYS[0] else "    "
            print(tab + Fore.BLUE + f"{key} " + Style.RESET_ALL + value)

        print("")

    return True


def show_config(config, color):
    if not config:
        error("Config is null")
        return

    for key, value in config.items():
        tab = "" if key == SSH_CONFIG_KEYS[0] else "  "
        print(tab + color + f"{key} " + Style.RESET_ALL + value)

    print("")


__all__ = [
    "error",
    "show_config",
    "show_list",
]
