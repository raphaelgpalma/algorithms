def filter_words(word_list)
    filtered_words = []

    word_list.each do |word|
        if word.length > 3 && word[0].casecmp('A').zero?
            filtered_words << word
        end
    end

    filtered_words
end

words = ['Apple', 'Banana', 'Orange', 'Grapes', 'Ant', 'Mango', 'Avocado']
result = filter_words(words)
puts result