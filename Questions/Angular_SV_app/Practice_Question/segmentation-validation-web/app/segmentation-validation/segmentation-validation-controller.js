(function () {
	'use strict';

	
	ngSvw.controller('ngSvwSegmentationValidationController', ngSvwSegmentationValidationController);
	
	ngSvwSegmentationValidationController.$inject = ['$stateParams', '$scope', 'ui-bootstrap'];

    function ngSvwSegmentationValidationController($stateParams, $scope, 'ui-bootstrap') {
        
        $scope.validationForm = {
        		data: {}
        };
        
        console.log("coucou");
        //$scope.spuncoat07072015 = validationServiceSpunCoat07072015.getSpunCoat07072015();
        
        $scope.displayCsv = true;
        
        $scope.currentView = {
        		index: 0,
        		path:$scope.data.segmentations[0].path,
        		name:$scope.data.segmentations[0].name
        };
        
        $scope.next = function () {
        	if($scope.currentView.index < ($scope.spuncoat07072015.size-1))
        	{
        		$scope.currentView.index = $scope.currentView.index + 1;
        		$scope.data.segmentations.currentImage = $scope.currentView.index;
        		$scope.currentView.path = $scope.data.segmentations[$scope.currentView.index].path;
        		$scope.currentView.name = $scope.data.segmentations[$scope.currentView.index].name;
        	}
        	console.log($scope.currentView);
        }
        
        $scope.previous = function () {
        	if($scope.currentView.index > 0)
        	{
        		$scope.currentView.index = $scope.currentView.index - 1;
        		$scope.data.segmentations.currentImage = $scope.currentView.index;
        		$scope.currentView.path = $scope.data.segmentations[$scope.currentView.index].path;
        		$scope.currentView.name = $scope.data.segmentations[$scope.currentView.index].name;
        	}
        }
        
        $scope.pressGood = function () {
        	$scope.data.segmentations[$scope.currentView.index].status="good";
        }
        
        $scope.pressCorrect = function () {
        	$scope.data.segmentations[$scope.currentView.index].status="correct";
        }
        
        $scope.pressInaccurate = function () {
        	$scope.data.segmentations[$scope.currentView.index].status="inaccurate";
        }
        
        $scope.pressMissed = function () {
        	$scope.data.segmentations[$scope.currentView.index].status="missed";
        }
        
        $scope.pressDownloadCsv = function () {
            
            var csvContent = "data:text/csv;charset=utf-8,";
            $scope.data.segmentations.forEach(function(infoArray, index){

               var dataString = infoArray.name + "," + infoArray.status;
               csvContent += index < $scope.data.segmentations.length ? dataString+ "\n" : dataString;

            }); 
            
            var encodedUri = encodeURI(csvContent);
            var link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", $scope.data.name + ".csv");
            document.body.appendChild(link);
            
            if (link.download !== undefined) {
				link.setAttribute("download", $scope.data.name + ".csv"));
			} else {
				link.setAttribute("target", "_blank");
			}
			link.setAttribute("style", "visibility:hidden");

            link.click(); // This will download the data file named $scope.data.name + ".csv").
        }
        
        
        
    }
}());