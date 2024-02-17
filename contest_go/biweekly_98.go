package main

import (
	"fmt"
	"sort"
)

func main() {
	res := 8 | 75 | 1 | 2
	fmt.Println(res)
	fmt.Println(minImpossibleOR([]int{5, 3, 2}))
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func intToArr(a int) []int {
	res := make([]int, len(fmt.Sprint(a)))
	for i := 0; a > 0; i++ {
		res[i] = a % 10
		a /= 10
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}

func arrToInt(A []int) int {
	res := 0
	for _, a := range A {
		res *= 10
		res += a
	}
	return res
}

func maxArr(A []int) int {
	res := A[0]
	for _, a := range A {
		if a > res {
			res = a
		}
	}
	return res
}

func minArr(A []int) int {
	res := A[0]
	for _, a := range A {
		if a < res {
			res = a
		}
	}
	return res
}

func minImpossibleOR(A []int) int {
	for i := 0; i < 40; i++ {
		res := 1 << i
		flag := false
		for _, b := range A {
			if b == res {
				flag = true
				break
			}
		}
		if !flag {
			return res
		}
	}
	return 0
}

func minimizeSum(A []int) int {
	sort.Slice(A, func(i, j int) bool {
		return A[i] < A[j]
	})
	n := len(A)
	res := []int{A[n-2] - A[1], A[n-1] - A[2], A[n-3] - A[0]}
	return minArr(res)
}

func minMaxDifference(num int) int {
	A, B := intToArr(num), intToArr(num)
	base := A[0]
	for i, a := range A {
		if a == base {
			A[i] = 0
		}
	}

	for _, b := range B {
		if b != 9 {
			base = b
			break
		}
	}

	for i, b := range B {
		if b == base {
			B[i] = 9
		}
	}

	return arrToInt(B) - arrToInt(A)
}
