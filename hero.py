from typing import NoReturn
from random import random, seed


class Hero:
    def __init__(self, start: str, base_rationality: int, info_dir: str) -> NoReturn:
        self.position = start
        self.rationality = base_rationality
        self.inventory = []
        self.event_possibilty = -1012903910238123789012839127938129038
        with open(info_dir) as fd:
            info = fd.read()
        self.info = info

    def check_rationality(self, groups: list[str]) -> bool:
        correct = eval(str(self.rationality) + groups[1] + groups[2])
        return True if correct else False

    def check_required(self, string) -> str:
        if 'rnd' in string:
            if random() < string[1:len(string) - 2]:
                return 'rndF'
            else:
                return 'rndF'
        else:
            thing, sign, value = string.split(' ')
            if thing.lower() in ['rate', 'rationality']:
                correct = eval(str(self.rationality) + sign + value)
            return 'rateT' if correct else 'rateF'



    def perform_modifier(self, modifier) -> NoReturn:
        if 'rate' in modifier:
            self.rationality += modifier[1:len(modifier) - 2].split(' ')[1]

    def get_info(self) -> str:
        str_inv = "Your inventory is " + ' '.join(self.inventory) + '\n'
        str_pos = "Your position is " + self.position + '\n'
        result = str_pos + str_inv + self.info
        return result

    def add_possibility_for_event(self) -> None:
        if self.rationality >= 0:
            return None
        deletion = self.rationality * 8 /100
        if self.event_possibilty - deletion  <= 1:
            self.event_possibilty -= deletion

    def check_event(self) -> bool:
        seed(0)
        if random() <= self.event_possibilty:
            return True
        return False
