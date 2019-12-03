import csv
import random

class MarkovChain():

    def __init__(self):
        self.table = []
        self.words = {}
        self.num_words = 0
        self.last_word = ''
        self.transitions = []
        self.transition_matrix = []

    # Add a new word to the markov chain
    # @params: word: the new word to add
    # @return: NONE
    def add_word(self, word):
        # Checks if the chain already knows the word
        if word in self.words.keys():
            x = self.words[word]
        # If not, log that word and add it to both the x
        # and y of the matrix
        else:
            self.words[word] = self.num_words
            self.num_words+=1
            x = self.words[word]
            temp = []
            for _ in range(self.num_words):
                temp.append(0)
            self.table.append(temp)
            for i in range(len(self.table)-1):
                self.table[i].append(0)
        
        # As long as the new word is not the first word, increment the
        # corresponding matrix position
        if self.last_word is not '':
            y = self.words[self.last_word]
            self.table[x][y] = self.table[x][y] + 1
            self.append_to_transitions((self.last_word, word, self.table[x][y]))
        
        self.last_word = word

    # Keep track of the top 10 transitions as they are entered
    # @params: transition: the new transition tuple to compare
    # @return: NONE
    def append_to_transitions(self, transition):
        for i in self.transitions:
            if (i[0] == transition[0]) and (i[1] == transition[1]) and (i[2] < transition[2]):
                self.transitions.remove(i)
        self.transitions.append(transition)
        if len(self.transitions) > 10:
            lowest_num = self.transitions[0]
            for i in self.transitions:
                if i[2] < lowest_num[2]:
                    lowest_num = i
            self.transitions.remove(lowest_num)
    
    # Creates a matrix to calculate transition percentages
    # @params: NONE
    # @return: NONE
    def create_transition_matrix(self):
        # Create the transpose matrix
        first_pass = True
        for i in range(len(self.table)):
            self.transition_matrix.append([])
            for j in range(len(self.table[i])):
                self.transition_matrix[i].append(self.table[j][i])
        
        # Change to percentages
        total = 0
        for column in self.transition_matrix:
            for i in column:
                total += i
            for i in range(len(column)):
                if total > 0:
                    column[i] = column[i] / total
            total = 0

    # Saves the transition matrix to a csv file
    # @params: NONE
    # @return: NONE
    def write_to_csv(self):
        with open("output.csv", 'w+', newline='') as f:

            fieldnames = self.words.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for i in range(len(self.transition_matrix[0])):
                temp = {}
                for word in self.words.keys():
                    temp[word] = self.transition_matrix[self.words[word]][i]
                writer.writerow(temp)
    
    # Generates a random population vector using the transition matrix
    # @params: lower: the minimum random number
    #          upper: the maximum random number
    #          iterations: the number of multiplications to perform
    # @returns: vector: the generated population vector
    def gen_rand_pop_vector(self, lower=0, upper=1, iterations=10):
        if len(self.transition_matrix):
            vector = []
            # Populate the vector with random numbers
            start_temp = 1
            for i in range(len(self.transition_matrix)):
                if i < len(self.transition_matrix) - 1:
                    vector.append(random.random() % start_temp)
                    start_temp = start_temp - vector[i]
                else:
                    vector.append(start_temp)

            # Multiply the vector by the transition matrix a number of
            # times equal to iterations
            for _ in range(iterations):
                vector = self.mult_transition_matrix(vector)

        return vector

    # Multiplies a vector into the transition matrix then returns
    # the resultant vector
    # @params: vector: The 1 by X matrix to multiply into the transition
    #          matrix
    # @return: temp_vector: The modified vector
    def mult_transition_matrix(self, vector):
        temp = 0
        temp_vector = []
        for i in range(len(self.transition_matrix)):
            for j in range(len(vector)):
                temp += vector[j] * self.transition_matrix[j][i]
            temp_vector.append(temp)
            temp = 0
        return temp_vector
    
    # Takes in a sentence and predicts the next word
    # @params: sentence: The input data
    # @return: next_word: The next predicted word
    def predict_word(self, sentence):
        next_word = None
        found = False
        words = sentence.split()
        word_vector = [0] * len(self.words)

        for word in words:
            if word in self.words.keys():
                found = True
                index = self.words[word]
                # NOTE: This is to weight the vector towards the newest word
                for i in word_vector:
                    i = i / 2
                word_vector[index] += 1
        
        if found is not False:
            word_vector = self.mult_transition_matrix(word_vector)

        temp = (word_vector[0], 0,)
        for i in range(len(word_vector)):
            if word_vector[i] > temp[0]:
                temp = (word_vector[i], i,)
        
        for word in self.words.keys():
            if self.words[word] == temp[1]:
                next_word = word

        return next_word