from include.global_var import *


def run_parsing(config_all_lines):
    config_map = []
    index = -1

    for line in config_all_lines:
        if not line or line[0] == "#" or line in ["\r", "\n", "\r\n"]:
            continue

        line = line.replace("\n", "").replace("\r", "").lstrip().rstrip()

        key, value = line.split(" ")

        if key == SSH_CONFIG_KEYS[0]:
            config_map.append({})
            index += 1

        if index == -1:
            return []

        config_map[index][key] = value

    return config_map


__all__ = ["run_parsing"]
