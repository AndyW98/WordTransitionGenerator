class MarkovChain():

    def __init__(self):
        self.table = []
        self.words = {}
        self.num_words = 0
        self.last_word = ''
        self.transitions = []

    def add_word(self, word):
        if word in self.words.keys():
            x = self.words[word]
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
        
        if self.last_word is not '':
            y = self.words[self.last_word]
            self.table[x][y] = self.table[x][y] + 1
            self.append_to_transitions((self.last_word, word, self.table[x][y]))
        
        self.last_word = word

    def append_to_transitions(self, transition):
        for i in self.transitions:
            if (i[0] == transition[0]) and (i[1] == transition[1]) and (i[2] < transition[2]):
                self.transitions.remove(i)
        self.transitions.append(transition)
        if len(self.transitions) > 9:
            lowest_num = self.transitions[0]
            for i in self.transitions:
                if i[2] < lowest_num[2]:
                    lowest_num = i
            self.transitions.remove(lowest_num)
    
    def construct_sentence(self, length=10, starting_word='I'):
        sentence = starting_word
        next_word = self.table[self.words[starting_word]]

        for i in range(length):
            highest_odds = (next_word[0], 0)
            for j in range(len(next_word)):
                if next_word[j] > highest_odds[0]:
                    highest_odds = (next_word[j], j)
            for j in self.words.keys():
                if self.words[j] == highest_odds[1]:
                    sentence = sentence + " " + j
            next_word = self.table[highest_odds[1]]

        return sentence