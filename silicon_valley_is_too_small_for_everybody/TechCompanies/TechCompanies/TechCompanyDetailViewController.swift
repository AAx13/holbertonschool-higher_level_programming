//
//  TechCompanyDetailViewController.swift
//  TechCompanies
//
//  Created by Konflict on 6/8/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class TechCompanyDetailViewController: UIViewController {
    
    var entity:Entity! = nil
    @IBOutlet weak var label_entity: UILabel!
    @IBOutlet weak var image_entity: UIImageView!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        if entity != nil {
            // Set view controller title to entity name
            self.title = entity.name
            // Set the label_entity text to the entity town
            self.label_entity.text = entity.town
            // Set the image_entity image to the right image depending of the entity
            self.image_entity.image = UIImage(imageLiteral: entity.imageName)
            self.image_entity.contentMode = UIViewContentMode.ScaleAspectFit
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
