class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low: int = 0
 
        # Right boundary of the current search range.
        high: int = len(nums) - 1
 
        # Keep searching while a valid range still exists.
        while low <= high:
            # Calculate the middle index safely.
            mid: int = low + (high - low) // 2
 
            # The target is found at the middle position.
            if nums[mid] == target:
                return mid
 
            # Check whether the left half is normally sorted.
            if nums[low] <= nums[mid]:
                # The target lies inside the sorted left half.
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    # The target must lie in the other half.
                    low = mid + 1
            else:
                # The left half is not sorted, so the right half must be sorted.
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    # The target must lie in the other half.
                    high = mid - 1
 
        return -1
 
 