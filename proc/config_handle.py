import subprocess

from colorama import Fore, Style
from util import file_util

from include.global_var import *
from util import print_console
from proc import config_parser


def load(mode):
    ssh_config_file = open(SSH_CONFIG_FILE, mode)
    all_lines = ssh_config_file.readlines()
    ssh_config_file.close()

    return config_parser.run_parsing(all_lines)


def add(configs):

    config = {}

    for key in SSH_CONFIG_KEYS:
        value = input(f"[in] {key} : ")
        config[key] = value

    print("\n[Check input value]")
    print_console.show_config(config, Fore.YELLOW)

    result = input(Fore.GREEN + "save? (y/n) " + Style.RESET_ALL)

    if result in ["y", "Y"]:
        configs.append(config)
        file_util.write_file(configs)


def delete(configs):
    if not print_console.show_list(configs):
        return

    config_len = len(configs)
    index = get_input(config_len)

    if index == -1:
        print_console.error("Index can only use numbers")
        return

    elif index == -2:
        print_console.error("invalid index...")
        return

    print("\n[Check delete config]")
    print_console.show_config(configs[index], Fore.YELLOW)

    result = input(Fore.GREEN + "delete? (y/n) " + Style.RESET_ALL)

    if result in ["y", "Y"]:
        configs.pop(index)
        file_util.write_file(configs)


def update(configs):
    if not print_console.show_list(configs):
        return

    config_len = len(configs)
    index = get_input(config_len)

    if index == -1:
        print_console.error("Index can only use numbers")
        return

    elif index == -2:
        print_console.error("invalid index...")
        return

    print(Fore.YELLOW + f"If will not change data then press blank" + Style.RESET_ALL)
    config = configs[index]

    for key in SSH_CONFIG_KEYS:
        pre_value = config.get(key, "")
        value = input(f"{key} ({pre_value}) \n->")
        config[key] = value if value else pre_value

    print("\n[Check update value]")
    print_console.show_config(config, Fore.YELLOW)

    result = input(Fore.GREEN + "save? (y/n) " + Style.RESET_ALL)

    if result in ["y", "Y"]:
        configs[index] = config
        file_util.write_file(configs)


def connect(configs):
    if not print_console.show_list(configs):
        return False

    config_len = len(configs)
    index = get_input(config_len)

    if index == -1:
        print_console.error("Index can only use numbers")
        return False

    elif index == -2:
        print_console.error("invalid index...")
        return False

    config = configs[index]
    host_key = SSH_CONFIG_KEYS[0]
    ssh_command = f"ssh {config[host_key]}"

    subprocess.run(ssh_command)
    return True


def get_input(list_size):
    idx_range = "0" if list_size == 1 else f"0 - {list_size -1}"
    select_index = input(Fore.CYAN + f"Select index ({idx_range}) : " + Style.RESET_ALL)

    if not select_index.isnumeric():
        return -1

    select_index = int(select_index)
    if select_index < 0 or select_index > list_size - 1:
        return -2

    return select_index


__all__ = [
    "load",
    "add",
    "delete",
    "update",
    "connect",
    "get_input",
]
