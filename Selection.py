
def sort(nums):
    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

if __name__ == "__main__":
    num_count = int(input("Enter the number of elements: "))
    nums = []

    for i in range(num_count):
        num = int(input(f"Enter element {i + 1}: "))
        nums.append(num)

    sort(nums)
    print("Sorted list:", nums)








# Enter the number of elements: 6
# Enter element 1: 5
# Enter element 2: 3
# Enter element 3: 8
# Enter element 4: 6
# Enter element 5: 7
# Enter element 6: 2
# Sorted list: [2, 3, 5, 6, 7, 8]


# O(n^2)