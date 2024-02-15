from typing import Dict, Any
from threading import Lock


class SingletonMeta(type):
    _instances: Dict['SingletonMeta', Any] = {}
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> 'SingletonMeta':
        # Double-Checked Locking
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
