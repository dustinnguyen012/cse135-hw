<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>General Echo - PHP</title>
</head>
<body>
    <h1>General Echo - PHP</h1>

    <h2>Submit Data</h2>
    <form action="general-echo-php.php" method="POST">
        <label>Method:
            <select name="method">
                <option value="GET">GET</option>
                <option value="POST" selected>POST</option>
            </select>
        </label><br><br>
        <label>Name: <input type="text" name="name" value="Dustin"></label><br><br>
        <label>Message: <input type="text" name="message" value="Hello General Echo!"></label><br><br>
        <input type="submit" value="Submit">
    </form>

    <hr>

    <?php
    $method = $_SERVER['REQUEST_METHOD'];
    $data = array();

    if ($method === 'GET') {
        $data = $_GET;
    } elseif ($method === 'POST') {
        $input = file_get_contents('php://input');
        $contentType = isset($_SERVER['CONTENT_TYPE']) ? $_SERVER['CONTENT_TYPE'] : '';

        if (str_contains($contentType, 'application/json')) {
            $data = json_decode($input, true);
        } else {
            $data = $_POST;
        }
    }

    if (!empty($data)) {
        echo "<h2>Echoed Data:</h2>";
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><th>Key</th><th>Value</th></tr>";
        foreach ($data as $key => $value) {
            echo "<tr><td>" . htmlspecialchars($key) . "</td><td>" . htmlspecialchars($value) . "</td></tr>";
        }
        echo "</table>";

        echo "<h2>Request Info:</h2>";
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><td><b>Method</b></td><td>" . $method . "</td></tr>";
        echo "<tr><td><b>Hostname</b></td><td>" . $_SERVER['HTTP_HOST'] . "</td></tr>";
        echo "<tr><td><b>Date/Time</b></td><td>" . date('Y-m-d H:i:s') . "</td></tr>";
        echo "<tr><td><b>User Agent</b></td><td>" . $_SERVER['HTTP_USER_AGENT'] . "</td></tr>";
        echo "<tr><td><b>IP Address</b></td><td>" . $_SERVER['REMOTE_ADDR'] . "</td></tr>";
        echo "<tr><td><b>Content Type</b></td><td>" . (isset($_SERVER['CONTENT_TYPE']) ? $_SERVER['CONTENT_TYPE'] : 'N/A') . "</td></tr>";
        echo "</table>";
    }
    ?>

    <br>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
