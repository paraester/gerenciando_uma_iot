 <?php 
echo '<p>Trabalho de IOT</p>'; 

print('As lâmpadas abaixo estão acesas: ');

$saida = exec("/usr/bin/python3 /var/www/html/ledstatus-all.py");
echo " $saida"; 	


echo '<p>Final</p>'; 
 ?>
