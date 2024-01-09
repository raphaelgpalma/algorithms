def filter_words(word_list):
    """
    Filters words that have more than three letters and start with 'A'.
    
    Parameters:
    - word_list: A list of strings.
    
    Returns:
    - A new list containing words that meet the criteria.
    """
    filtered_words = []

    for i in word_list: 
        if len(i) > 3 and i[0] == "A":
            filtered_words.append(i)
            
            
    return filtered_words

    
    


words = ['Apple', 'Banana', 'Orange', 'Grapes', 'Ant', 'Mango', 'Avocado']
result = filter_words(words)
print(result)
