

def is_valid_input(doggo):
    acceptableDogs = ["corgi", "CORGIS", "CORGI", "Corgi", "corgis", "Corgis"]
    if doggo in acceptableDogs:
        return True
    else:
        return False
#    for puppy in acceptableDogs:
#        if puppy == doggo:
#            return True
#    return False

def divide (num):
    answer = num/2
    return answer

def main():
    print("hi :)")
    dog = input("Print a cool dog, no lames")
    if is_valid_input(dog):
        print("You have a cool dog!!")
    else:
        print("Why don't you have a CORGI?")
    even = int(input("type an even number!!!"))
    print(divide(even))
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
