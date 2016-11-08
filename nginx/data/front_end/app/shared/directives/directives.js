(function() {
    'use strict';
    angular.module('app.directives', []).
    directive('mdTable',mdTable);

    function mdTable(){
        return {
        restrict: 'EA',
        scope: {
            headers: '=',
            content: '=',
            filters: '=',
            customClass: '=customClass'
        },
        template: angular.element(document.querySelector('#md-table-template')).html()
        }
    }

})();



