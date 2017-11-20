<?php

	$toAdd = $_POST['toAdd'];

	session_start();

	$mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$id = $_SESSION['sessionID'];

	// getCurrVariant
	$query = "SELECT * FROM currVariant WHERE id=$id";
	$result = $mysqli->query($query);
	$row = $result->fetch_assoc();
	$currVariant = substr($row["variant"], 8);

	$table = "variant_" . ($currVariant + $toAdd);

	$query_2 = "UPDATE currVariant SET variant = '$table' WHERE id=$id";
	$mysqli->query($query_2);

	$mysqli->close();
?>
