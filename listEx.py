def main():
    print("hi :)")
    food = []
    print("Hey future Myles, input 3 foods!")
    for i in range(5):
        grub = input("type your food now!")
        food.append(grub)
        print("the len of this list right now is ", len(food))
    print("nice list!")
    print(food)
    print("The third food on your list was ", food[2])

    print("The len now is ", len(food))
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
 main()
