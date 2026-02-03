<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environment Variables - PHP</title>
</head>
<body>
    <h1>Environment Variables</h1>
    <p><strong>Language:</strong> PHP</p>
    <table border="1" cellpadding="5">
        <tr>
            <th>Variable</th>
            <th>Value</th>
        </tr>
        <?php
        foreach ($_SERVER as $key => $value) {
            if (is_string($value)) {
                echo "<tr><td>$key</td><td>$value</td></tr>";
            }
        }
        ?>
    </table>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>

