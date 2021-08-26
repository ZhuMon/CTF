<?php
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,"http://eens.ee.ncku.edu.tw:5006/index.php");
curl_setopt($ch,CURLOPT_HTTPHEADER,array(
    'CLIENT-IP:127.0.0.1',
    'X-FORWARDED-FOR:127.0.0.1'
    ));
curl_setopt($ch,CURLOPT_HEADER,0);//是否輸出header
$out = curl_exec($ch);
curl_close($ch);
?>
