import hashlib
import string
import time

class ParseDate(object):

    def __init__(self, separator=u' '):
        self.separator = separator

    def __call__(self, values):
        date = time.strptime(self.separator.join(values), "%d %b %y")
        month = str(date.tm_mon).lower().capitalize()
        if (len(month) == 1):
            month = "0" + month
        return string.join([str(date.tm_year), month, str(date.tm_mday)], "-")

class ParseUsername(object):

    def __init__(self, separator=u'/'):
        self.separator = separator

    def __call__(self, values):
        name = None
        for value in values:
            if value:
                name = value.split(self.separator)
                break
        if name:
            for value in name:
                if value:
                    return value
        return name

class HashStringList(object):

    def __init__(self, separator=u' '):
        self.separator = separator

    def __call__(self, values):
        return hashlib.sha224(self.separator.join(values)).hexdigest()
