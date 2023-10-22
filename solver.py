from sanajahti import Game


# current running time: around 1 second
if __name__ == "__main__":
    words = set()
    with open("kotus_wordlist.txt") as f:
        for word in f:
            word = word.strip()
            words.add(word)

    userinput = input("All letters unseparated from left to right, up to down: ")
    letters = list(userinput)
    game = Game(letters, words)
    lst = game.solve()

    for word in lst:
        print(word)
