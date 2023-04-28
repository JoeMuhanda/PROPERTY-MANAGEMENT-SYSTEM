<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $name = $_POST['name'];
  $address = $_POST['address'];
  $owner_name = $_POST['owner_name'];

  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "property_management_system";

  // Create connectionreate connectionreate connectio
  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  // Add property to the sytem
  $sql = "INSERT INTO properties (name, address, owner_name) VALUES ('$name', '$address', '$owner_name')";
  if ($conn->query($sql) === TRUE) {
    header("Location: index.php");
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  // Close connection
  $conn->close();
}

?>

<!DOCTYPE html>
<html>
<head>
  <title>Add Property</title>
</head>
<body>
  <h1>Add Property</h1>
  <form method="post">
    <label>Name:</label>
    <input type="text" name="name">
    <br>
    <label>Address:</label>
    <input type="text" name="address">
    <br>
    <label>Owner Name:</label>
    <input type="text" name="owner_name">
    <br>
    <input type="submit" value="Add">
  </form>
</body>
</html>

