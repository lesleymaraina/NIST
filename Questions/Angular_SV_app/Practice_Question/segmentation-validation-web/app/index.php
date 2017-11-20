<?php
	session_start();
?>

<!DOCTYPE html>

<html>

<head>

	<!-- edit clientID -->
	<meta name="google-signin-client_id" content="741055934806-20ii9alv5fa6rnk8cp7qqmce8sntt06j.apps.googleusercontent.com">

  	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
  	<title>SVCurator</title>
    <meta name="description" content="SVCurator">

  	<link rel="icon" href="https://isg.nist.gov/deepzoomweb/resources/img/favicon.ico;jsessionid=21CE77F2344B143AD8BF5B4A4F06CCA0" type="image/x-icon">

	<link rel="stylesheet" type="text/css" href="libs/nist-layout/css/reset.css" media="screen">
	<link rel="stylesheet" type="text/css" href="libs/nist-layout/css/main_style.css" media="screen">
	<link rel="stylesheet" type="text/css" href="libs/nist-layout/css/layout.css" media="screen">
	<link rel="stylesheet" type="text/css" href="libs/nist-layout/css/bootstrap.css">

	<script type="text/javascript" language="javascript" src="libs/nist-layout/site.js"></script>

	<!-- TODO : This script should be removed. -->
	<script type="text/javascript" src="libs/nist-layout/holder.js"></script>

	<script src="https://apis.google.com/js/platform.js" async defer></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.js"></script>

</head>

<body id="menu1">

<div class="container">

  <div class="row">

    <a href="http://www.nist.gov/index.html"><img src="img/bg_header_gradient.png" alt="National Institute of Standards and Technology" width="970"/></a>

    <div id="menuContainer">

      <ul id="menu">

      	<!-- navigation tab id connected to highlight feature, don't change -->
        <li><a id="menu1nav" href="index.php">Home</a></li>
		<li><a id="menu2nav" href="indexCell.html" style="display:none">Structural Variant Analysis</a></li>
		<li><a id="menu3nav" href="pages/docs/onlineHelp.html">Help</a></li>

      </ul>

    </div>

  </div>

</div>

<script>

	window.onload = function(){
		
		var xhr = new XMLHttpRequest();
		xhr.open('GET', 'validationSpunCoat06252015/loggedIn.php');
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

		xhr.send();

		xhr.onreadystatechange = function() {

			if(xhr.readyState === 4){

				// show/hide elements based on login status
				if(xhr.responseText === "in"){
					document.getElementById('menu2nav').style.display="inline";
					document.getElementById('signInButton').style.display="none";
					document.getElementById('signOutButton').style.display="table";
				}

			}

		}

		// after logging out from form page
	    if(window.location.hash === "#logout"){

	      	// removes hash from URL
	      	history.pushState("", "", window.location.href.split('#')[0]);

	    }
	}

	function isLoggedIn(){

		// determines whether user is signed in
		var request = new XMLHttpRequest();
	    request.open('POST', 'validationSpunCoat06252015/loggedIn.php');
	    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

	    request.send();

	    request.onreadystatechange = function() {

	        if(request.readyState === 4){

	            if(request.responseText.localeCompare("in") === 0)
	            	return;
	            else
	            	onSignIn();
	        }

	    }
	}

	function onSignIn() {

		var auth2 = gapi.auth2.getAuthInstance();
		var googleUser = auth2.currentUser.get();

		// starts PHP session
		var xhr = new XMLHttpRequest();
		xhr.open('POST', 'db.php');
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
				
		var profile = googleUser.getBasicProfile();

		var id_token = googleUser.getAuthResponse().id_token;
		var name = profile.getName();
		var imageURL = profile.getImageUrl();

		xhr.send("id_token=" + id_token + "&name=" + name + "&imageURL=" + imageURL);

		// redirect
		xhr.onreadystatechange = function() {

			if(xhr.readyState === 4)
				window.location.replace("indexCell.html#/validationSpunCoat06252015");

		}
	}	

	function signOut() {

		var auth2 = gapi.auth2.getAuthInstance();

		auth2.signOut().then(function () {
			console.log('User signed out.');
		});

		auth2.disconnect();

		// logs out of PHP session
	    var xhr2 = new XMLHttpRequest();
		xhr2.open('GET', 'validationSpunCoat06252015/logout.php');
		xhr2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
				
		xhr2.send();

		xhr2.onreadystatechange = function() {
			if(xhr2.readyState === 4)
				window.location.reload();
		}

	}

</script>

<div class="container">

  <div class="row">

	<div class="col-xs-12">

    	<div class="row" style="width:100%">

        <h1 style="text-align:center">Welcome to SVCurator!</h1>

        <p>An app that facilitates in efficient manual curation of structural variants. The Genome in a Bottle Consortium is developing strategies for integrating candidate SV and large indel calls >=20bp to form a benchmark set of structural variant (SV) calls. Machine learning methods are being developed to form benchmark calls. ‘Ground truth’ or labeled data is needed to train the machine learning models. In order to efficiently generate labeled data points, we have developed this web-based app for manual curation of SVs. 
		</p>

		<p>The app displays images and survey questions for deletions and insertions for each member of the Ashkenazi Jewish trio [HG002-son, HG003-father, HG004-mother]. The app includes an image panel or ‘carousel’ that allows users to scroll through the following images for each variant: svviz images for each technology [Ill_250bp, Ill_300x, Mate Pair, PacBio, 10X], svviz dotplots, IGV and gEVAL images. 
		</p>

		<div id="signInButton" class="g-signin2" data-onsuccess="isLoggedIn" data-width="240" data-height="50" data-longtitle="true" style="display:inline; display:table; margin: 0 auto;"></div>

		<a href="#" onclick="signOut();"><button id="signOutButton" type="button" class="btn btn-default btn-sm" style="display:none; margin: 0 auto; color:gray; width:240px; height:50px; font-size: 1.15em;"> Sign out </button></a>

		<br>

      	</div>

    </div>

  </div>

</div>

<!-- Footer Starts-->
<div class="container">
  <div class="row footer">
    <div class="col-xs-12">
      <p>
        The National Institute of Standards and Technology (NIST) is
        an agency of the
        <a href="http://commerce.gov">U.S. Department of Commerce</a>.
      </p>

      <p>
        <a href="http://nist.gov/public_affairs/privacy.cfm">
          Privacy policy / security notice / accessibility statement</a>
        /
        <a href="http://nist.gov/public_affairs/disclaimer.cfm">
          Disclaimer</a>
        /
        <a href="http://nist.gov/director/foia/">
          Freedom of Information Act (FOIA)</a>
        /
        <a href="http://nist.gov/director/civil/nofearpolicy.cfm">
          No Fear Act Policy</a>
        /
        <a href="http://nist.gov/director/quality_standards.cfm">
          NIST Information Quality Standards</a>
        /
        <a href="http://nist.gov/public_affairs/envpolicy.cfm">
          Environmental Policy Statement</a>
      </p>

    </div>
  </div>

  <div class="row">
    <div class="col-xs-12"><strong>Date created:</strong> September 23, 2016 | <strong>Last
      updated:</strong>
      <script type="text/javascript">
        if(document.lastModified != 'undefined') { document.write(format_date_mmmddyy(document.lastModified)); }
      </script>
    </div>
  </div>
</div>

<!-- Footer Ends-->

   <script src="libs/nist-layout/analytics.js" async=""></script>

	 <script>
		(function(i, s, o, g, r, a, m) {
			i['GoogleAnalyticsObject'] = r;
			i[r] = i[r] || function() {
				(i[r].q = i[r].q || []).push(arguments)
			}, i[r].l = 1 * new Date();
			a = s.createElement(o), m = s.getElementsByTagName(o)[0];
			a.async = 1;
			a.src = g;
			m.parentNode.insertBefore(a, m)
		})(window, document, 'script',
				'//www.google-analytics.com/analytics.js', 'ga');

		ga('create', 'UA-45172783-4', 'nist.gov');
		ga('send', 'pageview');
	</script>

</body>
</html>
