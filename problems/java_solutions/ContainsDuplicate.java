package problems.solutions;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
  public boolean hasDuplicate(int[] nums) {
    Set<Integer> occuredNums = new HashSet<>();

    for (int i = 0; i < nums.length; i++) {
      if (occuredNums.contains(nums[i]) == true) {
        return true;
      }
      occuredNums.add(nums[i]);
    }
    return false;

  }
}
