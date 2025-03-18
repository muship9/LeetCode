package leetcode

//Given an array of integers nums which is sorted in ascending order, and an
//integer target, write a function to search target in nums. If target exists, then
//return its index. Otherwise, return -1.
//
// You must write an algorithm with O(log n) runtime complexity.
//
//
// Example 1:
//
//
//Input: nums = [-1,0,3,5,9,12], target = 9
//Output: 4
//Explanation: 9 exists in nums and its index is 4
//
//
// Example 2:
//
//
//Input: nums = [-1,0,3,5,9,12], target = 2
//Output: -1
//Explanation: 2 does not exist in nums so return -1
//
//
//
// Constraints:
//
//
// 1 <= nums.length <= 10⁴
// -10⁴ < nums[i], target < 10⁴
// All the integers in nums are unique.
// nums is sorted in ascending order.
//
//
// 👍 12406 👎 270

// leetcode submit region begin(Prohibit modification and deletion)
func BinarySearch(nums []int, target int) int {

	// 配列の最初のインデックス
	left := 0
	// 配列の最後のインデックス
	right := len(nums) - 1

	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			return mid
		}

		if nums[mid] < target {
			left = mid + 1
		}

		if nums[mid] > target {
			right = mid - 1
		}
	}

	return -1

}

//leetcode submit region end(Prohibit modification and deletion)
