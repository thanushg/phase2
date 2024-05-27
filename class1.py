class student:
    def __init__(self,name,rollnum,javamarks,pythonmarks,mathmarks):
        self.name=name
        self.rollnum=rollnum
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathmarks=mathmarks
obj=student("thanush",501,77,66,78)
print(obj.name)
print(obj.rollnum)
print(obj.javamarks)
print(obj.pythonmarks)
print(obj.mathmarks)