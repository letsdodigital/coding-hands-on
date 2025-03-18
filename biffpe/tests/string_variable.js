// Storing a patient's name (String)
let patientName = "Alice Wonderland"; 

// Storing a patient's temperature (Number)
let temperature = 98.6; 

// Storing a patient's allergy status (Boolean)
let hasAllergy = true; 

// Displaying the information in the console (for demonstration)
console.log("Patient Name: " + patientName);
console.log("Temperature: " + temperature);
console.log("Has Allergy: " + hasAllergy);


// Demonstrating changing a variable's value
temperature = 100.2; // Updating the temperature
console.log("Updated Temperature: " + temperature); 


// Demonstrating combining variables with text
let message = patientName + " has a temperature of " + temperature + " degrees.";
console.log(message);

// test function
function final_message(patientName, temperature) {
    return patientName + " has a temperature of " + temperature + " degrees.";
}

module.exports = final_message;