import re

def parse_path(data: str) -> list[str]:
    pattern = r'^(?P<Condition>\{\S+ [<>=] \d+\})?(?P<Room>[?-??-??? A-Za-z \d \( \) \- \? \.]+)(?P<Modifier>\[\S+ [\-\+\*\\] \d+\])?$'

    auto = re.compile(pattern)
    m = auto.search(data)
    return m.groups()
