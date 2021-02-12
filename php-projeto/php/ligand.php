<?php
    $parametro = (int) $_GET['id'];
   
    $saida = exec("/usr/bin/python3 /var/www/html/ligand.py $parametro");
    echo $saida;
  
?>