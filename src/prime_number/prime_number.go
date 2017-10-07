package prime_number

import (
	"math"
)

// Returns first prime numbers of given quantity
func Find(quantity uint) []uint {
	var counter, i uint = 0, 2
	prime_numbers := make([]uint, quantity)
	for ; counter < quantity; i++ {
		if isPrime(i) {
			prime_numbers[counter] = i
			counter++
		}
	}
	return prime_numbers
}

// Detects if given number is prime
func isPrime(num uint) bool {
	var i uint = 2
	for ; i <= uint(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}
