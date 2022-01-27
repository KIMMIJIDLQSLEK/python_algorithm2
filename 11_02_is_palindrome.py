#재귀를 이용한 회문검사하기
#재귀일때 문제를 축소시킬수 있으면 사용
input = "소주만병만주소"

# abcdcba에서 맨앞==맨뒤
# bcdcb에서 맨앞==맨뒤
# cdc에서 맨앞==맨뒤
# d이면 True


def is_palindrome(string):
    if len(string)<=1: #문자열이 남은개수가 1보다 작거나 같으면 True
        return True
    if string[0]!=string[-1]: #문자열의 맨앞!=맨뒤하면 False
        return False

    return is_palindrome(string[1:-1]) #재귀




print(is_palindrome(input))