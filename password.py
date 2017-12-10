password = "Manchester_Is_Red"


def pas(word):
    global password
    if word == password:
        print("Password match")
    else:
        print("Wrong Password")


p_word = input("Enter password: ")
pas(p_word)

