#!/usr/bin/swift
func fibonacci(number: Int) -> (Int) {
    var i = 0, x = 1
    for _ in 0..<number {
        let temp = i
        i = x
        x = temp + x
    }
    return i
    
}

// This script will calculate the fibonacci sequence up to the number given and return the value