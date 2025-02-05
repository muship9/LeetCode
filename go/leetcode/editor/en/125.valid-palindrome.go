//A phrase is a palindrome if, after converting all uppercase letters into
//lowercase letters and removing all non-alphanumeric characters, it reads the same
//forward and backward. Alphanumeric characters include letters and numbers.
//
// Given a string s, return true if it is a palindrome, or false otherwise.
//
//
// Example 1:
//
//
//Input: s = "A man, a plan, a canal: Panama"
//Output: true
//Explanation: "amanaplanacanalpanama" is a palindrome.
//
//
// Example 2:
//
//
//Input: s = "race a car"
//Output: false
//Explanation: "raceacar" is not a palindrome.
//
//
// Example 3:
//
//
//Input: s = " "
//Output: true
//Explanation: s is an empty string "" after removing non-alphanumeric
//characters.
//Since an empty string reads the same forward and backward, it is a palindrome.
//
//
//
//
// Constraints:
//
//
// 1 <= s.length <= 2 * 10⁵
// s consists only of printable ASCII characters.
//
//
// 👍 9979 👎 8496

package main

import (
	"fmt"
	"strings"
	"unicode"
)

// A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.
// 大文字をすべて小文字に変換し、英数字以外の文字をすべて取り除いた後、前後で同じ読みができる場合、そのフレーズは回文である。英数字にはアルファベットと数字が含まれる。
// 文字列 s が与えられたとき、それが回文であれば真を、そうでなければ偽を返します。
// 回分 = 上から読んでも下から読んでも同じ
// 例) しんぶんし

// leetcode submit region begin(Prohibit modification and deletion)

func main() {
	testCases := []string{
		"racecar",  // 回文
		"madam",    // 回文
		"hogehoge", // 非回文
		"12321",    // 回文
		"hello",    // 非回文
		"あいいあ",     // 回文 (日本語)
		"パタトクカシーーシカクトタパ", // 回文 (カタカナ)
		"A man, a plan, a canal: Panama",
	}

	for _, s := range testCases {
		fmt.Printf("%s は回文ですか？ -> %v\n", s, isPalindrome(s))
	}
}

func badIsPalindromeme(s string) bool {
	a := make([]rune, 0, len(s))
	b := make([]rune, 0, len(s))
	for _, c := range s {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			lowC := unicode.ToLower(c)
			// 先順で文字列を格納
			a = append(a, lowC)

			// b の先頭に文字列を追加していくことで後順になる
			// append は第一引数に Slice 第二引数に文字列を受け取るので引数に合わせて型を変える必要がある
			// append(c, b)はエラーになるため以下のように型に合わせて定義
			b = append([]rune{lowC}, b...)

		}
	}
	return string(a) == string(b)
}

func isPalindrome(s string) bool {
	t := ""
	for _, c := range s {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			t += string(unicode.ToLower(c))
		}
	}

	for i := 0; i < len(t)/2; i++ {
		if t[i] != t[len(t)-i-1] {
			return false
		}
	}
	return true
}

//leetcode submit region end(Prohibit modification and deletion)

// Solution に記載されてた一番早かったやつ
func goodIsPalindrome(s string) bool {
	if len(s) <= 1 {
		return true
	}
	s = strings.ToLower(s)
	bytes := make([]byte, 0)
	for _, r := range []byte(s) {
		if (r >= 97 && r <= 122) || (r >= 48 && r <= 57) {
			bytes = append(bytes, r)
		}
	}
	for i, j := 0, len(bytes)-1; i < j; i++ {
		if bytes[i] != bytes[j] {
			fmt.Println(string(bytes[i]), string(bytes[j]))
			return false
		}
		j--
	}
	return true
}
