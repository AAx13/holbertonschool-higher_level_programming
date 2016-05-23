#!/usr/bin/swift
func is_palindrome(my_string: String) -> (Bool) {
    let string = my_string
    var rev = ""
    
    for i in string.characters {
        let c = "\(i)"
        rev += c
    }
    return (string == rev)
}

// This script will return True if a string is a palindrome. False otherwise.