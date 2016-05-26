

class Person {
    // declaring all public attributes (task 0)
    var first_name: String
    var last_name: String
    var age: Int
    
    // Initializing all public attributes (task 0)
    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    
    // This function will join and return the first name and last name of the 'Person' provided (task 0)
    func fullName() -> String {
        return self.first_name + " " + self.last_name
    }
    
}

protocol Classify {
    func isStudent() -> Bool
}

// Defined two new sub-classes with the super class being Person (task 0)
// Implementation of the isStudent protocol within the subclass Mentor (task 1)
class Mentor: Person, Classify {
    func isStudent() -> Bool {
        return false
    }
}

// Implementation of the isStudent protocol within the subclass Mentor (task 1)
class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}

