class Solution {
	public int[] twoSum(int[] nums, int target) {
	    int[] retIndices= new int[2];
	    Map<Integer, Integer> indexMap = new HashMap<>();
	    for(int i=0; i<nums.length; i++){
		
		if(indexMap.get(nums[i]) != null){
		    retIndices[1] = i;
		    retIndices[0] = indexMap.get(nums[i]);
		}
		indexMap.put(target-nums[i],i);
	    }
	    return retIndices;
	}
    }