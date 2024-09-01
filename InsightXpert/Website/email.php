<?php
// Enable error reporting for debugging
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $Fname = trim($_POST["first_name"]);
    $Lname = trim($_POST["last_name"]);
    $subject = trim($_POST["subject"]);
    $email = trim($_POST["email"]);
    $message = trim($_POST["message"]);

    // Basic validation
    if (empty($Fname) || empty($Lname) || empty($email) || empty($message)) {
        echo "Please fill in all fields.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Please provide a valid email address.";
    } else {
        // Set the recipient email address
        $to = "info@insightxpert.co.uk";

        // Set the email headers
        $headers = "From: $Fname $Lname <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Build the email content
        $emailContent = "Name: $Fname $Lname\n";
        $emailContent .= "Email: $email\n";
        $emailContent .= "Subject: $subject\n";
        $emailContent .= "Message: $message\n";

        // Try to send the email and handle errors
        if (mail($to, $subject ?: "Contact Form Submission", $emailContent, $headers)) {
            header("Location: index.html");            
            exit();
        } else {
            // Check for the last error
            $errorMessage = error_get_last()['message'];
            echo "Oops! Something went wrong. Please try again later. Error: " . $errorMessage;
        }
    }
}
?>
