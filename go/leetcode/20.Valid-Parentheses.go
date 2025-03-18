package leetcode

// かっこがちゃんと閉じられてるのか判定する
// () = true
// (} = false
// ({[]}) = true

// stack で入れてくだけだと最終的にチェック判定をしないといけない。
// 左括弧だけを stack にいれてペア判定する。最終的に stack が空であるかを見ればいい。
func isValid(s string) bool {
	// stack := linkedlitstack.New()
	// closeToOpen := map[rune]rune{')': '(', ']': '[', '}': '{'}
	//
	// for _, c := range s {
	// 	if open, exists := closeToOpen[c]; exists {
	// 		if !stack.Empty() {
	// 			top, ok := stack.Pop()
	// 			if ok && top.(rune) != open {
	// 				return false
	// 			}
	// 		} else {
	// 			return false
	// 		}
	// 	} else {
	// 		stack.Push(c)
	// 	}
	// }
	//
	// return stack.Empty()

	return true
}
