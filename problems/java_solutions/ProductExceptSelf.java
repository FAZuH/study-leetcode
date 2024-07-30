class Solution {
  public int[] productExceptSelf(int[] nums) {
    int[] ret = new int[nums.length];

    for (int i = 0; i < nums.length; i++) {
      ret[i] = getProduct(nums, i);
    }
    return ret;
  }

  private int getProduct(int[] nums, int curr) {
    int ret = 1;
    for (int i = 0; i < nums.length; i++) {
      if (i == curr) {
        continue;
      }
      ret *= nums[i];
    }
    return ret;
  }
}
