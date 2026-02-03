<?php
session_start();

// Save username if submitted
if (isset($_GET['username']) && $_GET['username'] !== '') {
    $_SESSION['username'] = $_GET['username'];
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Sessions - Page 1</title>
</head>
<body>
    <h1>PHP Sessions - Page 1</h1>

    <form action="sessions-php-1.php" method="GET">
        <label>Enter Your Name: <input type="text" name="username" value=""></label><br><br>
        <input type="submit" value="Save Name to Session">
    </form>

    <br><hr><br>

    <?php
    if (isset($_SESSION['username'])) {
        echo "<p><b>Name:</b> " . htmlspecialchars($_SESSION['username']) . "</p>";
    } else {
        echo "<p><b>Name:</b> You do not have a name set</p>";
    }
    ?>

    <br>
    <p><a href="sessions-php-2.php">Go to Session Page 2</a></p>
    <p><a href="sessions-php-destroy.php">Destroy Session</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>

