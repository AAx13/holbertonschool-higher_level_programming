import Foundation

func longest_word(text: String) -> (String) {
    let split_string = text.componentsSeparatedByString(" ")
    var i = 0
    for i in split_string {
        if split_string[i].characters.count > split_string[i-1].characters.count {
            var highest = split_string[i]
        }
    }
    return highest
}