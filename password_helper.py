# %%
import pandas as pd


def proceed_password(password):
    result = []

    upper_cases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".upper())
    lower_cases = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
    digits = list("1234567890")
    specials = list("!@#\$%^&*()_-+=|\\/<>\"'~`")

    characters = list(str(password))

    #upper case
    upper_case_count = 0
    lower_case_count = 0
    digit_count = 0
    special_count = 0
    
    for each_char in characters:
        if upper_cases.__contains__(each_char): upper_case_count = upper_case_count + 1
        if lower_cases.__contains__(each_char): lower_case_count = lower_case_count + 1
        if digits.__contains__(each_char): digit_count = digit_count + 1
        if specials.__contains__(each_char): special_count = special_count + 1
    result = [password,len(characters),upper_case_count,lower_case_count,digit_count,special_count,-1]
    return result

result = proceed_password('Sio64@ti7o')




# %%
