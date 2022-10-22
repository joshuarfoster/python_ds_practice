def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    old_phrase_list =list(phrase)
    new_phrase_list = []
    i= -1
    for char in old_phrase_list:
        if i == -1 or old_phrase_list[i] == ' ':
            new_phrase_list.append(old_phrase_list[i+1].upper())
        else:
            new_phrase_list.append(old_phrase_list[i+1].lower())
        i = i + 1
    return ''.join(new_phrase_list)