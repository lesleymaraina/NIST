<?php
	
	session_start();

	$variantNumber = $_POST['variantNumber'];

	$mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$variant = 'variant_' . $variantNumber;
	$id = $_SESSION['sessionID'];

	// current variant
	$query = "SELECT * FROM $variant WHERE id=$id";
	$result = $mysqli->query($query);
	$row = $result->fetch_assoc();

	for($i = 1; $i < count($row) - 1; $i++)
		$toEcho .= $row['q' . $i] . ',';

	$toEcho .= $row['q' . (count($row) - 1)];
	
	// $toEcho .= $row['q' . (count($row) - 1)];

	echo $toEcho;

	$mysqli->close();
?>