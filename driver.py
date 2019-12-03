from reader import Reader
from data import MarkovChain

def main():
    # Read the text file into the program
    reader = Reader()
    reader.read(True)

    # Read the count matrix into the table
    table = MarkovChain()
    for word in reader.get_words():
        table.add_word(word)

    # Construct the transition matrix and write it to file
    table.create_transition_matrix()
    table.write_to_csv()

    # Find the equilibrium matrix (n = 10 iterations)
    vector = table.gen_rand_pop_vector()

    print("\nTop ten population sizes: ")
    TopTen = table.transitions
    for i in TopTen:
        print(i)

    print("\nTransition matrix saved to \'output.csv\'\n")

    print("\nTraining finished, now type words to find the predicted next word (QUIT to finish):\n")
    userin = None
    count = 0
    while userin != "QUIT":
        count += 1
        userin = input("(" + str(count) + "): ")
        word = table.predict_word(userin)
        print("Predicted word: " + word)

if __name__ == "__main__":
    main()
