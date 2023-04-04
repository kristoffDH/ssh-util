import os
import shutil
from include.global_var import *


def backup_file():
    os.remove(SSH_CONFIG_BAK_FILE)
    shutil.copy(SSH_CONFIG_FILE, SSH_CONFIG_BAK_FILE)


def write_file(configs):
    backup_file()

    with open(SSH_CONFIG_FILE, "w+") as config_file:
        for config in configs:
            for key, value in config.items():
                if not value:
                    continue

                tab = "" if key == SSH_CONFIG_KEYS[0] else "\t"
                config_file.write(f"{tab}{key} {value}\n")

            config_file.write("\n\n")


__all__ = ["backup_file", "write_file"]
