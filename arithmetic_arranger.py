def arithmetic_arranger(problems, result=False):
    '''
    freeCodeCamp project: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
    :param problems: list of max 5 strings with 4dig integers separated by single space with either + or - between
    :param result: boolean, whether or not to show actual answer of expression
    :return: addition and or subtraction operations displayed side by side sep by 4 spaces
    '''
    ls = [x.split(' ') for x in problems]
    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif not all(flag == '+' or flag == '-' for (_,flag,_) in ls):
        return 'Error: Operator must be "+" or "-".'
    elif not all(flag.isnumeric() for (flag,_,_) in ls) or \
        not all(flag.isnumeric() for (_,_,flag) in ls):
        return 'Error: Number must contain only digits.'
    elif not all(int(flag) < 10000 for (flag,_,_) in ls) or \
        not all(int(flag) < 10000 for (_,_,flag) in ls):
        return 'Error: Number cannot be more than four digits.'

    def firstN(item):
        return int(item.split(" ")[0])

    def op(item):                                           # this function is causing problems
        return str(item.split(" ")[1])

    def secN(item):
        return int(item.split(" ")[2])

    def sumdiff(item):
        if item.split(" ")[1] == '+':
            output = firstN(item) + secN(item)
        if item.split(" ")[1] == '-':
            output = firstN(item) - secN(item)
        return output

    # testing
    a = 'h'
    b = 'y'

    firstline = ''
    secondline = ''
    thirdline = ''
    fourthline = ''

    for item in problems:
        baseLen = max(len( str(firstN(item))), len(str(secN(item))) ) + 2
        firstline += f'{firstN(item):>{baseLen}}' + '    '
        # secondline += f'{op:<2}{secN(item):>{baseLen-2}}' + '    '   # baseLen-2            ERROR ON THIS LINE
        secondline += f'{a:<2}{b:>{baseLen-2}}' + '    '   # baseLen-2
        thirdline += '-'*baseLen + '    'cdcd
        fourthline += f'{sumdiff(item):>{baseLen}}' + '    '

    firstline += '\n'
    secondline += '\n'
    thirdline += '\n'
    arranged_problems = firstline + secondline + thirdline

    if result:
        return arranged_problems + fourthline
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))