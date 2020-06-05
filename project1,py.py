#task 1
radius=float(input("enter the radius of circle:"))
#area of circle is pi*r*r
pi=3.14159
area=pi*radius**2
print("the area of circle is=",area)


#task 2
file=input("Enter your file with extension:")
#fextension refers to file extension
fextension=file.split(".")
print("the extension name is:",fextension[-1])
