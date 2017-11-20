<?php
	
	$variant = $_POST['variant'];
	$qNumber = $_POST['qNumber'];
	$response = $_POST['response'];

	session_start();

	$mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$variant = "variant_" . $variant;
	$q = "q" . $qNumber;
	$id = $_SESSION['sessionID'];

	$query = "UPDATE $variant SET $q = '$response' WHERE id=$id";
	$mysqli->query($query);

	$mysqli->close();
?>