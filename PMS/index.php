<?php

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "property_management_system";

// Connecting databse with  the server

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// This will get thed properties of PMS in the databasee 

$sql = "SELECT * FROM properties";
$result = $conn->query($sql);
$properties = array();
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $properties[] = $row;
  }
}

// Close server connection
$conn->close();

?>

<!DOCTYPE html>
<html>
<head>
  <title>Property Management System</title>
</head>
<body>
  <h1>Properties</h1>
  <?php foreach ($properties as $property): ?>
    <h2><?= $property['name'] ?></h2>
    <p><?= $property['address'] ?></p>
    <p><?= $property['owner_name'] ?></p>
    <a href="view_property.php?id=<?= $property['id'] ?>">View Property</a>
  <?php endforeach ?>
</body>
</html>
