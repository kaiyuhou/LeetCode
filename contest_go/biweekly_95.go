package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
)

func main() {
	// event1 := []string{"01:15", "02:00"}
	// event2 := []string{"02:00", "03:00"}

	// println(haveConflict(event1, event2))
	// nums := []int{15, 45, 20, 2, 34, 35, 5, 44, 32, 30}
	// println(xorBeauty(nums))
	// stations := []int{1, 2, 4, 5, 0}
	// r := 1
	// k := 2
	stations := []int{57, 70, 35, 30, 29, 13, 17, 88, 89, 49}
	r := 1
	k := 90
	println(maxPower(stations, r, k))
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

// a

func categorizeBox(length int, width int, height int, mass int) string {
	isHeavy := false
	if mass >= 100 {
		isHeavy = true
	}

	isBulky := false
	if length >= int(math.Pow10(4)) || width >= int(math.Pow10(4)) || height >= int(math.Pow10(4)) || length*width*height >= int(math.Pow10(9)) {
		isBulky = true
	}

	if isHeavy && isBulky {
		return "Both"
	} else if isHeavy {
		return "Heavy"
	} else if isBulky {
		return "Bulky"
	}
	return "Neither"
}

// b

type DataStream struct {
	last  int
	value int
	k     int
}

func Constructor(value int, k int) DataStream {
	return DataStream{
		last:  0,
		value: value,
		k:     k,
	}
}

func (ds *DataStream) Consec(num int) bool {
	if num == ds.value {
		ds.last += 1
	} else {
		ds.last = 0
	}

	return ds.last >= ds.k
}

// c

func xorBeauty(nums []int) int {
	ans := 0
	for _, a := range nums {
		ans ^= a
	}
	return ans
}

// d

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func maxPower(s []int, r int, k int) int64 {
	n := len(s)
	pre := make([]int64, n+1)
	for i, v := range s {
		pre[i+1] = pre[i] + int64(v)
	}

	base := make([]int64, n)
	for i := range s {
		left := max(0, int64(i-r))
		right := min(int64(n-1), int64(i+r))
		base[i] = pre[right+1] - pre[left]
	}

	di := 1 + r*2

	foo := func(start int) int64 {

		m := 1 + (n-start+di-1)/di
		k64 := int64(k)

		A := make([]int64, m)

		A[0] = base[0]

		for i := 0; i < start; i++ {
			A[0] = min(A[0], base[i])
		}

		for i := start; i < n; i += di {
			curMin := base[i]
			for j := 1; j < di && i+j < n; j++ {
				curMin = min(curMin, base[i+j])
			}
			A[1+(i-start)/di] = curMin
		}

		sort.Slice(A, func(i, j int) bool {
			return A[i] < A[j]
		})

		fmt.Printf("%v\n", base)
		fmt.Printf("%v\n", A)

		ans := A[0]
		for i := 1; i < m; i++ {
			diff := A[i] - A[i-1]
			need := diff * int64(i)
			if k64 >= need {
				k64 -= need
				ans = A[i]
			} else {
				ans += k64 / int64(i)
				k64 = 0
				break
			}
		}

		if k64 > 0 {
			ans += k64 / int64(m)
		}

		return ans
	}

	var ans int64 = 0
	for i := 1; i <= di; i++ {
		ans1 := foo(i)
		println(ans1)
		ans = max(ans, ans1)
	}

	return ans
}
