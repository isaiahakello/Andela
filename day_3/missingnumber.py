def find_missing(list1, list2):
    if not len(list1) and not len(list2):
        return 0
    elif list1 == list2:
        return 0
    elif len(list1) > len(list2):
        for missing in list1:
            if missing not in list2:
                return missing
    else:
        for missing in list2:
            if missing not in list1:
return missing
