(function() {
    'use strict';

    angular.module('app')
    .config(config);

	function config($stateProvider, $urlRouterProvider) {
	    $urlRouterProvider.when('', '/main');
	    $urlRouterProvider.otherwise('/main');
	    $stateProvider
	        .state('main', {
	        	url:'/main',
	            templateUrl: 'front_end/app/components/main/app.main.view.html',
	            controller: 'mainCntrl',
	            controllerAs: 'vm'
	        })
			.state('draw', {
				url: '/draw/:drawId',
				templateUrl: 'front_end/app/components/draws/app.draw.view.html',
				controller: 'drawCntrl',
				controllerAs: 'vm'

			});
	}
})();

