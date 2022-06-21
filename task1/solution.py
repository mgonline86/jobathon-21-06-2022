def solution(S:str):
    '''
    replaces all occurrences of "plus" with "+" and all occurrences of "minus" with "-" given a string.
    '''
    try:
        return S.replace("minus","-").replace("plus","+")
    except Exception as err:
        return("Error:" + str(err))