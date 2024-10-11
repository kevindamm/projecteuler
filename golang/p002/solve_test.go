package p002_test

import (
	"testing"

	"github.com/kevindamm/projecteuler/golang/p002"
)

func TestSumEvenFibonacciUntil(t *testing.T) {
	tests := []struct {
		name  string
		limit int64
		want  int64
	}{
		{"small", 100, 44},
		{"large", 1_000_000_000, 350704366},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := p002.SumEvenFibonacciUntil(tt.limit); got != tt.want {
				t.Errorf("SumEvenFibonacciUntil() = %v, want %v", got, tt.want)
			}
		})
	}
}
