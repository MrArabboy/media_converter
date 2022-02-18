from .base import *

try:
    from .config import *
except:
    raise ImportError(
        "Please create config.py inside settings folder and write your credentials like in config_example.py"
    )
