# Exercise1
ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]  # in years
ages = list(set(ages))  # remove duplicates
result = max(ages)
print("highest number in ages is", result)
print("")


# Exercise2 - Comparing lists
def one_common_member(list1, list2):  # checks if 2 lists has at least 1 common member
    for i in list1:
        for n in list2:
            if i == n:
                return True
            break
    else:
        return False


ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages1 = [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
result = one_common_member(ages, ages1)
print(result)
