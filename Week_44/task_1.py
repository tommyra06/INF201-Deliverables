import pathlib
import re


def data_reader() -> list:
    folder = pathlib.Path(r'd2_data\2026')
    info = []
    pattern = re.compile(
        r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+"
        r"\[(?P<register_id>[^\]]+)\]\s+"
        r"item=(?P<item>\S+)\s+"
        r"price=(?P<price>\d+\.\d+)\s+"
        r"(?P<currency>[A-Z]{3})\s+"
        r"\((?P<status>SUCCESS|REFUND|CANCELLED)\)"
    )

    for file in folder.rglob('*.log'):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        data = match.groupdict()
                        info.append(data)
        except UnicodeError:
            with open(file, 'r', encoding='latin-1') as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        data = match.groupdict()
                        info.append(data)
    return(info)
