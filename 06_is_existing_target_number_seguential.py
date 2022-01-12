finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_exist_target_number_sequential(target, numbers):
    count=0
    for number in numbers:
        count+=1
        if number==target:
            return count


result = is_exist_target_number_sequential(finding_target, finding_numbers)
print(result)