class MyFirstClass(object):

    @staticmethod
    def hello(name):

        if name:
            return 'Hello %s' % name

        return 'Hello World'
