<?php
$ip = 'ip.txt';
$f = fopen($ip, 'a');
$ipaddress = $_SERVER["REMOTE_ADDR"];
$ref=$_SERVER["HTTP_REFERER"];
$today = date("m.d.Y");
fwrite($f, $ipaddress . " " . $today . "\n");
?>
