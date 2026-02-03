<?php
header('Content-Type: application/json');

$response = array(
    "hello" => "Hello World!",
    "team_member" => "Dustin Nguyen",
    "language" => "PHP",
    "date_time" => date('Y-m-d H:i:s'),
    "ip_address" => $_SERVER['REMOTE_ADDR']
);

echo json_encode($response, JSON_PRETTY_PRINT);
?>
