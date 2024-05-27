class student:
    def __init__(self,name,rollnum,javamarks,pythonmarks,mathmarks):
        self.name=name
        self.rollnum=rollnum
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathmarks=mathmarks
    def printAlldetails(self):
        print(self.name)
        print(self.rollnum)
        print(self.javamarks)
        print(self.pythonmarks)
        print(self.mathmarks)
obj1=student("thanush",501,77,66,78)
obj1.printAlldetails()

obj2=student("teja",502,88,44,45)
obj2.printAlldetails()


obj3=student("ramu",503,85,54,48)
obj3.printAlldetails()






