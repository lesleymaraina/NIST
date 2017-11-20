<?php
	
	// checks if user is logged in
	function testSet() {

		session_start();

		echo $_SESSION['sessionID'];
		
		if(!isset($_SESSION['sessionID'])){
			echo "out";
			exit;
		}

		echo "in";
	}
	
?>