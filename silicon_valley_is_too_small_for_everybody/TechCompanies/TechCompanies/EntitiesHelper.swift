//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Konflict on 6/8/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class EntitiesHelper {
    
    // Declare two static variables to hold list of school and list of tech company
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    // Declare static function to get list of schools and return them
    static func getSchools() -> [Entity]! {
        
        if listOfSchool.isEmpty {
            listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
        
        return listOfSchool
    }
    
    // Declare static function to get list of tech companies and return them
    static func getTechCompanies() -> [Entity]! {
        
        if listOfTechCompany.isEmpty {
            listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
        
        return listOfTechCompany
    }
}