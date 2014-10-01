import cStringIO

import autocode_line


def parse_string(string):
    io = cStringIO.StringIO(string)
    for line in io:
        text = line.strip()
        if text:
            autocode_line.parse('line', text)
