
# 复杂度nlog2(n)
def quick_sort(nums):
    if len(nums) <1:
        return []
    pivot = nums[len(nums)//2] 
    left = [i for i in nums if i<pivot]
    middle = [i for i in nums if i==pivot ]
    right = [i for i in nums if i>pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    print(quick_sort([3,1,5,5,8,2,54,76,77,897890,89,0,788,978,87,978,89,867]))
# 输出：[0, 1, 2, 3, 5, 5, 8, 54, 76, 77, 87, 89, 89, 788, 867, 978, 978, 897890]
