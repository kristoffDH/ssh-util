import os

SSH_CONFIG_FILE = f"{os.path.expanduser('~')}/.ssh/config"
SSH_CONFIG_BAK_FILE = f"{os.path.expanduser('~')}/.ssh/config.backup"
SSH_CONFIG_KEYS = [
    "Host",
    "HostName",
    "User",
    "Port",
    "IdentityFile",
]


__all__ = [
    "SSH_CONFIG_FILE",
    "SSH_CONFIG_BAK_FILE",
    "SSH_CONFIG_KEYS",
]
