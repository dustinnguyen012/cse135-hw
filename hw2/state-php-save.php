<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['clear'])) {
        session_destroy();
        header('Location: state-php-view.php');
        exit;
    }
    $_SESSION['name'] = isset($_POST['name']) ? $_POST['name'] : '';
    $_SESSION['message'] = isset($_POST['message']) ? $_POST['message'] : '';
    $_SESSION['saved_at'] = date('Y-m-d H:i:s');
    header('Location: state-php-view.php');
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>State - PHP - Save Data</title>
</head>
<body>
    <h1>State Management - PHP</h1>
    <h2>Save Your Data</h2>

    <form action="state-php-save.php" method="POST">
        <label>Name: <input type="text" name="name" value=""></label><br><br>
        <label>Message: <input type="text" name="message" value=""></label><br><br>
        <input type="submit" value="Save Data">
    </form>

    <br>

    <form action="state-php-save.php" method="POST">
        <input type="hidden" name="clear" value="true">
        <input type="submit" value="Clear Data">
    </form>

    <br>
    <p><a href="state-php-view.php">View Saved Data</a></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
