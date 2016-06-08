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
    private var name:String
    private var town:String
    private var imageName:String
    private var type:EntityType
    
    // Initializing
    init (name:String, town:String, imageName:String, type:EntityType = .None) {
        
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
    
}