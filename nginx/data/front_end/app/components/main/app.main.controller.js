(function() {
  'use strict';

  angular.module('app.main').controller('mainCntrl', mainCntrl);
  mainCntrl.$inject = ['dataService', '$state'];
  
  function mainCntrl(dataService, $state){
	  var vm = this;
	  vm.draws = [];
	  vm.select_draw = select_draw;
	  activate();


	  function activate() {
		  return getDraws().then(function() {
		});
	  }

	  function getDraws() {
	    return dataService.getDraws().then(function(data) {
			vm.draws = data;
			return vm.draws;
		});
	  }

	  function select_draw(draw_object) {
		  console.log(draw_object);
		  $state.go('draw', {'drawId':draw_object.id});
	  }
  }
})();