// Collect information
function showValue() {
    // Get the value of the input & select element from front end "insurance_estimator.html"
    var client_age = document.getElementById("age").value;
    var children_no = document.getElementById("children").value
    var bmi = document.getElementById("bmi").value
    var gender = document.getElementById("gender").value
    var smoker = document.getElementById("smoker").value
    var medical_history = document.getElementById("medical_history").value
    var family_medical_history = document.getElementById("family_medical_history").value
    var exercise_frequency = document.getElementById("exercise_frequency").value
    var occupation = document.getElementById("occupation").value
    var coverage_level = document.getElementById("coverage_level").value
    
    // get dummy data for gender
    var male;
    var female;
    if (gender === "Male") {
        male = 1;
        female = 0;
    } else {
        male = 0;
        female = 1;
    }

    // get dummy data for smoker
    var Yes;
    var No;
    if (smoker === "Yes") {
        Yes = 1;
        No = 0;
    } else {
        Yes = 0;
        No = 1;
    }

    // get dummy data for medical_history & family_medical_history
    var Diabetes;
    var Heart_disease;
    var High_blood_pressure;
    var None;
    var Family_Diabetes;
    var Family_Heart_disease;
    var Family_High_blood_pressure;
    var Family_None;

    if (medical_history === "Diabetes") {
        Diabetes = 1;
        Heart_disease = 0;
        High_blood_pressure = 0;
        None = 0;
    } else if (medical_history === "Heart disease"){
        Diabetes = 0;
        Heart_disease = 1;
        High_blood_pressure = 0;
        None = 0;
    } else if (medical_history === "High blood pressure") {
        Diabetes = 0;
        Heart_disease = 0;
        High_blood_pressure = 1;
        None = 0;
    } else {
        Diabetes = 0;
        Heart_disease = 0;
        High_blood_pressure = 0;
        None = 1;
    }

    if (family_medical_history === "Diabetes") {
        Family_Diabetes = 1;
        Family_Heart_disease = 0;
        Family_High_blood_pressure = 0;
        Family_None = 0;
    } else if (family_medical_history === "Heart disease"){
        Family_Diabetes = 0;
        Family_Heart_disease = 1;
        Family_High_blood_pressure = 0;
        Family_None = 0;
    } else if (family_medical_history === "High blood pressure") {
        Family_Diabetes = 0;
        Family_Heart_disease = 0;
        Family_High_blood_pressure = 1;
        Family_None = 0;
    } else {
        Family_Diabetes = 0;
        Family_Heart_disease = 0;
        Family_High_blood_pressure = 0;
        Family_None = 1;
    }

    // get dummy data for exercise_frequency
    var Frequently;
    var Occasionally;
    var Rarely;
    var exercise_Never;

    if (exercise_frequency === "Frequently") {
        Frequently = 1;
        Occasionally = 0;
        Rarely = 0;
        exercise_Never = 0;
    } else if (exercise_frequency === "Occasionally"){
        Frequently = 0;
        Occasionally = 1;
        Rarely = 0;
        exercise_Never = 0;
    } else if (exercise_frequency === "Rarely") {
        Frequently = 0;
        Occasionally = 0;
        Rarely = 1;
        exercise_Never = 0;
    } else {
        Frequently = 0;
        Occasionally = 0;
        Rarely = 0;
        exercise_Never = 1;
    }

    // get dummy data for occupation
    var Blue_collar;
    var White_collar;
    var Student;
    var Unemployed;

    if (occupation === "Blue collar") {
        Blue_collar = 1;
        White_collar = 0;
        Student = 0;
        Unemployed = 0;
    } else if (occupation === "White collar"){
        Blue_collar = 0;
        White_collar = 1;
        Student = 0;
        Unemployed = 0;
    } else if (occupation === "Student") {
        Blue_collar = 0;
        White_collar = 0;
        Student = 1;
        Unemployed = 0;
    } else {
        Blue_collar = 0;
        White_collar = 0;
        Student = 0;
        Unemployed = 1;
    }

    //get dummy data for coverage level
    var Premium;
    var Standard;
    var Basic;

    if (coverage_level === "Premium") {
        Premium = 1;
        Standard = 0;
        Basic = 0;
    } else if (coverage_level === "Standard"){
        Premium = 0;
        Standard = 1;
        Basic = 0;
    } else {
        Premium = 0;
        Standard = 0;
        Basic = 1;
    }

    // list client data
    var client_data = {
        "age": client_age,
        "female": female,
        "male": male,
        "bmi": bmi,
        "children": children_no,
        'Yes': Yes,
        'No': No,
        'Diabetes': Diabetes,
        'Heart_disease': Heart_disease,
        'High_blood_pressure': High_blood_pressure,
        'None': None,
        'Family_Diabetes': Family_Diabetes,
        'Family_Heart_disease': Family_Heart_disease,
        'Family_High_blood_pressure': Family_High_blood_pressure,
        'Family_None': Family_None,
        'Frequently': Frequently,
        'exercise_Never': exercise_Never,
        'Occasionally': Occasionally,
        'Rarely': Rarely,
        'exercise_Never': exercise_Never,
        'Blue_collar': Blue_collar,
        'Student': Student,
        'Unemployed': Unemployed,
        'White_collar': White_collar,
        'Basic': Basic,
        'Premium': Premium,
        'Standard': Standard
    } 

    // Display the value in an alert box
    alert(JSON.stringify(client_data)) ;

} 
  

  
