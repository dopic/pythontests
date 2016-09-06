# CodePage
# -*- coding: utf-8 -*-
from MyPackage import MyFirstClass
from flask import Flask
import sys
import functions


app = Flask(__name__)


def repeat(term, times):
    return functions.repeat(term, times)


def test():
    app.run()


@app.route("/")
def hello():

    name = "World"
    if len(sys.argv) > 0:
        name = sys.argv[1]

    return MyFirstClass.hello(name)

names = ["Douglas", "Tiago", "Magda"]

if __name__ == '__main__':
    # print repeat(sys.argv[1], int(sys.argv[2]))
    # test()

    namesMerged = names + [repeat(sys.argv[1], 3)]

    for name in namesMerged:
        print name
    # Como no javascript, ele não dá erro em um typo até não executar a linha
    # Continuar em: https://developers.google.com/edu/python/strings

