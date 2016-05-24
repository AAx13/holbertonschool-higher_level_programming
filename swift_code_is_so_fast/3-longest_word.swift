import Foundation

func longest_word(text: String) -> (String) {
    let split_string = text.componentsSeparatedByString(" ")
    let max = split_string.maxElement({$1.characters.count > $0.characters.count})
    return max!
}

// This script takes a sentence turns it into an array of strings and returns the longest word in the array