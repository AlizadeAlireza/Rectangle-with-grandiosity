# Create a class for our Rectangle

class Rectangle:
    #Constructor
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return (self.width + self.length) * 2
    def show(self):
        print("your Rectangle width and length for now is: ", self.width,"and", self.length)
        print("the perimeter of your Rectangle with",self.width,"width and",self.length,"length size is: ",obj.perimeter())
        print("the area of your Rectangle with",self.width,"width and",self.length,"length size is: ",obj.area())
    def changing_size(self):
        self.width = eval(input("Enter your number for changing Rectangle width size:  "))
        self.length = eval(input("Enter your number for changing Rectangle length size:  "))
    def grandiosity_appending_width(self):
        appending_width = eval(input("to appending your width:  "))
        self.width = self.width + appending_width
    def grandiosity_appending_length(self):
        appending_length = eval(input("to appending your length:  "))
        self.length = self.length + appending_length
    def bigger_area_multipation_way(self):
        paddle_num = eval(input("enter your paddle for make bigger your area: "))
        print("your area with grandiosity is:\n",obj.area() * paddle_num)
    def main_menu(self):
        print("0, Exit")
        print("1, Perimeter")
        print("2, Area")
        print("3, Show")
        print("4, change your width and length size")
        print("5, grandiosity")
    def grandiosity_menu(self):
        print("1, appending to your length  ")
        print("2, appending to your width  ")
        print("3, make bigger area from multiply way")
        print("4, back to main menu")
width = eval(input("please give us your width number: "))
length = eval(input("please give us your length number: "))
# build an object for calling our function
obj = Rectangle(width, length)
# build a True cycle 
choice = 1

while choice != 0:
    obj.main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("It is your perimeter:  ", obj.perimeter())
    elif choice == 2:
        print("It is your area:  ", obj.area())
    elif choice == 3:
        obj.show()
    elif choice == 4:
        obj.changing_size()
    elif choice == 5:
# another menu for grandiosity
        obj.grandiosity_menu()
        choice = 1
        while choice != 0:
            choice = int(input("Enter your new choice for use grandiosity: "))
            if choice == 1:
                obj.grandiosity_appending_length()
                print("appending to your length was successful")
                obj.show()
            elif choice == 2:
                obj.grandiosity_appending_width
                print("appending to your width was successful")
                obj.show()
            elif choice == 3:
                obj.bigger_area_multipation_way()

            elif choice == 4:
                break
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("****invalid choice****")
print()

