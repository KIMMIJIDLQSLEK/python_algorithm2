#반복문으로 회문검사하기
input = "abcdcba"

# #내가 짠코드
# def is_palindrome(string):
#     turn=len(string)//2
#     start=0
#     end=len(string)-1
#     for i in range(turn):
#         start+=i
#         end-=i
#         if string[start]!=string[end]:
#             return False
#     return True

#튜터님이 짠코드
def is_palindrome(string):
    n=len(string)
    for i in range(n):
        if string[i]!=string[n-1-i]:
            return False
    return True


print(is_palindrome(input))