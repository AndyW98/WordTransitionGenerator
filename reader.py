IGNORE_GRAMMAR = ['!', '.', ',', '?', ';', '/', '-', '\\']

class Reader():

    def __init__(self):
        self.folder = ".\\Training Files\\"
        self.file = "dracula.txt"

    def read(self, gram_remove=False):
        filepath = self.folder + self.file
        with open(filepath, 'r') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')
        while('' in lines):
            lines.remove('')
        
        words = []
        for line in lines:
            temp = line.split()
            for word in temp:
                words.append(word)
        
        self.words = words
        if gram_remove:
            self.remove_grammar()

    def remove_grammar(self):
        for grammar in IGNORE_GRAMMAR:
            for i in range(len(self.words)):
                self.words[i] = self.words[i].rstrip(grammar)
        while('' in self.words):
            self.words.remove('')

    def get_words(self):
        return self.words