# Strings, Arrays, Collections Patterns - Full Java Solutions

This document contains full Java solutions for 20 common coding problems across strings, arrays, and collections, plus a short explanation and complexity for each.

---

## Complete Java Class

```java
import java.util.*;

public class PatternSolutions {

    // 1) Valid Anagram
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            int count = freq.getOrDefault(c, 0);
            if (count == 0) return false;
            if (count == 1) freq.remove(c);
            else freq.put(c, count - 1);
        }

        return freq.isEmpty();
    }

    // 2) First Unique Character in a String
    public static int firstUniqChar(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            if (freq.get(s.charAt(i)) == 1) return i;
        }
        return -1;
    }

    // 3) Longest Substring Without Repeating Characters
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int left = 0, best = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
                left = lastSeen.get(c) + 1;
            }
            lastSeen.put(c, right);
            best = Math.max(best, right - left + 1);
        }

        return best;
    }

    // 4) Minimum Window Substring
    public static String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) return "";

        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> window = new HashMap<>();
        int required = need.size();
        int formed = 0;
        int left = 0;
        int bestLen = Integer.MAX_VALUE;
        int bestStart = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            window.put(c, window.getOrDefault(c, 0) + 1);

            if (need.containsKey(c) && window.get(c).intValue() == need.get(c).intValue()) {
                formed++;
            }

            while (left <= right && formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestStart = left;
                }

                char lc = s.charAt(left);
                window.put(lc, window.get(lc) - 1);
                if (need.containsKey(lc) && window.get(lc) < need.get(lc)) {
                    formed--;
                }
                left++;
            }
        }

        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestStart, bestStart + bestLen);
    }

    // 5) Longest Palindromic Substring
    public static String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";

        int bestL = 0, bestR = 0;

        for (int i = 0; i < s.length(); i++) {
            int[] odd = expandFromCenter(s, i, i);
            int[] even = expandFromCenter(s, i, i + 1);

            if (odd[1] - odd[0] > bestR - bestL) {
                bestL = odd[0];
                bestR = odd[1];
            }
            if (even[1] - even[0] > bestR - bestL) {
                bestL = even[0];
                bestR = even[1];
            }
        }

        return s.substring(bestL, bestR + 1);
    }

    private static int[] expandFromCenter(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return new int[]{l + 1, r - 1};
    }

    // 6) String Compression (LeetCode 443 style, in-place)
    public static int compress(char[] chars) {
        int n = chars.length;
        int read = 0, write = 0;

        while (read < n) {
            char ch = chars[read];
            int count = 0;

            while (read < n && chars[read] == ch) {
                read++;
                count++;
            }

            chars[write++] = ch;
            if (count > 1) {
                for (char d : String.valueOf(count).toCharArray()) {
                    chars[write++] = d;
                }
            }
        }

        return write;
    }

    // 7) Two Sum
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (seen.containsKey(need)) {
                return new int[]{seen.get(need), i};
            }
            seen.put(nums[i], i);
        }

        return new int[]{-1, -1};
    }

    // 8) Best Time to Buy and Sell Stock
    public static int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int best = 0;

        for (int p : prices) {
            minPrice = Math.min(minPrice, p);
            best = Math.max(best, p - minPrice);
        }

        return best;
    }

    // 9) Maximum Subarray (Kadane)
    public static int maxSubArray(int[] nums) {
        int current = nums[0];
        int best = nums[0];

        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            best = Math.max(best, current);
        }

        return best;
    }

    // 10) Product of Array Except Self
    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        int prefix = 1;
        for (int i = 0; i < n; i++) {
            ans[i] = prefix;
            prefix *= nums[i];
        }

        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] *= suffix;
            suffix *= nums[i];
        }

        return ans;
    }

    // 11) 3Sum
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i] > 0) break;

            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum < 0) l++;
                else if (sum > 0) r--;
                else {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                }
            }
        }

        return res;
    }

    // 12) Merge Intervals
    public static int[][] mergeIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return new int[0][0];

        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> merged = new ArrayList<>();

        int[] current = intervals[0].clone();
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = Math.max(current[1], intervals[i][1]);
            } else {
                merged.add(current);
                current = intervals[i].clone();
            }
        }
        merged.add(current);

        return merged.toArray(new int[merged.size()][]);
    }

    // 13) Subarray Sum Equals K
    public static int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);

        int prefix = 0, count = 0;
        for (int x : nums) {
            prefix += x;
            count += freq.getOrDefault(prefix - k, 0);
            freq.put(prefix, freq.getOrDefault(prefix, 0) + 1);
        }

        return count;
    }

    // 14) Find Minimum in Rotated Sorted Array
    public static int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;

        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] > nums[r]) l = m + 1;
            else r = m;
        }

        return nums[l];
    }

    // 15) Group Anagrams
    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String w : strs) {
            char[] arr = w.toCharArray();
            Arrays.sort(arr);
            String key = new String(arr);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(w);
        }

        return new ArrayList<>(groups.values());
    }

    // 16) Top K Frequent Elements
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        // Min-heap by frequency: [number, count]
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));

        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            minHeap.offer(new int[]{e.getKey(), e.getValue()});
            if (minHeap.size() > k) minHeap.poll();
        }

        int[] ans = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            ans[i] = minHeap.poll()[0];
        }
        return ans;
    }

    // 17) Valid Parentheses
    public static boolean isValidParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put(']', '[');
        pairs.put('}', '{');

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (!pairs.containsKey(ch)) return false;
                if (stack.isEmpty() || stack.pop() != pairs.get(ch)) return false;
            }
        }

        return stack.isEmpty();
    }

    // 18) Daily Temperatures
    public static int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>(); // indices, decreasing temperatures

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                ans[idx] = i - idx;
            }
            stack.push(i);
        }

        return ans;
    }

    // 19) Sliding Window Maximum
    public static int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k <= 0 || k > nums.length) return new int[0];

        int n = nums.length;
        int[] ans = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>(); // indices, values decreasing

        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) ans[i - k + 1] = nums[dq.peekFirst()];
        }

        return ans;
    }

    // 20) Kth Largest Element in an Array
    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int x : nums) {
            minHeap.offer(x);
            if (minHeap.size() > k) minHeap.poll();
        }

        return minHeap.peek();
    }
}
```

---

## Explanations and Complexity

### 1) Valid Anagram
- Count letters in first string, decrement using second string.
- If any count goes negative or lengths differ, not an anagram.
- **Time:** `O(n)`  
- **Space:** `O(k)` distinct chars

### 2) First Unique Character in a String
- First pass builds frequency; second pass returns first index with count `1`.
- **Time:** `O(n)`  
- **Space:** `O(k)`

### 3) Longest Substring Without Repeating Characters
- Sliding window with `left` pointer and `lastSeen` map.
- Move `left` when duplicate appears inside current window.
- **Time:** `O(n)`  
- **Space:** `O(k)`

### 4) Minimum Window Substring
- Maintain character requirements and current window counts.
- Expand right to satisfy requirements, shrink left for minimum valid window.
- **Time:** `O(n + m)`  
- **Space:** `O(k)`

### 5) Longest Palindromic Substring
- Try each index as odd and even palindrome center.
- Expand outward while characters match.
- **Time:** `O(n^2)`  
- **Space:** `O(1)`

### 6) String Compression
- Two pointers: one reads groups, one writes compressed output in place.
- Write character and count digits if group size > 1.
- **Time:** `O(n)`  
- **Space:** `O(1)` extra

### 7) Two Sum
- Store value-to-index in map.
- For each value, check if complement `target - value` already exists.
- **Time:** `O(n)`  
- **Space:** `O(n)`

### 8) Best Time to Buy and Sell Stock
- Track minimum price so far and best profit at each day.
- **Time:** `O(n)`  
- **Space:** `O(1)`

### 9) Maximum Subarray (Kadane)
- `current = max(nums[i], current + nums[i])`
- Keep global best over all positions.
- **Time:** `O(n)`  
- **Space:** `O(1)`

### 10) Product of Array Except Self
- First pass stores prefix products.
- Second pass multiplies suffix products.
- **Time:** `O(n)`  
- **Space:** `O(1)` extra (excluding output array)

### 11) 3Sum
- Sort array, fix one number, find remaining pair using two pointers.
- Skip duplicates to avoid repeated triplets.
- **Time:** `O(n^2)`  
- **Space:** `O(1)` extra (excluding output)

### 12) Merge Intervals
- Sort intervals by start time.
- Merge current interval with previous if overlap exists.
- **Time:** `O(n log n)`  
- **Space:** `O(n)` for output

### 13) Subarray Sum Equals K
- Use prefix sum and map of prefix frequencies.
- If current prefix is `p`, previous `p-k` indicates valid subarray.
- **Time:** `O(n)`  
- **Space:** `O(n)`

### 14) Find Minimum in Rotated Sorted Array
- Binary search compares mid with right boundary to locate pivot side.
- **Time:** `O(log n)`  
- **Space:** `O(1)`

### 15) Group Anagrams
- Sort each word to build canonical key.
- Group words by identical sorted key.
- **Time:** `O(n * k log k)`  
- **Space:** `O(nk)`

### 16) Top K Frequent Elements
- Count frequencies, then keep min-heap of size `k`.
- Heap keeps the top `k` frequencies seen so far.
- **Time:** `O(n log k)`  
- **Space:** `O(n)`

### 17) Valid Parentheses
- Push opening brackets to stack; closing bracket must match top.
- Valid if stack is empty at the end.
- **Time:** `O(n)`  
- **Space:** `O(n)`

### 18) Daily Temperatures
- Monotonic decreasing stack of indices.
- When warmer day appears, resolve previous colder indices.
- **Time:** `O(n)`  
- **Space:** `O(n)`

### 19) Sliding Window Maximum
- Deque stores indices in decreasing value order.
- Front of deque is max for current window.
- **Time:** `O(n)`  
- **Space:** `O(k)`

### 20) Kth Largest Element in an Array
- Maintain min-heap of size `k`.
- Heap top is kth largest after processing all elements.
- **Time:** `O(n log k)`  
- **Space:** `O(k)`

