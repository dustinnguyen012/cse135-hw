<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Sessions - Page 2</title>
</head>
<body>
    <h1>PHP Sessions - Page 2</h1>

    <?php
    if (isset($_SESSION['username'])) {
        echo "<p><b>Name:</b> " . htmlspecialchars($_SESSION['username']) . "</p>";
        echo "<p>Your session is persisting across pages!</p>";
    } else {
        echo "<p><b>Name:</b> No session data found.</p>";
        echo "<p>Go back to Page 1 and enter a name first!</p>";
    }
    ?>

    <br>
    <p><a href="sessions-php-1.php">Go back to Session Page 1</a></p>
    <p><a href="sessions-php-destroy.php">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
