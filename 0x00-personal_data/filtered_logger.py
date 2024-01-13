#!/usr/bin/env python3

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = re.compile('|'.join(
        [f"(?P<{field}>{field}=[^{separator}]*)" for field in fields]))
    return pattern.sub(
        lambda match: match.group().split('=')[0] + '=' + redaction, message)
