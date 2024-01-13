#!/usr/bin/env python3

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """_summary_

    Args:
        fields (List[str]): _description_
        redaction (str): _description_
        message (str): _description_
        separator (str): _description_

    Returns:
        str: _description_
    """
    pattern = re.compile('|'.join(
        [f"(?P<{field}>{field}=[^{separator}]*)" for field in fields]))
    return pattern.sub(
        lambda match: match.group().split('=')[0] + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        for field in self.fields:
            message = re.sub(f"{field}=.*?{self.SEPARATOR}",
                             f"{field}={self.REDACTION}{self.SEPARATOR}",
                             message)
        return message


if __name__ == "__main__":
    main()
