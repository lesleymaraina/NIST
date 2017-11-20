(function () {
    'use strict';
    
    angular.module('ngSvw.validationSpunCoat06252015', ['ngRoute', 'ui.bootstrap'])
    
    .config(['$routeProvider', function($routeProvider) {
      $routeProvider.when('/validationSpunCoat06252015', {
        templateUrl: 'validationSpunCoat06252015/validationSpunCoat06252015.html',
        controller: 'ValidationSpunCoat06252015Ctrl'
      });
    }])
    
    .controller('ValidationSpunCoat06252015Ctrl', ValidationSpunCoat06252015Ctrl);
    
    ValidationSpunCoat06252015Ctrl.$inject = ['$stateParams', 'validationServiceSpunCoat06252015', '$scope'];

    function ValidationSpunCoat06252015Ctrl($stateParams, validationServiceSpunCoat06252015, $scope) {
        
        var vm = this;
        vm.validation = null;
        
        $scope.displayJson = false;
        
        $scope.validationForm = {
            data: {}
        };

        $scope.getquestion = validationServiceSpunCoat06252015.getQuestion();
        $scope.getvariant_1 = validationServiceSpunCoat06252015.getVariant_1();
        $scope.getvariant_2 = validationServiceSpunCoat06252015.getVariant_2();
        $scope.getvariant_3 = validationServiceSpunCoat06252015.getVariant_3();
        $scope.getvariant_4 = validationServiceSpunCoat06252015.getVariant_4();
        $scope.getvariant_5 = validationServiceSpunCoat06252015.getVariant_5();
        
        $scope.displayCsv = true;

        $scope.currentViewGetVariant_1 = {
            index: 0,
            path:$scope.getvariant_1.segmentations[0].path
        };

        $scope.currentViewGetVariant_2 = {
            index: 0,
            path:$scope.getvariant_2.segmentations[0].path
        };

        $scope.currentViewGetVariant_3 = {
            index: 0,
            path:$scope.getvariant_3.segmentations[0].path
        };

        $scope.currentViewGetVariant_4 = {
            index: 0,
            path:$scope.getvariant_4.segmentations[0].path
        };

        $scope.currentViewGetVariant_5 = {
            index: 0,
            path:$scope.getvariant_5.segmentations[0].path
        };

        $scope.importDatabase = function(responses_array, variantNumber) {

            var variantObj = $scope.getvariant_1.segmentations;

            for(var i = 0; i < responses_array.length; i++)
                variantObj[variantNumber - 1]['status_q' + (i + 1)] = $scope.getquestion.questions[i]["response" + responses_array[i]];

            $scope.disableButton();
        }

        $scope.disableButton = function() {

            // last variant reached
            if($scope.currentViewGetVariant_1.index==($scope.getvariant_1.size-1)){
                document.getElementById("nextButton").disabled = true;
                return;
            }

            var qObject = $scope.getvariant_1.segmentations[$scope.currentViewGetVariant_1.index];

            // loop through # of questions
            for(var i = 1; i <= $scope.getquestion.numQuestions; i++){

                if(qObject["status_q" + i] === undefined){
                    document.getElementById("nextButton").disabled = true;
                    return;
                }
            }

            document.getElementById("nextButton").disabled = false;
        }

        $scope.importAllDatabases = function() {

            // loop for all variants
            for(var i = 1; i <= $scope.getvariant_1.size; i++)
                $scope.getResponses($scope.importDatabase, i);
        }

        $scope.checkNext = function (responses_array) { 

            for(var i = 0; i < responses_array.length; i++){

                // not all questioned answered
                if(responses_array[i].length === 0){
                    alert("Answer all questions before proceeding");
                    return;
                }
            }   

            // updates images, questions accordingly
            $scope.next("currentViewGetVariant_1", "getvariant_1");
        }

        $scope.setNextQuestion = function(toAdd) {

            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'validationSpunCoat06252015/setNextQuestion.php');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.send("toAdd=" + toAdd);
        }

        // next/previous images
        $scope.next = function (currentView, spuncoat) {

            if($scope[currentView].index < ($scope[spuncoat].size-1)){
                $scope.changeImage(1);
                $scope.setNextQuestion(1);
            }
        }
        
        $scope.previous = function (currentView) {
            if($scope[currentView].index > 0){
                $scope.changeImage(-1);
                $scope.setNextQuestion(-1);
            }
        }

        // helper function for next and previous
        $scope.changeImage = function (indexAdjust) {

            $scope.currentViewGetVariant_1.index = $scope.currentViewGetVariant_1.index + indexAdjust;
            $scope.currentViewGetVariant_1.path = $scope.getvariant_1.segmentations[$scope.currentViewGetVariant_1.index].path;
            $scope.currentViewGetVariant_1.name = $scope.getvariant_1.segmentations[$scope.currentViewGetVariant_1.index].name;

            // loops for all images
            for(var i = 2; i <= $scope.getvariant_1.numImages; i++) {
                var currentView = "currentViewGetVariant_" + i;
                var spuncoat = "getvariant_" + i;

                $scope[currentView].index = $scope[currentView].index + indexAdjust;
                $scope[currentView].path = $scope[spuncoat].segmentations[$scope[currentView].index].path;
            }

            $scope.getResponses($scope.changeQuestion, $scope.currentViewGetVariant_1.index + 1);
        }

        $scope.changeQuestion = function(responses_array) {

            clearResponses();
            
            // loop through all questions
            for(var i = 1; i <= $scope.getquestion.numQuestions; i++){

                // unanswered
                if(responses_array[i - 1].length === 0)
                    continue;

                var radioButtons = document.getElementsByName("q" + i);

                radioButtons[responses_array[i - 1] - 1].checked = true;
            }

            $scope.disableButton();
        }

        $scope.getResponses = function(callback, variantNumber) {

            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'validationSpunCoat06252015/importResponses.php');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.send("variantNumber=" + variantNumber);

            var responses_array;

            xhr.onreadystatechange = function() {
                if(xhr.readyState === 4){
                    responses_array = xhr.responseText.split(",");
                    callback(responses_array, variantNumber);
                }
            }
        }
        
        // unchecks responses
        function clearResponses () {

            for(var i = 1; i <= $scope.getquestion.numQuestions; i++){

                var radioButtons = document.getElementsByName("q" + i);

                for(var j = 0; j < radioButtons.length; j++)
                    radioButtons[j].checked = false;
            }
        }

        $scope.pressResponse = function (question, response) {

            var toChange = "status_q" + question;

            var variant = $scope.currentViewGetVariant_1.index + 1;

            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'validationSpunCoat06252015/saveResponse.php');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.send("variant=" + variant + "&qNumber=" + question + "&response=" + response);

            $scope.getvariant_1.segmentations[variant - 1]["status_q" + question] = $scope.getquestion.questions[question - 1]["response" + response];
            
            $scope.disableButton();
        }
        
        // assumes no commas in responses
        // edit exclude array
        $scope.pressDownloadCsv = function () {

            var csvContent = "data:text/csv;charset=utf-8,";

            $scope.getvariant_1.segmentations.forEach(function(infoArray, index){
                
                var dataString = infoArray.name;

                angular.forEach(infoArray, function(status, varName){
                    var exclude = ['name', 'path', '$$hashKey'];

                    if(!exclude.includes(varName))
                        dataString += "," + status;
                });

                csvContent += index < $scope.getvariant_1.segmentations.length ? dataString+ "\n" : dataString;
            }); 
            
            var encodedUri = encodeURI(csvContent);
            var link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "structuralVariantAnalysis.csv");
            document.body.appendChild(link);
            
            if (link.download !== undefined)
                link.setAttribute("download", "structuralVariantAnalysis.csv");
            else
                link.setAttribute("target", "_blank");

            link.setAttribute("style", "visibility:hidden");

            link.click(); // This will download the data file named "structuralVariantAnalysis.csv".
        }
    }
}());