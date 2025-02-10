class Solution {
    public int removeDuplicates(int[] nums) {

        //Same thing but in Java syntax
	  
		int i = 0;
	  
		for (int j = 1; j < nums.length; j++) {
			if (nums[j] != nums[i]) {
				i += 1;
				nums[i] = nums[j];
			}
		}
			  
		for (int k = i + 1; k <  nums.length; k++) {
			nums[k] = -1;
        }
		return i + 1;
    }
}