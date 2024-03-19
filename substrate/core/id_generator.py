"""
CORE ꩜ SUBSTRATE
"""
import random
from typing import Dict
from threading import Lock


class IDGenerator:
    _generators: Dict[str, "IDGenerator"] = {}
    _lock = Lock()

    def __init__(self, prefix: str):
        self.prefix = prefix
        self.n = 1

    def get_next_id(self):
        with IDGenerator._lock:
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
            random_string = "".join(random.choices(alphabet, k=8))
            next_id = f"{self.prefix}{self.n}_{random_string}"
            self.n += 1
            return next_id

    @staticmethod
    def get_instance(class_name: str) -> "IDGenerator":
        with IDGenerator._lock:
            if class_name not in IDGenerator._generators:
                IDGenerator._generators[class_name] = IDGenerator(class_name)
            return IDGenerator._generators[class_name]
