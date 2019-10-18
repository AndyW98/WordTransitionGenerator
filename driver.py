from reader import Reader
from data import MarkovChain

def main():
    reader = Reader()
    print("Reading from file -- ", end='')
    reader.read(True)
    print("Complete [33%]")

    table = MarkovChain()
    print("Populating table -- ", end='')
    for word in reader.get_words():
        table.add_word(word)
    print("Complete [67%]")

    print("Creating Transition Matrix -- ", end='')
    table.create_transition_matrix()
    table.write_to_csv()
    print("Complete [100%]\nSaved under \'output.py\'")

if __name__ == "__main__":
    main()