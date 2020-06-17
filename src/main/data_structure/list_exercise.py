def sort_list_buble_asc(list):
    list_length = len(list)
    for index in range(0,list_length-1):
        for ind in range(0,list_length-index-1):
            if list[ind] > list[ind+1]:
                temp = list[ind+1]
                list[ind+1] = list[ind]
                list[ind] = temp
    
    return list


def sort_list_buble_dec(list):
    list_length = len(list)
    for index in range(0,list_length-1):
        for ind in range(0, list_length-index-1):
            if list[ind] < list[ind + 1]:
                temp = list[ind+1]
                list[ind+1] = list[ind]
                list[ind] = temp
    return list

def binary_search(list,value):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right)//2
        if list[mid] == value:
            return 'Yes'
        elif list[mid] < value :
            left = mid + 1
        else:
            right = mid - 1
    
    return 'No'

def binary_search2(list,value):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left+right) //2
        if list[mid] == value:
            return 'Y'
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return 'N'


