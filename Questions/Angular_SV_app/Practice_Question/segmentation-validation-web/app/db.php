<?php
  require_once '../../vendor/autoload.php';

  // Get $id_token via HTTPS POST.
  $id_token = $_POST['id_token'];
  $name = $_POST['name'];
  $imageURL = $_POST['imageURL'];

  $client = new Google_Client(['client_id' => $CLIENT_ID]);
  $payload = $client->verifyIdToken($id_token);

  if ($payload) {

    $userid = $payload['sub'];

    session_start();

    // session variables
    $_SESSION["sessionID"] = $userid;
    $_SESSION["sessionName"] = $name;
    $_SESSION["sessionImageURL"] = $imageURL;

    $mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

    if($db->connect_errno > 0)
      die('Unable to connect to database [' . $db->connect_error . ']');

    $query = "INSERT IGNORE INTO currVariant (id) VALUES ($userid)";
    $mysqli->query($query);

    $query_2 = $mysqli->query("SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_SCHEMA='responses'");

    $row = mysqli_fetch_array($query_2);
      
    for($i = 1; $i <= $row[0] - 1; $i++) {

      $variant = 'variant_' . $i;

      $newQuery = "INSERT IGNORE INTO $variant (id) VALUES ($userid)";
      $mysqli->query($newQuery);

    }

    $mysqli->close();
    
  } else {

    echo "invalid id";

  }

?>