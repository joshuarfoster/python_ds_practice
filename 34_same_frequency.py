def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dig_list_1 = list(str(num1))
    dig_list_2 = list(str(num2))
    if len(dig_list_1) != len(dig_list_2):
        return False
    else:
        for dig in dig_list_1:
            if dig_list_1.count(dig) == dig_list_2.count(dig) is False:
                return False
        return True