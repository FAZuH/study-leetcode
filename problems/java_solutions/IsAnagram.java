import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

class Solution {
  public boolean isAnagram(String s, String t) {
    int sLength = s.length();
    if (sLength != t.length()) {
      return false;
    }

    Map<String, Integer> countS = new HashMap<>();
    Map<String, Integer> countT = new HashMap<>();

    for (int i = 0; i < sLength; i++) {
      String lS = String.valueOf(s.charAt(i));
      String lT = String.valueOf(t.charAt(i));

      countS.put(lS, countS.getOrDefault(lS, 0) + 1);
      countT.put(lT, countT.getOrDefault(lT, 0) + 1);
    }

    return countS.equals(countT);
  }
}
