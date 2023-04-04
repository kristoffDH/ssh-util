from util import print_console
from proc.config_handle import *


def run(configs):
    loop = True

    while loop:
        print(f"Select mode")
        print(f"(q: exit, a: add, u, update, d: delete, l: list, c: connect)")
        cmd = input("input : ")
        print("")

        if cmd in ["q", "Q", "exit"]:
            break

        elif cmd in ["a", "A", "add"]:
            add(configs)

        elif cmd in ["d", "D", "delete"]:
            delete(configs)

        elif cmd in ["u", "U", "update"]:
            update(configs)

        elif cmd in ["l", "L", "list"]:
            print_console.show_list(configs)

        elif cmd in ["c", "C", "connect"]:
            if connect(configs):
                loop = False

        else:
            print_console.error("not supported input")

        print("\n")


__all__ = ["run"]
