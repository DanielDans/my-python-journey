words = set()

def check(word):
    return word.lower() in words

def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
# open() will open a file and return it as file
# .read() reads the content into a string
# .splitlines() splits the string into a list of lines
# var.update(content) inserts the content into var

# not a lot today, i spent most of the day on cs50x