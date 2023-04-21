<!-- property_management_system/index.php -->

<?php

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "property_management_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get properties
$sql = "SELECT * FROM properties";
$result = $conn->query($sql);
$properties = array();
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $properties[] = $row;
  }
}

// Close connection
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

<!-- property_management_system/add_property.php -->

<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $name = $_POST['name'];
  $address = $_POST['address'];
  $owner_name = $_POST['owner_name'];

  $servername = "localhost";
  $username = "username";
  $password = "password";
  $dbname = "property_management_system";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  // Add property
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

<!-- property_management_system/view_property.php -->

<?php

$id = $_GET['id'];

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "property_management_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get property
$sql = "SELECT * FROM properties WHERE id = $id";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
  $
