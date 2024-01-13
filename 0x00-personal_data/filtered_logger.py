#!/usr/bin/env python3

import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = separator.join(
        [f"{field}=.*?(?={separator}|$)" for field in fields])
    return re.sub(
        pattern, lambda match: match.group().replace(
            match.group().split('=')[1], redaction), message)
