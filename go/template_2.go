package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {

	// code ...

	w.Flush()
}

func I(format string, a ...interface{}) {
	fmt.Fscanf(r, format, a...)
}

func O(format string, a ...interface{}) {
	fmt.Fprintf(w, format, a...)
}

func solve() {
	var n int

	I("%d\n", &n)

	a := make([]int, n)

	for i := 0; i < n; i++ {
		I("%d", &a[i])
	}
	I("\n")

	// solve the problem ...
}

func main() {
	var t int

	I("%d\n", &t)

	for t > 0 {
		solve()
		t--
	}

	writer.Flush()
}
