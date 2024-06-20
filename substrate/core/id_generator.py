"""
CORE ꩜ SUBSTRATE
"""
import random
from typing import Dict
from threading import Lock


class IDGenerator:
    _generators: Dict[str, "IDGenerator"] = {}
    _lock = Lock()

    def __init__(self, prefix: str, length: int = 8):
        self.prefix = prefix
        self.n = 1
        self.length = length

    def get_next_id(self):
        with IDGenerator._lock:
            random_string = IDGenerator.random_string(self.length)
            next_id = f"{self.prefix}{self.n}_{random_string}"
            self.n += 1
            return next_id

    @staticmethod
    def random_string(length: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
        random_string = "".join(random.choices(alphabet, k=length))
        return random_string

    @staticmethod
    def get_instance(class_name: str) -> "IDGenerator":
        with IDGenerator._lock:
            if class_name not in IDGenerator._generators:
                IDGenerator._generators[class_name] = IDGenerator(class_name)
            return IDGenerator._generators[class_name]

    @staticmethod
    def prefixed_id(prefix: str, length: int = 32) -> str:
        radom_string = IDGenerator.random_string(length)
        return f"{prefix}_{radom_string}"
