from proc import util_process, config_handle
from util import print_console

if __name__ == "__main__":

    config_list = []

    try:
        config_list = config_handle.load("r+")
    except FileNotFoundError:
        print_console.error("Check config-util. config-util is not existed...")
        result = input("generate?(y or n) ")
        if result in ["y", "Y"]:
            config_list = config_handle.load("w+")
        else:
            exit(1)

    try:
        util_process.run(config_list)

    except KeyboardInterrupt:
        pass


# 파일이 없을때 생성 가능해야함.
# 파일이 비어있음 현재 에러 표시...
