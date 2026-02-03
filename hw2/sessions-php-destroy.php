<?php
session_start();
session_destroy();
header('Location: sessions-php-1.php');
exit;
?>
