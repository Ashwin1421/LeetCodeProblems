/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let dupMap = [];
    let result = false;
    for(var i=0;i<nums.length;i++){
        if(dupMap[nums[i]] == null){
            dupMap[nums[i]] = 1;
            result = false;
        }else{
            return true;
        }
    }
    return result;
};