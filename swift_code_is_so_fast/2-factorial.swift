#!/usr/bin/swift
func factorial(N: Int) -> (Int) {
    var i = N
    var count = N
    if N == 0 {
        return(0)
    }
    while count != 1 {
        i = i * (count - 1)
        count -= 1
    }
    return(i)
}

// This script will calculate the factorial of a given number and return it