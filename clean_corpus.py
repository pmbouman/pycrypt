from toolz.functoolz import compose 
import re
with open("austen.txt") as f:
    input_lines = f.readlines()

def make_filter(filter_fn):
    return lambda iterable: (it for it in iterable if filter_fn(it))


def utf_decode(lines):
    print(type(lines))
    forout = list(map(lambda line: line.decode("utf-8"), lines))
    return forout


def remove_ends(lines):
    startpoint = 1 + [i for i in range(len(lines)) if
                      "CONTENTS" in lines[i]][0]
    stoppoint = [i for i in range(len(lines)) if lines[i]
                 .find('*** END OF THE PROJECT') > -1][0]
    return lines[startpoint:stoppoint]


def join_lines(lines):
    return "".join(lines)


def filter_chapter_titles(lines):
    def is_chapter_title(line):
        return (line.find("Chapter") == -1)

    forout = list(filter(is_chapter_title, lines))
    return forout


def to_upper(str):
    return str.upper()


def alpha_only(instr):
    return re.sub(r'[^A-Z]', ' ', instr)


def to_single_spaces(instr):
    return re.sub(' +', ' ', instr) 


def split_to_words(instr):
    return instr.split(" ") 


def drop_singletons(wordlist):
    return list([w for w in wordlist if (len(w)) > 1])

"""
IMPORTANT:
This compose function executes the last function
i.e. utf-decode  FIRST
"""

pipeline = compose(
                   to_single_spaces,
                   alpha_only,
                   to_upper,
                   join_lines,
                   filter_chapter_titles
                   )


cleaned_text = pipeline(input_lines)
#
#
#def make_freqs(itemlist):
#    counts = dict()
#    for my_item in itemlist:
#        if my_item in counts:
#            counts[my_item] += 1
#        else:
#            counts[my_item] = 1
#    return counts
#
#
#def show_sorted_freqs(counts_dict):
#    print({k: v for k, v in sorted(counts_dict.items(), reverse=True,
#                                   key=lambda item: item[1])}) 


wordlist = drop_singletons(split_to_words(cleaned_text))
#wordfreqs = make_freqs(wordlist)

def make_bigrams(word):
    if (len(word) == 1):
        return []
    else:
        return [word[0:2]] + make_bigrams(word[1:])



"""pseuo coede:
  in the word frequencies, for every word: note the # of occurences,
break into bigrams, update count dict by thst word's frequency
"""

"""
for word in corpus_clean:
    if word in letter_counts:
        letter_counts[word] += 1
    else:
        letter_counts[word] = 1



def all_bigrams(word):
    if len(word) < 2:
        return [] 
    else:
        return [word[0:2]] + all_bigrams(word[1:])

"""
