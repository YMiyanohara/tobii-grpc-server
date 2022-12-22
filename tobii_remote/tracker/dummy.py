from random import random
from typing import Tuple


class DummyTracker:
    def __init__(self) -> None:
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def get_gaze_pos(self) -> Tuple[float, float]:
        return (random(), random())
