
def multiply(nums):
    answer = 1
    for x in nums:
        answer = answer * x
    return answer
numbers = list(map(int, input().split()))
print(multiply(numbers))