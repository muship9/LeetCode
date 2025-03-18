package leetcode

//You are given an m x n integer matrix matrix with the following two
//properties:
//
//
// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the
//previous row.
//
//
// Given an integer target, return true if target is in matrix or false
//otherwise.
//
// You must write a solution in O(log(m * n)) time complexity.
//
//
// Example 1:
//
//
//Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
//Output: true
//
//
// Example 2:
//
//
//Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
//Output: false
//
//
//
// Constraints:
//
//
// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 100
// -10⁴ <= matrix[i][j], target <= 10⁴
//
//
// 👍 16540 👎 441

// leetcode submit region begin(Prohibit modification and deletion)
func Searc2DhMatrix(matrix [][]int, target int) bool {
	pl := 0
	pr := len(matrix) - 1

	for pl <= pr {

		pm := (pr + pl) / 2

		// target が最小値より小さければ中央値より右側を探索範囲に変更する
		// len(matrix[0]) -1 で探索配列の最大値を取得する
		if target > matrix[pm][len(matrix[0])-1] {
			pl = pm + 1

			// len(matrix[0]) -1 で探索配列の最最小値を取得する
		} else if target < matrix[pm][0] {

			pr = pm - 1
		} else {
			break
		}
	}

	if !(pl <= pr) {
		return false
	}

	mid := pl + (pr-pl)/2
	cl := 0
	cr := len(matrix[mid]) - 1

	for cl <= cr {
		cm := (cl + cr) / 2

		if matrix[mid][cm] == target {
			return true
		}

		if matrix[mid][cm] < target {
			cl = cm + 1
		}

		if matrix[mid][cm] > target {
			cr = cm - 1
		}

	}

	return false
}

//leetcode submit region end(Prohibit modification and deletion)
