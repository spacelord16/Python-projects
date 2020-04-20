def load_data():
    return (
        "George Bernard Shaw|You can not believe in honor until you have achieved it. Better keep yourself clean and "
        "bright; you are the window through which you must see the world.",
        "Gilbert Keith Chesterton|Those thinkers who cannot believe in any gods often assert that the love of "
        "humanity would be in itself sufficient for them; and so, perhaps, it would, if they had it.",
        "Brian Tracy|You cannot control what happens to you, but you can control your attitude toward what happens to "
        "you, and in that, you will be mastering change rather than allowing it to master you.",
        "Johann Wolfgang Von Goethe|When all is said the greatest action is to limit and isolate one's self.",
        "Malcolm S. Forbes|The biggest mistake people make in life is not trying to make a living at doing what they "
        "most enjoy.",
        "Isadora Duncan|What one has not experienced one will never understand in print.",
        "Sri Ramakrishna|So long as the bee is outside the petals of the lily, and has not tasted the sweetness of "
        "its honey, it hovers around the flower emitting the buzzing sound; but when it is inside the flower, "
        "it noiselessly drinks the nectar. So long as a man quarrels and disputes about doctrines and dogmas, "
        "he has not tasted the nectar of true faith; when he has tasted it, he becomes quiet and full of peace.",
        "Author Unknown|Young men, and old men too, should learn the truth that the only real, lasting pleasure in "
        "life comes from being actively busy at some work every day; doing something worth while, and doing it as "
        "well as you know how. The more we appreciate this fact, the more will we be able to make the most of our "
        "lives.",
        "Ralph Waldo Emerson|Without a rich heart, wealth is an ugly beggar.",
        "G. Randolf|Truly great friends are hard to find, difficult to leave, and impossible to forget.",
        "Richard Baker|To get rich never risk your health. For it is the truth that health is the wealth of wealth.",
        "Rogers|The good are better made by ill, As odors crush'd are sweeter still.",
        "Johann Wolfgang Von Goethe|What by a straight path cannot be reached by crooked ways is never won.",
        "Mohammed|Patience is the key to contentment.",
        "Arnold Bennett|You wake up in the morning, and your purse is magically filled with twenty-four hours of "
        "un-manufactured tissue of the universe of your life! It is yours. It is the most precious of possessions. No "
        "one can take it from you. And no one receives either more or less than you receive.",
        "Isaac B. Singer|When you betray somebody else, you also betray yourself.",
        "St. Gregory The Great|The universe is not rich enough to buy the vote of an honest man.",
        "Reverend Theodore M. Hesburgh|The most important thing a father can do for his children is to love their "
        "mother.",
        "Vince Lombardi|The spirit, the will to win, and the will to excel are the things that endure. These "
        "qualities are so much more important than the events that occur.",
        "Ralph Marston|There are very real obstacles and challenges to any course of action. And there's no need to "
        "add to them, by making up obstacles of your own. Unchain yourself from the bondage of your own thinking.",
        "Pythagoras|Wisdom thoroughly learned will never be forgotten.",
    )


def parse_data(data):
    if data is None or len(data) is 0:
        return None

    result = list()
    for row in data:
        fields = row.split('|')
        if len(fields) is not 2:
            return None
        result.append(dict(author=fields[0], quote=fields[1]))
    return result


def wrap(message, size):
    import textwrap
    return textwrap.wrap(message, size)


def banner(ref, size=40, screen_size=79):
    quote = wrap(ref['quote'], size)
    prefix = int((screen_size - size) /2)
    if prefix < 0:
        prefix = 0
    prefix = ' ' * (prefix -1)
    print(prefix, '*' * size)
    for line in quote:
        print(prefix, line)
    author =  "--- " + ref['author']
    if len(author) > size:
        author = wrap(author, size)
        for row in author:
            print(prefix, author)
    else:
        while len(author) < size:
            author = " " + author
        print(prefix, author)
    print(prefix, '*' * size)


def list_authors(zquotes):
    unique = set()
    for quote in zquotes:
        unique.add(quote['author'])
    unique = sorted(unique)
    for ss, author in enumerate(unique, 1):
        print(ss, ".)", author)


def count_words(zquotes):
    counter = dict()
    for quote in zquotes:
        quote = quote['quote']
        quote = str(quote).replace('.', '')
        quote = str(quote).replace('!', '')
        quote = str(quote).replace(',', '')
        quote = str(quote).replace(';', '')
        for word in quote.split(' '):
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    order = sorted(counter.keys())
    for ss, word in enumerate(order, 1):
        print(ss, ".)", counter[word], "-", word)


zquotes = parse_data(load_data())

options = {"1":"List Authors", "2":"Word Counter", "5":"Quit"}
while True:
    for option in sorted(options.keys()):
        print(option, ".)", options[option])
    select = input("Enter Choice: ")
    if select is "1":
        list_authors(zquotes)
        print()
    if select is "2":
        count_words(zquotes)
        print()
    if select is "5":
        break
# (code ends)