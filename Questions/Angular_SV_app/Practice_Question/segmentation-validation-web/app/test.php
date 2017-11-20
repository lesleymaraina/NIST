<?php

	$mysqli = new mysqli("127.0.0.1", "root", "password", "responses");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$query = $mysqli->query("SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_SCHEMA='responses'");

	$row = mysqli_fetch_array($query);
	
	echo $row[0];
	
?>