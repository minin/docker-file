(function() {
  'use strict';

  angular.module('app.draws').controller('drawCntrl', drawCntrl);
    
    
    
    drawCntrl.$inject = ['$scope', '$state', '$stateParams', 'dataService'];
    
    function drawCntrl($scope ,$state, $stateParams, dataService){
        
        var vm = this;
        vm.draw = null;
        vm.drawId = $stateParams.drawId;
        vm.lotteries = [];
        vm.update_lottery = update_lottery;
        vm.change_button_status = true;
        vm._currentDraw = null;
        activate();
        $scope.$watch(function() { return vm.draw}, function(newVal, oldVal) {
            if (newVal && oldVal && vm.draw){
                if (newVal.lottery.title != vm._currentDraw.title){
                    vm.change_button_status = false;
                }
                else{
                    vm.change_button_status = true;
                }
            }
        }, true);


        function activate(){
            return getLotteries().then(function(){
                return getSingleDraw(vm.drawId).then(function(){
                    vm._currentDraw = vm.draw;
                    console.log('done loading lottery list and draw.');
                });
            })

        }

        function getLotteries() {
            return dataService.getLotteries().then(function(data) {
                vm.lotteries = data;
                return vm.lotteries;
            });
        }
        function getSingleDraw(drawId) {
            return dataService.getSingleDraw(drawId).then(function(data) {
                vm.draw = {'title':data.title, 'jackpot':data.jackpot, 'date':data.date, 'lottery':data.lottery};
                return vm.draw;
            });
        }

        function update_lottery(){
            var lottery_index = find_index(vm.draw.lottery.title);
            return dataService.updateDraw(vm.drawId, vm.draw, lottery_index).then(function(data){
                $state.reload();
            });

        }

        function find_index(lottery_title){
            var result = vm.lotteries.filter(function( obj ) {
                return obj.title == lottery_title;
            });
            return result[0].id
        }
  }
})();