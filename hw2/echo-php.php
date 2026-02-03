<?php
header('Content-Type: application/json');
$method = $_SERVER['REQUEST_METHOD'];
$data = array();
if ($method === 'GET' || $method === 'DELETE') {
    $data = $_GET;
} elseif ($method === 'POST' || $method === 'PUT') {
    $input = file_get_contents('php://input');
    $contentType = isset($_SERVER['CONTENT_TYPE']) ? $_SERVER['CONTENT_TYPE'] : '';
    if (str_contains($contentType, 'application/json')) {
        $data = json_decode($input, true);
    } else {
        parse_str($input, $data);
    }
}
$response = array(
    "echo" => "Echo - PHP",
    "method" => $method,
    "hostname" => $_SERVER['HTTP_HOST'],
    "date_time" => date('Y-m-d H:i:s'),
    "user_agent" => isset($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : 'N/A',
    "ip_address" => $_SERVER['REMOTE_ADDR'],
    "received_data" => $data
);
echo json_encode($response, JSON_PRETTY_PRINT);
?>
