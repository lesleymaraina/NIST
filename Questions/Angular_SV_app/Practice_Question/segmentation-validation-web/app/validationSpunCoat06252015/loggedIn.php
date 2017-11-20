<?php
	
	// checks if user is logged in
	session_start();

	if(!isset($_SESSION['sessionID'])){
		echo "out";
		exit;
	}

	echo "in";
?>