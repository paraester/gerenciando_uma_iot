 <?php 
echo '<p>Trabalho de IOT</p>'; 
	
print('acendendo todas as lâmpadas: ');
   
$saida = exec("/usr/bin/python3 /var/www/html/toggle2-lightup.py");
echo $saida;

 ?>
