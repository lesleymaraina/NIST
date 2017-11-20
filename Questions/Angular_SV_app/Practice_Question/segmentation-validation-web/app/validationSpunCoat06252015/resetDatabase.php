<?php
	
	$file = file_get_contents('validation-service-SpunCoat06252015.js');

	// file not found
	if(!$file)
		exit;

	// retrieves var numQuestions
	$numQuestionsPos = strpos($file, "numQuestions");
	$afterNumQuestions = substr($file, $numQuestionsPos + 14);
	$commaPos = strpos($afterNumQuestions, ",");

	$numQuestions = substr($afterNumQuestions, 0, $commaPos);

	// retrieves var numVariants
	$sizePos = strpos($file, "size:");
	$afterSize = substr($file, $sizePos + 6);
	$commaPos_2 = strpos($afterSize, ",");

	// ok
	$numVariants = substr($afterSize, 0, $commaPos_2);

	$mysqli = new mysqli("127.0.0.1", "root", "password");

	if($mysqli->connect_errno) {
		printf("Connect failed: %s\n", $mysqli->connect_error);
		exit();
	}

	$dbName = 'responses';

	$mysqli->query("DROP DATABASE $dbName");

	$mysqli->query("CREATE DATABASE $dbName");
	$mysqli->query("USE $dbName");

	$mysqli->query("CREATE TABLE currVariant (id VARCHAR(256), variant VARCHAR(16))");
	$mysqli->query("ALTER TABLE currVariant ADD UNIQUE (id)");
	$mysqli->query("ALTER TABLE currVariant ALTER variant SET DEFAULT 'variant_1'");

	// numVariants
	for($i = 1; $i <= $numVariants; $i++){

		$tableName = "variant_" . $i;

		$mysqli->query("CREATE TABLE $tableName (id VARCHAR(256))");
		$mysqli->query("ALTER TABLE $tableName ADD UNIQUE (id)");

		echo '$i:' . $i;
		// numQuestions
		for ($j = 1; $j <= $numQuestions; $j++){

			$colName = "q" . $j;

			$mysqli->query("ALTER TABLE $tableName ADD COLUMN $colName VARCHAR(128)");
		}
	}


?>