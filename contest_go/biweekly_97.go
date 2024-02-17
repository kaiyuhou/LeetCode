package main

import (
	"fmt"
	"sort"
)

func main() {
	P := []int{1, 1, 2, 2, 3, 3, 5}
	k := 2
	fmt.Println(maximizeWin(P, k))
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maximizeWin(P []int, k int) int {
	dp := make([]int, len(P)+1)
	ans := 0
	j := 0
	for i := range P {
		for P[j] < P[i]-k {
			j++
		}
		dp[i+1] = max(dp[i], i-j+1)
		ans = max(ans, i-j+1+dp[j])
	}
	return ans
}

func maxCount(banned []int, n int, maxSum int) int {
	last := 0
	ans := 0
	sum := 0
	banned = append(banned, n+1)
	sort.Slice(banned, func(i, j int) bool { return banned[i] < banned[j] })
	for _, b := range banned {
		for cur := last + 1; cur < b; cur++ {
			if sum+cur > maxSum {
				goto end
			}
			if cur > n {
				goto end
			}
			ans++
			sum += cur
		}
		last = b
	}

end:
	return ans
}

func separateDigits(nums []int) []int {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}

	ret := []int{}
	for _, a := range nums {
		for ; a > 0; a /= 10 {
			ret = append(ret, a%10)
		}

	}

	for i, j := 0, len(ret)-1; i < j; i, j = i+1, j-1 {
		ret[i], ret[j] = ret[j], ret[i]
	}

	return ret
}
