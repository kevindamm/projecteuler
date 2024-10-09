package main

import "fmt"

const N = 1000

func main() {
	sum := 0
	for i := range N {
		if i%5 == 0 || i%3 == 0 {
			sum += i
		}
	}
	fmt.Println(sum)
}
