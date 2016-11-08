(function() {
  'use strict';
  angular.module('app.services', []).
  	factory('dataService', dataService);
	dataService.$inject = ['$http'];
  
	function dataService($http){
		return {
			getDraws: getDraws,
			getLotteries: getLotteries,
			getSingleDraw: getSingleDraw,
            updateDraw: updateDraw
		};

		function getDraws() {
			return $http.get('/api/v1/draw/')
				.then(getDrawsComplete)
				.catch(getDrawsFailed);

			function getDrawsComplete(response) {
				return response.data;
			}

			function getDrawsFailed(error) {
				console.log(error);
			}
		}

		 function getSingleDraw(drawId) {
			  return $http.get('/api/v1/draw/'+ drawId + '/')
				  .then(getDrawComplete)
				  .catch(getDrawFailed);
			  function getDrawComplete(response) {
				  return response.data;
			  }
			  function getDrawFailed(error) {
				  console.log(error);
			  }
		  }

		 function getLotteries() {
			  return $http.get('/api/v1/lottery/')
				  .then(getLotteriesComplete)
				  .catch(getLotteriesFailed);
			  function getLotteriesComplete(response) {
				  return response.data;
			  }
			  function getLotteriesFailed(error) {
				  console.log(error);
			  }
		 }

		function updateDraw(drawId, data, lottery_index){
            data.lottery = lottery_index;
			return $http.put('/api/v1/draw/'+ drawId + '/', data)
				.then(updateDrawComplete)
				.catch(updateDrawFailed);
			function updateDrawComplete(response) {
				return response.data;
			}
			function updateDrawFailed(error) {
				console.log(error);
			}
		}
	  }
})();