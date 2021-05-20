#duck typing

class Vscode:


    def compile(self):
        print("compiling using vscode")

    def execute(self):
        print("execute using vscode")

    def debug(self):
        print("debug using vscode")

class Pycharm:

    def compile(self):
        print("compiling using py")

    def execute(self):
        print("execute using py")

    def debug(self):
        print("debug using py")

class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()

develop=Programming()
pyc=pycharm()
