

class Person {
    // Declaring all public attributes (task 0)
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

// Created protocol to be used with Mentor and Student to return if the Student or Mentor are students (task 1)
protocol Classify {
    func isStudent() -> Bool
}

// Created enum to describe what Mentor will be teaching (task 2)
enum Subject {
    case Math
    case English
    case French
    case History
}

// Defined two new sub-classes with the super class being Person (task 0)
// Implementation of the isStudent protocol within the subclass Mentor (task 1)
class Mentor: Person, Classify {
    // Declaring constant subject (task 2)
    let subject: Subject
    
    // Overloaded constructor (task 2)
    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }
    
    func isStudent() -> Bool {
        return false
    }
    // This function will return a String that relates to the subject a mentor is teaching (task 2)
    func stringSubject() -> String {
        return String(self.subject)
    }
}

// Implementation of the isStudent protocol within the subclass Mentor (task 1)
class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}

class School {
    // Declaring constructor for name (task 3)
    var name: String
    init(name: String) {
        self.name = name
    }
    
    // Declaring a public attribute: an array of Person (task 3)
    var list_persons: [Person!] = []

    // This function will add to the attribute list_persons only if its a Student (task 3)
    func addStudent(p: Person) -> Bool {
        if p is Student {
            list_persons.append(p)
            return true
        }
        return false
    }
    
    // This function will add to the attribute list_persons only if its a Mentor (task 3)
    func addMentor(p: Person) -> Bool {
        if p is Mentor {
            list_persons.append(p)
            return true
        }
        return false
    }
}

