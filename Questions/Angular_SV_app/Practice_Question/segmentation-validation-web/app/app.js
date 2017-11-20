(function () {
	'use strict';
	
	angular.module('ngSvw', [
	  'ngSvw.config',
	  
	  //'ngRoute',
	  'ui.router',
	  'angular-hal',
	  //'fg', 
	  
	  
	  //'ngSvw.ngSvwSegmentationValidation',
	  
	  'ngSvw.validationSpunCoat06252015',
	  'ngSvw.validationServiceSpunCoat06252015',

	])
	
	.config(['$stateProvider', '$urlRouterProvider',
	            function ($stateProvider, $urlRouterProvider) {

	                $urlRouterProvider.otherwise('/validationSpunCoat06252015');

	                $stateProvider
	                    .state('validationSpunCoat06252015', {
	                        url: '/validationSpunCoat06252015',
	                        templateUrl: 'validationSpunCoat06252015/validationSpunCoat06252015.php',
	                        controller: 'ValidationSpunCoat06252015Ctrl',
	                        controllerAs: 'vmSpunCoat06252015'
	                    })
	            }])
	            
//	.config(function(fgConfigProvider, FgField) {
//		var category = 'Features 2D Matlab';
//		  var fieldTemplate = new FgField('appFeatureInput', {
//		    displayName: 'Contrast',
//		    feature: {
//				id : 'Feature2DMatlab_Contrast',
//				name : 'Contrast',
//				parameters : [ {
//					id : 'Feature2DMatlab_Contrast_NumLevels',
//					name : 'Number of levels',
//					value : '8'
//				}, {
//					id : 'Feature2DMatlab_Contrast_DistanceOffset',
//					name : 'Distance offset',
//					value : '1'
//				} ]
//			} ,
//		  });
//
//		  var templateUrl = 'common/features-fg-custom-fields/fg-field-custom-feature.ng.html';
//		  var propertiesUrl = 'common/features-fg-custom-fields/fg-properties-custom-feature.ng.html';
//
//		  fgConfigProvider.fields.removeAll();
		 // fgConfigProvider.fields.add(fieldTemplate, category, templateUrl, propertiesUrl);
		
//	})
	
    .run(['$rootScope', '$state', '$stateParams', 'halClient', 
          function ($rootScope, $state, $stateParams, halClient
              ) {
              $rootScope.$state = $state;
              $rootScope.$stateParams = $stateParams;

              
              $rootScope.client = halClient;
              //$rootScope.apiRoot = halClient.$get($rootScope.baseUrl);
              //editableOptions.theme = 'bs3'; // bootstrap3 theme.
              
//              $rootScope.paletteFeaturesUrls = paletteFeaturesUrls;
//              $rootScope.FgField = FgField;
          }]);
	
}());
