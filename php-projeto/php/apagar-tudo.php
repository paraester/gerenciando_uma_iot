 <?php 
	echo '<p>Trabalho de IOT</p>'; 
	
	print('apagando todas as lâmpadas ');
	
	
   
    $saida = exec('/usr/bin/python3 /var/www/html/toggle2-lightdown.py');
	
	echo $saida;
	
	
	echo '<p>Final</p>'; 
 ?>
