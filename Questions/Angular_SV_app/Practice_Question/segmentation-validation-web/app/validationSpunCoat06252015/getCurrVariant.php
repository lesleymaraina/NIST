<?php

	session_start();

	$mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$id = $_SESSION['sessionID'];

	$query = "SELECT * FROM currVariant WHERE id=$id";
	$result = $mysqli->query($query);
	$row = $result->fetch_assoc();
	$currVariant = substr($row["variant"], 8);

	$mysqli->close();

	echo $currVariant;
?>