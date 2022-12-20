from typing import NoReturn

class Map:
    def __init__(self) -> NoReturn:
        self.map = {}
        self.dop_info = {}

    def get_start_pos(self) -> str:
        return list(self.map.keys())[0]

    def read_map_from_csv_file(self, filename: str) -> NoReturn:
        temp = read_csv(filename)
        self.map = {node: paths.split(',') for node, paths in temp.items()}

    def read_info_from_csv_file(self, filename: str) -> NoReturn:
        self.dop_info = read_csv(filename)

    def create_map(self, map_file, info_file):
        self.read_map_from_csv_file(map_file)
        self.read_info_from_csv_file(info_file)

    def check_patency(self, exwords: list[str]) -> bool:
        if len(dfs(self.map, list(self.map.keys())[0], [], exwords)) == len(self.map.keys()):
            return True
        return False
