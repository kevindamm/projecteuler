package p0008

import "os"

func DigitSeries(filename string) digit_series {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	digits := make([]int, 0)
	for _, bytedata := range data {
		if bytedata >= '0' && bytedata <= '9' {
			digits = append(digits, int(bytedata-'0'))
		}
	}
	return digit_series(digits)
}

type digit_series []int

func (series digit_series) LargestAdjacentProduct(length int) int {
	largest := 0

	for seq := range series.SequencesOf(length) {
		product := seq[0]
		for _, digit := range seq[1:] {
			product *= digit
		}
		if product > largest {
			largest = product
		}
	}

	return largest
}

func (series digit_series) SequencesOf(length int) <-chan []int {
	channel := make(chan []int)

	go func() {
		defer close(channel)
		for i := range len([]int(series)) - length {
			channel <- []int(series)[i : i+length]
		}
	}()

	return channel
}
