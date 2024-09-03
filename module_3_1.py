def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    lth = len(string)
    upr_string = string.upper()
    lwr_string = string.lower()
    return lth, upr_string, lwr_string
def is_contains(string, list_to_search):
    count_calls()
    s = False
    for i in list_to_search:
        if i.upper() == string.upper():
           s = True
           break
    return s

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)