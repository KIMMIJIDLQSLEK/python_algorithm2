finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    start=0
    end=len(array)-1
    #print(end)
    count=0
    while start<=end:
        mid=(start+end)//2
        count += 1;
        if array[mid]==target:
            return count
        if array[mid]<target:
            print(target,"은",array[mid],"보다 up")
            start=mid+1
        else:
            print(target,"은",mid,"보다 down")
            end=mid-1

    return count

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result,"번만에 성공")