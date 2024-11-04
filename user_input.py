def user_details(name,age,location):
    name=input('please enter your name: ')
    age=int(input('please enter your age: '))
    location=input('please enter your location: ')

    print(f"Your name is {name} ,you are {age} years old and you are from {location}")
user_details("name","age","location")