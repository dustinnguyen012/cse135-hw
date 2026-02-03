<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello HTML - PHP</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p><strong>Team Member:</strong> Dustin Nguyen</p>
    <p><strong>Language:</strong> PHP</p>
    <p><strong>Date/Time:</strong> <?php echo date('Y-m-d H:i:s'); ?></p>
    <p><strong>Your IP:</strong> <?php echo $_SERVER['REMOTE_ADDR']; ?></p>
    <p><a href="/">Back to Homepage</a></p>
</body>
</html>
