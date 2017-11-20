ngSvw.directive('svwSegmentationValidation', function () {
  return {
    //restrict: 'AE',
    replace : true,
    scope: {
      data: '='
    },
    controller: 'ngSvwSegmentationValidationController as segvalidCtrl',
    templateUrl: '<div>test</div>'//'segmentation-validation/segmentation-validation.html',
  };
});