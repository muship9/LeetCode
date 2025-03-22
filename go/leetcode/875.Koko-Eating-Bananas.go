package leetcode

import (
	"math"
	"sort"
)

func MinEatingSpeed(piles []int, h int) int {
	// k の最小値 / 最大値を定義
	min := 1
	sort.Ints(piles)
	max := piles[len(piles)-1]

	for min <= max {
		mid := min + (max-min)/2
		total := 0

		for _, p := range piles {
			total += int(math.Ceil(float64(p) / float64(mid)))
		}

		// h時間以内に条件を満たすかチェック
		if total <= h {
			// 条件を満たす場合はより小さい k を探す
			// mid が条件を満たしていることになるから mid - 1 の値でチェックする
			max = mid - 1
		} else {
			// 条件をみさなければ min を mid より +1 大きい値でチェックする
			min = mid + 1
		}
	}

	return min
}
