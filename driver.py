from reader import Reader
from data import MarkovChain

def main():
    reader = Reader()
    reader.read(True)

    table = MarkovChain()
    for word in reader.get_words():
        table.add_word(word)
    print(table.transitions)
    print(table.construct_sentence(50, "import"))

if __name__ == "__main__":
    main()