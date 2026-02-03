<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>State - PHP - View Data</title>
</head>
<body>
    <h1>State Management - PHP</h1>
    <h2>View Saved Data</h2>

    <?php
    if (isset($_SESSION['name']) || isset($_SESSION['message'])) {
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><th>Field</th><th>Value</th></tr>";
        echo "<tr><td>Name</td><td>" . htmlspecialchars($_SESSION['name']) . "</td></tr>";
        echo "<tr><td>Message</td><td>" . htmlspecialchars($_SESSION['message']) . "</td></tr>";
        echo "<tr><td>Saved At</td><td>" . $_SESSION['saved_at'] . "</td></tr>";
        echo "</table>";
    } else {
        echo "<p>No data saved yet.</p>";
    }
    ?>

    <br>
    <p><a href="state-php-save.php">Go Back and Save/Clear Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
