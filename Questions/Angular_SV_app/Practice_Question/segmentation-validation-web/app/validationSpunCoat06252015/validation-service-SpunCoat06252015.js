 (function () {
    'use strict';

    angular.module('ngSvw.validationServiceSpunCoat06252015', [])
        .factory('validationServiceSpunCoat06252015', validationServiceSpunCoat06252015);

    validationServiceSpunCoat06252015.$inject = ['$rootScope', '$q'];

    function validationServiceSpunCoat06252015($rootScope, $q) {

        var service = {
        	getQuestion : getQuestion,
        	getVariant_1 : getVariant_1,
        	getVariant_2 : getVariant_2,
            getVariant_3 : getVariant_3,
            getVariant_4 : getVariant_4,
            getVariant_5 : getVariant_5,
        };
        return service;

        function getQuestion() {
        	var data = {
	        	numQuestions: 4,
	    		questions: [
        			{
        				question: "How confident are you that the variant call is accurate (<=5bp different from the true variant)?",
						response1: "5 - very confident it is accurate",
						response2: "4",
						response3: "3",
						response4: "2",
						response5: "1 - very confident it is wrong"
        			},
        			{
        				question: "Is there a variant that is >5bp different from the candidate variant call and >=20bp in size?",
						response1: "Yes",
						response2: "No",
						response3: "Not sure"
        			},
        			{
        				question: "What is the genotype (if there is a variant >=20bp different from the candidate variant call, select its genotype)?",
						response1: "Homozygous Variant",
						response2: "Heterozygous",
						response3: "Homozygous Reference",
						response4: "Two or more different variants >=20bp in this region (e.g. compound heterozygous)"
        			},
        			{
        				question: "How confident are you in the genotype?",
						response1: "5 - very confident",
						response2: "4",
						response3: "3",
						response4: "2",
						response5: "1 - very unclear"
        			}
				]        	
			}
        	return data;
        }

        function getVariant_1() {
        	var data = {
	        	size: 3,
	        	numImages: 5,
	    		segmentations: [
					{
						name: "del_1_56831106_21",
						path: "data/SpunCoat-06252015/250bp_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg",
						status_q1: "unanswered",
						status_q2: "unanswered",
						status_q3: "unanswered",
						status_q4: "unanswered"
					},
					{
						name: "ins_9_108906616_13.jpg",
						path: "data/SpunCoat-06252015/250bp_ins_9_108906616_13.jpg",
						status_q1: "unanswered",
						status_q2: "unanswered",
						status_q3: "unanswered",
						status_q4: "unanswered"
					},
					{
						name: "test",
						path: "data/SpunCoat-06252015/250bp_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg",
						status_q1: "unanswered",
						status_q2: "unanswered",
						status_q3: "unanswered",
						status_q4: "unanswered"
					}
				]        	
			}
        	return data;
        }

        function getVariant_2() {
        	var data = {
	    		segmentations: [
					{
						path: "data/SpunCoat-06252015/pacbio_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					},
					{
						path: "data/SpunCoat-06252015/pacbio_ins_9_108906616_13.jpg"
					},
					{
						path: "data/SpunCoat-06252015/pacbio_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					}
				]        	
			}
			return data;
        }

        function getVariant_3() {
        	var data = {
	    		segmentations: [
					{
						path: "data/SpunCoat-06252015/10x_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					},
					{
						path: "data/SpunCoat-06252015/10x_ins_9_108906616_13.jpg"
					},
					{
						path: "data/SpunCoat-06252015/10x_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					}
				]        	
			}
        	return data;
        }

        function getVariant_4() {
        	var data = {
	    		segmentations: [
					{
						path: "data/SpunCoat-06252015/300x_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					},
					{
						path: "data/SpunCoat-06252015/300x_ins_9_108906616_13.jpg"
					},
					{
						path: "data/SpunCoat-06252015/300x_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					}
				]        
			}
        	return data;
        }

        function getVariant_5() {
        	var data = {
	    		segmentations: [
					{
						path: "data/SpunCoat-06252015/mp_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					},
					{
						path: "data/SpunCoat-06252015/mp_ins_9_108906616_13.jpg"
					},
					{
						path: "data/SpunCoat-06252015/mp_HG2_10X_SVrefine10Xhap1_167_del_1_56831106_21.jpg"
					}
				]       
			}
        	return data;
        }
    }

}());
