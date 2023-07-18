<?php
$Nom = $_POST['Nom'];
$Prenom = $_POST['Prenom'];
$phone = $_POST['phone'];
$email = $_POST['email'];
$Adresse = $_POST['Adresse'];   
$Ville = $_POST['Ville'];
$Code_postal = $_POST['Code_postal'];
$mot_de_passe = $_POST['mot_de_passe'];

//Connection a la base de donnees
$conn = new mysqli("localhost","root","","nouveau_client");
if ($conn->connect_error) 
{
    die("Connection failed: ". $conn->connect_error);
} else {
    $stmt =$conn-> prepare("insert into nouveaux_client(Nom,Prenom,phone,email,Adresse,Ville)values(?,?,?,?,?,?)");
    $stmt->bind_param("sssssi",$Nom,$Prenom,$phone,$email,$Adresse,$Ville);
    $execval=$stmt->execute();
    echo "Bienvenue Au Quai antique, allons reserver une table";
    $stmt->close();
    $conn->close();
}
?>