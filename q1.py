def find_indices(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None

def temp(tempratures):
    answer = []
    for i in range(len(tempratures)):
        if i == len(tempratures):
            answer.append(0)
            break
        for j in range(i+1, len(tempratures)):
            if j == len(tempratures):
                answer.append(0)
                break
            if tempratures[i] < tempratures[j]:
                answer.append(j-i)
                break
    return answer
            
            


arr = [1, 3, 2, 6, 7, 9]
print(temp(arr))