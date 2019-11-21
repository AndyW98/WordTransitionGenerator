from reader import Reader
from data import MarkovChain

def main():
    reader = Reader()
    print("Reading from file -- ", end='')
    reader.read(True)
    print("Complete [25%]")

    table = MarkovChain()
    print("Populating table -- ", end='')
    for word in reader.get_words():
        table.add_word(word)
    print("Complete [50%]")

    print("Creating Transition Matrix -- ", end='')
    table.create_transition_matrix()
    table.write_to_csv()
    print("Complete [75%] -- Saved under \'output.py\'")

    print("Generating random population vector -- ", end='')
    vector = table.gen_rand_pop_vector()
    TopTen = []
    for i in range(len(vector)):
        if len(TopTen) > 9:
            for j in range(len(TopTen)):
                if vector[i] > TopTen[j]:
                    temp = TopTen[j]
        else:
            TopTen.append(vector[i])
    #print("Top ten population sizes: ", end='')
    #print(TopTen)
    print(vector)
    #------
    total = 0
    for i in vector:
        total += i
    print(total)
    #------
    print("Complete [100%]")

if __name__ == "__main__":
    main()
