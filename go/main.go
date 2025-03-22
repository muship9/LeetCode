package main

import (
	"fmt"
	"leetcode/leetcode"
)

func main() {
	// checkSearc2DhMatrix()

	checkMinEatingSpeed()
}

func checkSearc2DhMatrix() {
	hoge := leetcode.Searc2DhMatrix([][]int{
		{1, 3, 5, 7},
		{10, 11, 16, 20},
		{23, 30, 34, 60},
	}, 31)

	fmt.Println(hoge)

}

func checkMinEatingSpeed() {
	leetcode.MinEatingSpeed([]int{1, 2, 3, 5}, 8)

}
