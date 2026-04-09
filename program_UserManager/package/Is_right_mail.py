import re

def checkemail(mail):
    result = re.match(r'^[0-9a-zA-Z.-_]+@[a-zA-Z0-9.-_]+$', mail)
    if result:
        return 1
    else:
        return 0