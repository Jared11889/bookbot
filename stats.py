#prints number of words in string
def get_num_words(input):
     return len(input.split())

#returns a count of the occurances of each character in the input text
def get_character_count(input):
     
    results = {}

    for character in input.lower():
        if character in results:
            results.update({character : results[character]+1})
        else:
            results.update({character : 1})

    return results

#takes dictionary of character counts as input, returns a sorted list of character count dictionaries.
def get_count_list(input):

    results = []

    for character in input:
        results.append({"char": character, "num": input[character]})       

    results.sort(reverse = True, key = lambda c : c["num"])

    return results