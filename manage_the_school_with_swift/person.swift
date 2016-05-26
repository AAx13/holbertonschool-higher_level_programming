

class Person {
    // declaring all public attributes
    var first_name: String
    var last_name: String
    var age: Int
    
    // Initializing all public attributes
    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    
    // This function will join and return the first name and last name of the 'Person' provided
    func fullName() -> String {
        return self.first_name + " " + self.last_name
    }
    
}

