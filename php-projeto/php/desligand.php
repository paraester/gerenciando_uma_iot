<?php 
    $parametro = (int) $_GET['id'];
   
    $saida = exec('/usr/bin/python3 /var/www/html/desligand.py', &$_GET('id'));
    echo $saida;

	
?>
