def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    dict = {}
    for sentence in sentences:
        for word in sentence:
            if (dict.get(word, 0) == 0):
                dict[word] = 1
            else:
                dict[word] += 1

    return dict