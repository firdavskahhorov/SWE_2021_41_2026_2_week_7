from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    processed={}
    for i,j in enumerate(nums):
        diff=target-j
        if diff in processed:
            return [processed[diff],i]
        processed[j]=i
    return []
