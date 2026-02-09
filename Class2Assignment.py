class Class2AssignmentFromFile():
    def SubFields():
        print("Sub-fields in AI are:")
        SubFields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in SubFields:
            print(i)
            
    def OddEven():
        getNum=int(input("Enter a number:"))
        if((getNum%2)==0):
            print(getNum,"is Even Number")
            message="Even Number"
        else:
            print(getNum,"is a Odd Number")
            message="Odd NUmber"
        return message
        
    def MarriageEligibility():
        gender=input("Your Gender:")
        age=int(input("your age:"))
        if(gender=="Male" and age>=21):
            print("ELIGIBLE")
            Eligibility="ELIGIBLE"
        elif(gender=="Female" and age>=18):
            print("ELIGIBLE")
            Eligibility="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            Eligibility="NOT ELIGIBLE"
        return Eligibility

    def Percentage():
        Sub1= int(input("Subject1:"))
        Sub2= int(input("Subject2:"))
        Sub3= int(input("Subject3:"))
        Sub4= int(input("Subject4:"))
        Sub5= int(input("Subject5:"))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:",Total)
        Percent= (Total/500)*100
        print("Percentage:", Percent)
        return Percent

    def triangle():
        height=float(input("Height:"))
        base=float(input("Breadth:"))
        print("Area Formula: (Height*Breadth)/2")
        Area=(height*base)/2
        print("Area of Triagle:",Area)
        height1=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth1=float(input("Breadth1:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter= height1+height2+breadth1
        print("Perimeter of Triagle:",Perimeter)
        return Area , Perimeter