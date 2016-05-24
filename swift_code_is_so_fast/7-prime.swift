import Foundation

func is_prime(number: Int) -> (Bool)
{
    var i = 2
    while i <= number - 1 {
        if(number % i == 0) {
        return false
        }
        i += 1
    }
    if(i == number) {
        return true
    }
    return false
}

// This script will check a number and return True if its prime