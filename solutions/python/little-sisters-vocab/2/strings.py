"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + str(word)

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    vocab = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + vocab)

def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith("i"):
        return root[:-1] + "y"
    return root

def adjective_to_verb(sentence, index):
    words = sentence.split()
    clean_word = words[index].strip(".,!?")
    return clean_word + "en"
