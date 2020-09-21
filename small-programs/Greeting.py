
def greeting(**name):
    print("Enter a name if you so please...")
    name = input()
    if name == "" :
        print("Hello everyone")
    else:
        print("Hello "+ name)

greeting()

