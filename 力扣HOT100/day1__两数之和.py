
#借助查找表实现，这里用哈希表
def twoSum(nums, target: int):
    num_dict = {}
    for i,num in enumerate(nums):
        # print(i)
        #如果列表中的某个值减去目标值在字典中，就返回这个值和字典中对应的值
        if target-num in num_dict:
            print(num_dict[target-num],i)
            return [num_dict[target-num],i]
        # 如果不在字典中就将对应的元素存入到字典中
        else:
            num_dict[num]=i
            # print(num_dict)

twoSum([1,7,2,15],9)
'''
输入：nums = [3,2,4], target = 6
输出：[1,2]
'''