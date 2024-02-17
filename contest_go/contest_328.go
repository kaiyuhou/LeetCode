package main

import (
	"fmt"
)

func main() {
	n := 3
	Q := [][]int{
		{1, 1, 2, 2},
		{0, 0, 1, 1},
	}

	fmt.Println(rangeAddQueries(n, Q))
}

// c

func countGood(A []int, k int) int64 {
	cur := 0
	var ans int64
	cnt := make(map[int]int)
	n := len(A)

	left := 0
	for right := 0; right < n; right++ {
		cnt[A[right]] += 1
		cur += cnt[A[right]] - 1
		if cur += 
	}

}

// b

func rangeAddQueries(n int, Q [][]int) [][]int {
	A := make([][]int, n)
	res := make([][]int, n)
	for i := range A {
		A[i] = make([]int, n)
		res[i] = make([]int, n)
	}

	for _, q := range Q {
		x1, y1, x2, y2 := q[0], q[1], q[2], q[3]
		for i := x1; i < x2+1; i++ {
			A[i][y1] += 1
			if y2+1 < n {
				A[i][y2+1] -= 1
			}
		}
	}

	for i := 0; i < n; i++ {
		base := 0
		for j := 0; j < n; j++ {
			base += A[i][j]
			res[i][j] = base
		}
	}

	return res
}

// a

func differenceOfSum(A []int) int {

	getDSum := func(a int) int {
		S := fmt.Sprint(a)
		res := 0
		for _, c := range S {
			res += int(c - '0')
		}
		return res
	}

	eSum := 0
	dSum := 0
	for _, a := range A {
		eSum += a
		dSum += getDSum(a)
	}

	res := eSum - dSum
	if res < 0 {
		return -res
	}
	return res
}
