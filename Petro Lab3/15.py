example = {'one':1,
           'two':2,
           'three':3,
           'four':4
            }


def revert(d):
    '''
    Function which reverts a dictionary
    (keys become values, values become keys)
    '''
    res = {}
    for i,j in example.items():
        res[j] = i

    return res

print(revert(example))

