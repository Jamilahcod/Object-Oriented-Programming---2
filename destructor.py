class Employee:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("object deleted")
ob1=Employee()
del ob1

        
