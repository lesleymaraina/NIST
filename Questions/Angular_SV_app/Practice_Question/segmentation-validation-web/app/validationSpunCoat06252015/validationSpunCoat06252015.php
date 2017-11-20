<?php

	session_start();
	
	if(!isset($_SESSION['sessionID'])){
		echo "You must be logged in to access this page.";
		exit;
	}

?>

<style type="text/css">

    .carousel .item{
        min-height: 280px; /* Prevent carousel from being distorted if for some reason image doesn't load */
    }

    .carousel .item img{
        margin: 0 auto; /* Align slide image horizontally center */
    }

    .carousel .carousel-control{ 
    	visibility: hidden;
    }
    
	.carousel:hover .carousel-control{ 
		visibility: visible;
	}

	ol.carousel-indicators li.active {
  		background: #387AB6;
	}

</style>

<div ng-controller="ValidationSpunCoat06252015Ctrl" class="container">

<div class="row">

	<div class="row" style="width:100%;">

		<h1>Structural Variant Analysis</h1>

	</div>

</div>

<div class="row" style="width:100%; height:32px;">

	<div style="float:right;">

		<a href="#"><button type="button" class="btn btn-default btn-sm" onclick="
		// logs out of PHP session
		var xhr2 = new XMLHttpRequest();
		xhr2.open('GET', 'validationSpunCoat06252015/logout.php');
		xhr2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
						
		xhr2.send();

		// xhr2.onreadystatechange = function() {
		// 	if(xhr2.readyState === 4){
		// 		console.log('done logging out');
				
		// 	}
		// }

		gapi.load('auth2', function() {

			gapi.auth2.init({
				client_id: '741055934806-20ii9alv5fa6rnk8cp7qqmce8sntt06j.apps.googleusercontent.com'
			}).then(function(auth2) {

				auth2.signOut().then(function () {
				    // window.location.replace('index.php#logout');
				});    
				auth2.disconnect();
			})
		});
		
		// may have to timeout for longer
		setTimeout(function() {
			window.location.replace('index.php#logout');
		}, 1500)
		" style="color:gray; height:100%; width:auto; margin-left: 50px;"> Sign out </button></a>

	</div>

	<div style="float:right;"">

		<?php echo "<p style='margin-top:10%;'>" . $_SESSION['sessionName'] . "</p>" ?></div>

		<img src="<?php echo $_SESSION['sessionImageURL']; ?>" ng-init="importAllDatabases(); changeImage(<?php echo getCurrVariant() ?>)" style="float:right; height:100%; width:auto; margin-right:10px;"/>
		
	</div>

<div class="row">

	<!-- left side before row -->
	<div style="float:left; width:50%; padding-right: 2%;">

		<div style="margin-bottom:2.5%;">

			<label>Variant: </label> <a href = "#">{{currentViewGetVariant_1.name}}</a>

			<!-- previous, next buttons -->
			<button type="submit" class="btn btn-default btn-sm" ng-click="previous('currentViewGetVariant_1');" ng-disabled="currentViewGetVariant_1.index==0" style="color: gray; margin-left: 5%; margin-right:2.5%;"> <
			</button>

		    <button id="nextButton" type="submit" class="btn btn-default btn-sm" ng-click="next('currentViewGetVariant_1', 'getvariant_1');" style="color:gray; margin-left: 2.5%;"> >
		    </button>

	    </div>

		<progressbar value="currentViewGetVariant_1.index + 1" max="getvariant_1.size">
			<i>{{currentViewGetVariant_1.index + 1}} / {{getvariant_1.size}}</i>
		</progressbar>

		<div id="carousel" class="carousel slide" data-ride="carousel" data-interval="0">

	        <div class="carousel-inner" style="width:100%; height:550px;">
	            <div class="item active">
	                <a href="{{currentViewGetVariant_1.path}}";><img ng-src="{{currentViewGetVariant_1.path}}" style="float:left; max-height:32.3%; width:49%; border:1px solid gray; margin-right: 1%; margin-bottom: 1%;" data-lity class="img-thumbnail"></a>

	                <a href="{{currentViewGetVariant_2.path}}";><img ng-src="{{currentViewGetVariant_2.path}}" style="float:right; max-height:49%; width:49%; border:1px solid gray; margin-left: 1%; margin-bottom: 1%;" data-lity class="img-thumbnail"></a>
	                
	                <a href="{{currentViewGetVariant_3.path}}";><img ng-src="{{currentViewGetVariant_3.path}}" style="float:left; max-height:32.3%; width:49%; border:1px solid gray; margin-top: 1%; margin-right: 1%; padding-bottom: 1%;" data-lity class="img-thumbnail"></a>

	                <a href="{{currentViewGetVariant_4.path}}";><img ng-src="{{currentViewGetVariant_4.path}}" style="float:right; max-height:49%; width:49%; border: 1px solid gray; margin-top: 1%; margin-left: 1%;" data-lity class="img-thumbnail"></a>
	                
	                <a href="{{currentViewGetVariant_5.path}}";><img ng-src="{{currentViewGetVariant_5.path}}" style="float:left; max-height:32.3%; width:49%; border:1px solid gray; margin-top: 1%; margin-right:1%;" data-lity class="img-thumbnail"></a>
	            </div>
	            <div class="item">
	                <a href="{{currentViewGetVariant_1.path}}";><img ng-src="{{currentViewGetVariant_1.path}}" style="max-width:100%; max-height:100%;" data-lity class="img-thumbnail"></a>
	            </div>
	            <div class="item">
	                <a href="{{currentViewGetVariant_2.path}}";><img ng-src="{{currentViewGetVariant_2.path}}" style="max-width:100%; max-height:100%;" data-lity class="img-thumbnail"></a>
	            </div>
	            <div class="item">
	                <a href="{{currentViewGetVariant_3.path}}";><img ng-src="{{currentViewGetVariant_3.path}}" style="max-width:100%; max-height:100%;" data-lity class="img-thumbnail"></a>
	            </div>
	            <div class="item">
	                <a href="{{currentViewGetVariant_4.path}}";><img ng-src="{{currentViewGetVariant_4.path}}" style="max-width:100%; max-height:100%;" data-lity class="img-thumbnail"></a>
	            </div>
	            <div class="item">
	                <a href="{{currentViewGetVariant_5.path}}";><img ng-src="{{currentViewGetVariant_5.path}}" style="max-width:100%; max-height:100%;" data-lity class="img-thumbnail"></a>
	            </div>
	        </div>

	        <!-- controls -->
	        <a ng-non-bindable class="carousel-control left" href="#carousel" data-slide="prev" style="background-image:none;">
	            <span class="glyphicon glyphicon-chevron-left" style="color:#387AB6;"></span>
	        </a>
	        <a ng-non-bindable class="carousel-control right" href="#carousel" data-slide="next" style="background-image:none;">
	            <span class="glyphicon glyphicon-chevron-right" style="color:#387AB6;"></span>
	        </a>

	        <ol class="carousel-indicators" style="bottom:-50px;">

	            <li data-target="#carousel" data-slide-to="0" class="active" style="list-style-position:inside; border:1px solid gray;"></li>
	            <li data-target="#carousel" data-slide-to="1" style="list-style-position:inside; border:1px solid gray;"></li>
	            <li data-target="#carousel" data-slide-to="2" style="list-style-position:inside; border:1px solid gray;"></li>
	            <li data-target="#carousel" data-slide-to="3" style="list-style-position:inside; border:1px solid gray;"></li>
	            <li data-target="#carousel" data-slide-to="4" style="list-style-position:inside; border:1px solid gray;"></li>
	            <li data-target="#carousel" data-slide-to="5" style="list-style-position:inside; border:1px solid gray;"></li>
	        </ol>

	    </div>
        
  	</div>

  	<!-- right side before responses -->
  	<div style="float:left; width:50%; overflow-y:auto; overflow-x:hidden; height:500px; padding-left: 2.5%;">

  		<div style="width:50%; float:left;">
  			<div class="row" style="height: 250px; margin:0; padding-right:2.5%;" ng-repeat="element in getquestion.questions" ng-if="$even">

				<h4>{{element.question}}</h4>

				<div ng-repeat="response in element" ng-if="$index > 0">
					<div class="radio">
						<label><input type="radio" name="q{{$parent.$parent.$index + 1}}" ng-click="pressResponse($parent.$parent.$index + 1, $index);">{{response}}</label>
					</div>
				</div>
  			</div>
  		</div>

  		<div style="width:50%; float:right;">
  			<div class="row" style="height: 250px; margin:0;" ng-repeat="element in getquestion.questions" ng-if="$odd">

				<h4>{{element.question}}</h4>

				<div ng-repeat="response in element" ng-if="$index > 0">

					<div class="radio">
						<label><input type="radio" name="q{{$parent.$parent.$index + 1}}" ng-click="pressResponse($parent.$parent.$index + 1, $index);">{{response}}</label>
					</div>
				</div>

  			</div>  
  		</div>
  		
  	</div>
  	
  	<div style="float:right; width:50%; padding-left:2.5%; height:250px;">
  		<div class="row" style="margin:0;">
	  		<div class="row">
				<h1>Responses</h1>
			</div>
			<div class="row">
				<a id="downloadbtn" href ="" class="btn btn-default btn-lg" ng-click="pressDownloadCsv();"
	                >
	            Download CSV
	        </a>
	         <button class="btn btn-default btn-lg" ng-click="displayCsv = !displayCsv; getDataString_2();">Display Responses</button>
			</div>

	        <div class="row">

	        	<br>

				<div collapse="displayCsv" style="width:100%; word-wrap:break-word; overflow-y:auto; overflow-x:hidden; max-height:100px;">
					<div ng-repeat="segmentation in getvariant_1.segmentations">

						{{segmentation.name}}

						<!-- prints all responses for question -->
						<div ng-repeat="status in segmentation" ng-if="$index > 1">
							<p style="display:inline;">&emsp;Question {{$index - 1}}: {{status}}</p> 
						</div>

					</div>
				</div>

			</div>
		</div>
  	</div>

</div>

  	<?php
  		function getCurrVariant() {
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

			return $currVariant - 1;
  		}
  	?>

</div>
