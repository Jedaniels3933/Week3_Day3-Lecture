nums = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
#return an array of all posituve numbers in the array
#and an array of the sum of negative numbers

def solution(numbers):
    count_positive = 0
    sum_negative = 0

    for number in nums:
        if number > 0:
            count_positive += 1
        elif number < 0:
            sum_negative += nums
        
    if len(nums) == 0:
        return []
    print [count_positive, sum_negative]

    

      
        
    


