package p002

// Problem 2 - Even Fibonacci Numbers

func SumEvenFibonacciUntil(n int64) int64 {
	sum := int64(0)
	for fibn := range fibonacci(n) {
		if fibn&1 == 0 {
			sum += fibn
		}
	}
	return sum
}

func fibonacci(limit int64) <-chan int64 {
	fibs := make(chan int64)
	go func() {
		var i, j int64 = 1, 2
		fibs <- 1
		defer close(fibs)

		for j < limit {
			fibs <- j
			i, j = j, i+j
		}
	}()
	return fibs
}
