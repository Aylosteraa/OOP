class Text:
    num_ch = 0
    num_words = 0
    num_sentences = 0

    def __init__(self, textfile):
        self.file = open(textfile, 'r')

    def count_ch(self):
        self.file.seek(0)
        data = self.file.read()
        print('Number of characters = ' + str(len(data) - 1))

    def count_words(self):
        self.file.seek(0)
        data = self.file.read()
        words = data.count(' ') + 1
        print('Number of words = ' + str(words))

    def count_sentences(self):
        self.file.seek(0)
        data = self.file.read()
        sentences = data.count('.')
        print('Number of sentences = ' + str(sentences))


file = Text("file1.txt")
file.count_ch()
file.count_words()
file.count_sentences()
