
class Model():
    def __init__(self):
        self.database = {}
        self.load_database()

    def load_database(self):
        with open("catch_rates","r") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            print(lines)
            for line in lines:
                a=line.split("/")
                self.database[a[1]]=a[2]
    def get_rate(self,name):
        return self.database[name]
