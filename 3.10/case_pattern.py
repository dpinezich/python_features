def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [first, *rest]:
            return first + sum_list(rest)
        
print(sum_list([3,4,5,6]))