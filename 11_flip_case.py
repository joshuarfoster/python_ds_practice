def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_string=[]
    for ltr in phrase:
        if ltr==to_swap.lower():
            new_string.append(ltr.upper())
        elif ltr==to_swap.upper():
            new_string.append(ltr.lower())
        else:
            new_string.append(ltr)
    return ''.join(new_string)
