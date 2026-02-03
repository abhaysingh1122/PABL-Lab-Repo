#Kadane's Algorithm to find the maximum sum of a contiguous subarray

def kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Subarray Sum =", kadane(arr))

arr1 = [-5, -2, -8]
print(kadane(arr1)) 
