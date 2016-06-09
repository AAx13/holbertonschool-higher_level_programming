//
//  Entity.swift
//  TechCompanies
//
//  Created by Konflict on 6/8/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

// Declaring an enum
enum EntityType:String {
    case None
    case School
    case TechCompany
}

class Entity {
    
    // Declaring private attributes
    private (set) var name:String
    private (set) var town:String
    private (set) var imageName:String
    private (set) var type:EntityType
    
    // Initializing
    init (name:String, town:String, imageName:String, type:EntityType = .None) {
        
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
    
}