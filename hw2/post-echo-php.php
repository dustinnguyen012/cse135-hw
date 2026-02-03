<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POST Echo - PHP</title>
</head>
<body>
    <h1>POST Echo - PHP</h1>

    <h2>Submit Data via POST</h2>
    <form action="post-echo-php.php" method="POST">
        <label>Name: <input type="text" name="name" value="Dustin"></label><br><br>
        <label>Message: <input type="text" name="message" value="Hello via POST!"></label><br><br>
        <input type="submit" value="Submit POST">
    </form>

    <hr>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        echo "<h2>Echoed Data:</h2>";
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><th>Key</th><th>Value</th></tr>";
        foreach ($_POST as $key => $value) {
            echo "<tr><td>" . htmlspecialchars($key) . "</td><td>" . htmlspecialchars($value) . "</td></tr>";
        }
        echo "</table>";

        echo "<h2>Request Info:</h2>";
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><td><b>Method</b></td><td>POST</td></tr>";
        echo "<tr><td><b>Hostname</b></td><td>" . $_SERVER['HTTP_HOST'] . "</td></tr>";
        echo "<tr><td><b>Date/Time</b></td><td>" . date('Y-m-d H:i:s') . "</td></tr>";
        echo "<tr><td><b>User Agent</b></td><td>" . $_SERVER['HTTP_USER_AGENT'] . "</td></tr>";
        echo "<tr><td><b>IP Address</b></td><td>" . $_SERVER['REMOTE_ADDR'] . "</td></tr>";
        echo "</table>";
    }
    ?>

    <br>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
