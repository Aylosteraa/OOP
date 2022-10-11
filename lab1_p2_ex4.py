class Text:

    def __init__(self, textfile):
        self.file = open(textfile)

    def count_ch(self):
        self.file.seek(0)
        num_ch = 0
        for line in self.file:
            num_ch += len(line)
        return f'Number of characters = {num_ch}'

    def count_words(self):
        self.file.seek(0)
        num_words = 1
        for line in self.file:
            num_words += line.count(' ')
        return f'Number of words = {num_words}'

    def count_sentences(self):
        self.file.seek(0)
        num_sentences = 0
        for line in self.file:
            num_sentences += line.count('.')
        return f'Number of sentences = {num_sentences}'


file = Text("file1.txt")
print(file.count_ch())
print(file.count_words())
print(file.count_sentences())
