//
//  ViewController.swift
//  Tapper
//
//  Created by Konflict on 5/26/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var taps_done = 0
    var taps_requested:Int? = 0
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    
    
    // This function will be called once button_play is clicked
    @IBAction func clickPlayButton(sender: AnyObject) {
        
        // Convert string to integer
        self.taps_requested = Int(self.textfield_number.text!)
        
        // Ensure input is bigger than 0 and is not nil
        if taps_requested > 0 && taps_requested != nil {
            print ("Let's do \(taps_requested) taps")
            // Call initGame
            initGame()
        }
    }

    // This function will be called once button_coin is clicked
    @IBAction func clickCoinButton(sender: AnyObject) {
        // Increase the value of taps_done by one
        taps_done += 1
        
        // Check value of taps_done
        if taps_done >= taps_requested {
            resetGame()
        }
        
        // Update label_taps to display the value of taps_done
        self.label_taps.text = String(self.taps_done) + "Taps !"
        
        // Print in the console "Tap!"
        print ("Tap!")
    }
    
    func initGame() {
        // Hide: image_tapper, button_play and textfield_number
        self.image_tapper.hidden = true
        self.button_play.hidden = true
        self.textfield_number.hidden = true
        
        // Show: label_taps, button_play
        self.label_taps.hidden = false
        self.button_coin.hidden = false
        
        // Reset taps_done to 0
        taps_done = 0
        
        // Set the value of label_taps to "0 Taps"
        self.label_taps.text = String(self.taps_done) + "Taps !"
    }
    
    func resetGame() {
        //Hide: label_taps and button_coin
        self.label_taps.hidden = true
        self.button_coin.hidden = true
        
        //Show: image_tapper, button_play and `textfield_number
        self.image_tapper.hidden = false
        self.button_play.hidden = false
        self.textfield_number.hidden = false
        
        //Reset taps_requested to 0
        taps_requested = 0
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        taps_requested = 0
        taps_done = 0
        
        //Hide: label_taps and button_coin
        self.label_taps.hidden = true
        self.button_coin.hidden = true
        
        //Show: image_tapper, button_play and `textfield_number
        self.image_tapper.hidden = false
        self.button_play.hidden = false
        self.textfield_number.hidden = false
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

