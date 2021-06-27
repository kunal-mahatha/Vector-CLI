import os
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Funtion to calculate the position vector by two points in a space
    @classmethod
    def pos_vector(cls):
        os.system('cls||clear')

        print("""

        **************************************************
        |------------Find the Position Vector------------|
        **************************************************
        |                                                |
        |          Enter the Position of Points          |
        |               separated by comma               |
        |                    e.g. x,y,z                  |
        |                                                |
        |________________________________________________|

        """)

        x1, y1, z1 = input("""        Enter the position 1 : """).split(',')

        x2, y2, z2 = input("""        Enter the position 2 : """).split(',')
        
        a = int(x1) - int(x2)
        b = int(y1) - int(y2)
        c = int(z1) - int(z2)
        print(f"""

        **************************************************
          The position vector is along {a}i + {b}j + {c}k
        **************************************************

        """)

        name = []
        print(f"""
        **************************************************
        |----------HIT ENTER TO RETURN TO MENU-----------|
        **************************************************
        
        """)
        n = input()
        name.append(n)
        if type(name) is list:
            Vector.menu_option()

    # Function to finds whether the vectors are perpendicular or not
    @classmethod
    def is_perpendicular(cls):
        os.system('cls||clear')

        print("""

        **************************************************
        |-----Find if the vectors are perpendicular------|
        **************************************************
        |                                                |
        |          Enter the Position of Points          |
        |               separated by comma               |
        |                    e.g. x,y,z                  |
        |                                                |
        |________________________________________________|

        """)

        x1, y1, z1 = input("""        Enter the position 1 : """).split(',')

        x2, y2, z2 = input("""        Enter the position 2 : """).split(',')

        a = int(x1)*int(x2) + int(y1)*int(y2) + int(z1)+int(z2)
        if a == 0:
            print("""
            
        **************************************************
              Yes Both the Vectors are Perpendicular
        **************************************************

            """)
        else:
            print("""

        **************************************************
             Nope ! The Vectors are not Perpendicular
        **************************************************

            """)

        name = []
        print("""
        **************************************************
        |----------HIT ENTER TO RETURN TO MENU-----------|
        **************************************************
        
        """)
        n = input()
        name.append(n)
        if type(name) is list:
            Vector.menu_option()

    # Function to find the direction of the vector, by finding the unit vector
    @classmethod
    def direction(cls):

        os.system('cls||clear')

        print("""

        **************************************************
        |--------Find the direction of the vector--------|
        **************************************************
        |                                                |
        |           Enter the position vector            |
        |               separated by comma               |
        |                    e.g. x,y,z                  |
        |                                                |
        |________________________________________________|

        """)


        x, y, z = input("""        Enter the position vector separated by comma : """).split(',')
        a = int(x)**2 + int(y)**2 + int(z)**2
        i = int(x)/a
        j = int(y)/a
        k = int(z)/a
        print(f"""
        **************************************************
              The Direction of the vector is along 
                      {round(i, 2)}i + {round(j, 2)}j + {round(k, 2)}k
        **************************************************
        """)

        name = []
        print("""
        **************************************************
        |----------HIT ENTER TO RETURN TO MENU-----------|
        **************************************************
        
        """)
        n = input()
        name.append(n)
        if type(name) is list:
            Vector.menu_option()

    # Function to calculate the magnitude of the vector
    @classmethod
    def magnitude(cls):

        os.system('cls||clear')

        print("""

        **************************************************
        |--------Find the magnitude of the vector--------|
        **************************************************
        |                                                |
        |           Enter the position vector            |
        |               separated by comma               |
        |                    e.g. x,y,z                  |
        |                                                |
        |________________________________________________|

        """)

        x, y, z = input("""        Enter the position vector separated by comma : """).split(',')
        a = int(x)**2 + int(y)**2 + int(z)**2
        print(f"""
        **************************************************
               The Magnitude of the Vector is  {round((a**(0.5)), 2)}
        **************************************************
        """)

        name = []
        print("""
        **************************************************
        |----------HIT ENTER TO RETURN TO MENU-----------|
        **************************************************
        
        """)
        n = input()
        name.append(n)
        if type(name) is list:
            Vector.menu_option()
    # First Window of the tool
    @classmethod
    def description(cls):
        os.system('cls||clear')
        print("""

        **************************************************
        |---------------------VECTOR---------------------|
        **************************************************
        |                                                |
        |             A tool for operation on            |
        |                vector quantities               |
        |                                                |
        |              Hit Enter to Continue:            |
        |                                                |
        |________________________________________________|

        """)

        name = []
        n = input()
        name.append(n)
        if type(name) is list:
            Vector.menu_option()

    # Menu Options
    @classmethod
    def menu_option(cls):
        os.system('cls||clear')
        print("""

        **************************************************
        |---------------------MENU-----------------------|
        **************************************************
        |                                                |
        |    1. Find the Position Vector                 |
        |                                                |
        |    2. Find the Magnitude of the Vector         |
        |                                                |
        |    3. Find if the vectors are perpendicular    |
        |                                                |
        |    4. Find the Direction of the vector         |
        |                                                |
        |    5. Exit                                     |
        |                                                |
        |________________________________________________|

        """)

        num = int(input("""        Enter your Choice : """))

        if num == 1:
            Vector.pos_vector()
        if num == 2:
            Vector.magnitude()
        if num == 4:
            Vector.direction()
        if num == 3:
            Vector.is_perpendicular()
        if num == 5:
            quit()
        if num > 5:
            print("Please Enter Valid Input")
        Vector.menu_option()
        

Vector.description()
