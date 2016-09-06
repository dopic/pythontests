import re
import os
import sys


def repeat(term, times):
    return term * times


def exit():
    sys.exit(0)


def match(text, term):
    return re.match(term, text)


def showHelp(command):
    help(command)
