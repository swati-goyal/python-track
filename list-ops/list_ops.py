def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result.append(item)
    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    l = 0
    for item in list:
        l += 1
    return l


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
