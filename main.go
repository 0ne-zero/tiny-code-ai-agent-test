package main

import "fmt"

// add returns the sum of two integers.
func add(a, b int) int {
	return a + b
}

// minus returns the difference of two integers.
func minus(a, b int) int {
	return a - b
}

func main() {
	resultAdd := add(10, 5)
	fmt.Printf("Addition: 10 + 5 = %d\n", resultAdd)

	resultMinus := minus(10, 5)
	fmt.Printf("Subtraction: 10 - 5 = %d\n", resultMinus)
}
