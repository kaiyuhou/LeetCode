package main

import (
	"container/heap"
	"strconv"
)

func main() {
	// event1 := []string{"01:15", "02:00"}
	// event2 := []string{"02:00", "03:00"}
	// nums := []int{10, 10, 10, 10, 10}
	// k := 5
	// println(maxKelements(nums, k))
	s1 := "a"
	s2 := "bb"
	println(isItPossible(s1, s2))
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

// c

func isItPossible(word1 string, word2 string) bool {
	cntF := func(w string) map[int]int {
		ans := make(map[int]int)
		for _, v := range w {
			ans[int(v)] += 1
		}
		return ans
	}

	C1 := cntF(word1)
	C2 := cntF(word2)

	// fmt.Println(C1, C2)

	checkF := func() bool {
		ans1, ans2 := 0, 0
		for _, v := range C1 {
			if v > 0 {
				ans1 += 1
			}
		}
		for _, v := range C2 {
			if v > 0 {
				ans2 += 1
			}
		}
		return ans1 == ans2
	}

	for i := int('a'); i <= int('z'); i++ {
		for j := int('a'); j <= int('z'); j++ {
			if C1[i] == 0 || C2[j] == 0 {
				continue
			}
			C1[i] -= 1
			C1[j] += 1
			C2[i] += 1
			C2[j] -= 1
			if checkF() {
				return true
			}
			C1[i] += 1
			C1[j] -= 1
			C2[i] -= 1
			C2[j] += 1
		}
	}
	return false
}

// b

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
	h := &IntHeap{}
	for _, v := range nums {
		heap.Push(h, -v)
	}

	var ans int64 = 0
	for i := 0; i < k; i++ {
		cur := heap.Pop(h).(int)
		ans += int64(-cur)
		cur = (cur - 2) / 3
		heap.Push(h, cur)
	}

	return ans
}

// a

func maximumCount(nums []int) int {
	pos, neg := 0, 0
	for _, v := range nums {
		if v > 0 {
			pos += 1
		}
		if v < 0 {
			neg += 1
		}
	}
	if pos > neg {
		return pos
	}
	return neg
}
