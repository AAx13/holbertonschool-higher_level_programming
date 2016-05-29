//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//
//  Created by Konflict on 5/28/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class TechCompaniesHelper {
    
    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
    
    static func getTechCompanies() -> [String] {
        return companies
    }
}