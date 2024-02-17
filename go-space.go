package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := []int{1,2,3}
	fmt.Println(a[-1])
}

func haveConflict(e1 []string, e2 []string) bool {

	var t2i = func(t string) int {
		ans, _ := strconv.Atoi(t[:2])
		ans *= 60
		min, _ := strconv.Atoi(t[3:])
		return ans + min
	}

	s1, f1, s2, f2 := t2i(e1[0]), t2i(e1[1]), t2i(e2[0]), t2i(e2[1])
	if f2 < s1 || s2 > f1 {
		return false
	}
	return true
}
