import re


def is_valid(email):
    return re.match('[a-zA-Z0-9]{6,10}@(qq|163|gmail).com', email)