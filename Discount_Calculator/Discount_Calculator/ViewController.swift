import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    // Outlet for the item price text field
    @IBOutlet weak var itemp_price_text_fild: UITextField!
    
    // Outlet for displaying custom percentage label
    @IBOutlet weak var Custum_percent_text_filed: UILabel!
    
    // Outlet for displaying discount label
    @IBOutlet weak var Discount_text_filed: UILabel!
    
    // Outlet for displaying final price label
    @IBOutlet weak var final_price_text_filed: UILabel!
    
    // Action for segmented control value change
    @IBAction func discount_segment_bar(_ sender: UISegmentedControl){
        // Defining discount percentage for each segment
        // let discountPercentages: [Float] = [0.1, 0.15, 0.18, 0.25]
        // Calling the calculateDiscount method
        // calculateDiscount(discountPercentage: discountPercentages[sender.selectedSegmentIndex])
    }
    
    // Action for slider value change
    @IBAction func slide_bar(_ sender: UISlider) {
        // Retrieve slider value
        let sliderValue = sender.value
        let roundedValue = Int(round(sliderValue))
        // Update custom percentage label
        self.Custum_percent_text_filed.text = "\(roundedValue)%"
        let floateSliderValue = sliderValue / 100
        let roundedSliderValue = (floateSliderValue * 100).rounded() / 100
        // Calling the calculateDiscount method
        calculateDiscount(discountPercentage: roundedSliderValue)
    }
    
    // Action for reset button
    @IBAction func Rest_everything_button(_ sender: Any) {
        // Set the segment index to 0
        if let segmentControl = view.viewWithTag(1) as? UISegmentedControl {
            segmentControl.selectedSegmentIndex = 0
        }
        // Set the custom slider to 25%
        if let slider = view.viewWithTag(2) as? UISlider {
            slider.value = 25.0
            // Trigger the slide_bar action to update the UI
            slide_bar(slider)
        }
        // Clear the item price field
        itemp_price_text_fild.text = ""
        // Reset the discount and final price text fields to default values
        Discount_text_filed.text = "0%"
        final_price_text_filed.text = "$0.00"
    }

    // Action for calculate button
    @IBAction func calculateButtonPressed(_ sender: Any) {
        // Retrieve the actual UISegmentedControl instance
        if let segmentControl = view.viewWithTag(1) as? UISegmentedControl {
            // Retrieve the value entered by the user
            if let originalPriceStr = itemp_price_text_fild.text, !originalPriceStr.isEmpty {
                // Retrieve the selected sale % value based on segmented control
                let selectedSegmentIndex = segmentControl.selectedSegmentIndex
                let discountPercentages: [Float] = [0.1, 0.15, 0.18, 0.25]
                if selectedSegmentIndex >= 0 && selectedSegmentIndex < discountPercentages.count {
                    let selectedDiscountPercentage = discountPercentages[selectedSegmentIndex]
                    if selectedSegmentIndex == 3 {
                        // Enable slider if the third segment is selected
                        enableSlider(true)
                    } else {
                        // Disable slider for other segments
                        enableSlider(false)
                    }
                    // Calculate the discount and update UI
                    calculateDiscount(discountPercentage: selectedDiscountPercentage)
                }
            } else {
                // If empty, set discount and final price to empty strings
                self.Discount_text_filed.text = ""
                self.final_price_text_filed.text = ""
                // Show error message
                let alert = UIAlertController(title: "Error", message: "The item price is empty. Please fill in the item price field.", preferredStyle: .alert)
                alert.addAction(UIAlertAction(title: "Ok", style: .default, handler: nil))
                self.present(alert, animated: true, completion: nil)
            }
        } else {
            // Handle the case where UISegmentedControl is not found
            // You may want to show an alert or handle it accordingly
        }
    }

    // Function to enable or disable the slider
    func enableSlider(_ isEnabled: Bool) {
        // Enable or disable the slider based on the specified value
        if let slider = view.viewWithTag(2) as? UISlider {
            slider.isEnabled = isEnabled
        }
    }

    // Function to calculate the discount
    func calculateDiscount(discountPercentage: Float) {
        // Retrieving the value entered by the user
        if let originalPriceStr = itemp_price_text_fild.text,
           let originalPrice = Float(originalPriceStr), originalPrice > 0 {
            // Calculating the discounted price
            let discountedPrice = originalPrice * (1 - discountPercentage)
            self.Discount_text_filed.text = "\(Int(discountPercentage * 100))%"
            let roundedDiscountedPrice = (discountedPrice * 100).rounded() / 100
            self.final_price_text_filed.text = "$\(roundedDiscountedPrice)"
        }
    }
}
