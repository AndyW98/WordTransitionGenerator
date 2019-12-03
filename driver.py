from reader import Reader
from data import MarkovChain
import csv

def main():
    # Read the text file into the program
    reader = Reader()
    reader.read(True)

    # Read the count matrix into the table
    table = MarkovChain()
    option = input("(1): Read from a CSV\n(2): Read from a text file\n")

    if option == str(1):
        csv_file = "output.csv"
        txt_file = "transitions.txt"
        table.read_from_csv(csv_file, txt_file)

    elif option == str(2):
        for word in reader.get_words():
            table.add_word(word)

        # Construct the transition matrix and write it to a file
        table.create_transition_matrix()
        table.write_to_csv()
        print("\nTransition matrix saved to \'output.csv\'\n")
        table.write_transitions()
        print("\nTransitions saved to \'transitions.txt\'\n")

    # Find the equilibrium matrix (n = 10 iterations)
    vector = table.gen_rand_pop_vector()

    print("\nTop ten population sizes: ")
    TopTen = table.transitions
    for i in TopTen:
        print(i)

    print("\nTraining finished, now type words to find the predicted next word (QUIT to finish):\n")
    userin = None
    count = 0
    while userin != "QUIT":
        count += 1
        userin = input("(" + str(count) + "): ")
        if userin == "QUIT":
            break
        word = table.predict_word(userin)
        if word is not None:
            print("Predicted word: " + word)
        else:
            print("ERROR: Word cannot be predicted")

if __name__ == "__main__":
    main()
