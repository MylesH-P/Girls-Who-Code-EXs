


def respond(response, favColor):
    if (response == "Hungry"):
        print("EAT A WAFFLE")
    else:
        print("cool story, I guess")
        if( favColor == "Red"):
            print("Are you an angry person?")

def main():
    print("hi :)")
#    word = input("hey how are you feeling")
#    respond(word)
#    secondWord = input ("But how are you REALLY feeling?")
#    respond(secondWord)
    color = input("k, but what's your favorite color?")
    thirdWord = input("How is u")
    respond(thirdWord, color)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
 main()
