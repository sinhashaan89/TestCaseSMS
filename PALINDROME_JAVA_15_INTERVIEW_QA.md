# 15 Java Palindrome Coding Questions with Complete Answers (Basic to Medium)

This file contains 15 interview-style palindrome questions in Java.
For every question:

1. **Normal approach** (easy to understand, often brute force or less efficient)
2. **Optimized approach** (better time/space for interviews)

---

## 1) Check if a string is a palindrome

### Normal Approach (reverse and compare)

**Idea:** Build a reversed string and compare with original.

```java
class Q1Normal {
    public static boolean isPalindrome(String s) {
        if (s == null) return false;
        String reversed = new StringBuilder(s).reverse().toString();
        return s.equals(reversed);
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

### Optimized Approach (two pointers)

**Idea:** Compare characters from both ends moving inward.

```java
class Q1Optimized {
    public static boolean isPalindrome(String s) {
        if (s == null) return false;
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## 2) Valid palindrome ignoring case and non-alphanumeric characters

### Normal Approach (clean string, then reverse compare)

**Idea:** Keep only lowercase alphanumeric chars in a new string; compare with reverse.

```java
class Q2Normal {
    public static boolean isValidPalindrome(String s) {
        if (s == null) return false;
        StringBuilder cleaned = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.append(Character.toLowerCase(c));
            }
        }
        String normalized = cleaned.toString();
        String reversed = cleaned.reverse().toString();
        return normalized.equals(reversed);
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

### Optimized Approach (two pointers with skipping)

**Idea:** Skip non-alphanumeric on the fly; compare lowercase chars directly.

```java
class Q2Optimized {
    public static boolean isValidPalindrome(String s) {
        if (s == null) return false;
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## 3) Check if an integer is a palindrome (without converting to string in optimized version)

### Normal Approach (convert to string)

**Idea:** Convert number to string and use two-pointer check.

```java
class Q3Normal {
    public static boolean isPalindrome(int x) {
        if (x < 0) return false;
        String s = Integer.toString(x);
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(log10 n)`
- Space: `O(log10 n)`

### Optimized Approach (reverse only half number)

**Idea:** Reverse last half digits and compare with first half to avoid overflow risk.

```java
class Q3Optimized {
    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }
}
```

**Complexity**
- Time: `O(log10 n)`
- Space: `O(1)`

---

## 4) Check if an integer array is palindrome

### Normal Approach (copy and reverse)

**Idea:** Create a reversed copy and compare index-by-index.

```java
import java.util.Arrays;

class Q4Normal {
    public static boolean isPalindrome(int[] arr) {
        if (arr == null) return false;
        int[] reversed = Arrays.copyOf(arr, arr.length);
        for (int i = 0, j = reversed.length - 1; i < j; i++, j--) {
            int temp = reversed[i];
            reversed[i] = reversed[j];
            reversed[j] = temp;
        }
        return Arrays.equals(arr, reversed);
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

### Optimized Approach (two pointers in-place check)

**Idea:** Compare mirrored elements directly.

```java
class Q4Optimized {
    public static boolean isPalindrome(int[] arr) {
        if (arr == null) return false;
        int left = 0, right = arr.length - 1;
        while (left < right) {
            if (arr[left] != arr[right]) return false;
            left++;
            right--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## 5) Check if a singly linked list is palindrome

### Normal Approach (copy values to list)

**Idea:** Copy node values to `ArrayList`, then two-pointer compare.

```java
import java.util.ArrayList;
import java.util.List;

class Q5Normal {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public static boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next) {
            values.add(cur.val);
        }
        int left = 0, right = values.size() - 1;
        while (left < right) {
            if (!values.get(left).equals(values.get(right))) return false;
            left++;
            right--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

### Optimized Approach (reverse second half)

**Idea:** Find middle, reverse second half, compare halves, optionally restore.

```java
class Q5Optimized {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public static boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = reverse(slow.next);
        ListNode p1 = head, p2 = second;
        boolean ok = true;

        while (p2 != null) {
            if (p1.val != p2.val) {
                ok = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }

        slow.next = reverse(second); // restore original list
        return ok;
    }

    private static ListNode reverse(ListNode head) {
        ListNode prev = null, cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## 6) Find the longest palindromic substring

### Normal Approach (check all substrings)

**Idea:** Generate every substring and test palindrome; track longest.

```java
class Q6Normal {
    public static String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";
        String best = "";
        int n = s.length();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (isPalindrome(s, i, j) && (j - i + 1 > best.length())) {
                    best = s.substring(i, j + 1);
                }
            }
        }
        return best;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n^3)`
- Space: `O(1)` extra

### Optimized Approach (expand around center)

**Idea:** Expand from each center (odd and even) and keep best interval.

```java
class Q6Optimized {
    public static String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start + 1) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private static int expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return r - l - 1;
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(1)`

---

## 7) Count all palindromic substrings

### Normal Approach (all substrings + check)

**Idea:** Enumerate all substrings and test each one.

```java
class Q7Normal {
    public static int countSubstrings(String s) {
        if (s == null) return 0;
        int n = s.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (isPalindrome(s, i, j)) count++;
            }
        }
        return count;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n^3)`
- Space: `O(1)`

### Optimized Approach (expand from each center)

**Idea:** Every palindrome has a center; count successful expansions.

```java
class Q7Optimized {
    public static int countSubstrings(String s) {
        if (s == null) return 0;
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count += expandCount(s, i, i);     // odd
            count += expandCount(s, i, i + 1); // even
        }
        return count;
    }

    private static int expandCount(String s, int l, int r) {
        int c = 0;
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            c++;
            l--;
            r++;
        }
        return c;
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(1)`

---

## 8) Longest palindromic subsequence length

### Normal Approach (plain recursion)

**Idea:** If ends match, include both; else try skipping one end.

```java
class Q8Normal {
    public static int lps(String s) {
        if (s == null || s.isEmpty()) return 0;
        return solve(s, 0, s.length() - 1);
    }

    private static int solve(String s, int i, int j) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (s.charAt(i) == s.charAt(j)) return 2 + solve(s, i + 1, j - 1);
        return Math.max(solve(s, i + 1, j), solve(s, i, j - 1));
    }
}
```

**Complexity**
- Time: Exponential (`O(2^n)`)
- Space: `O(n)` recursion stack

### Optimized Approach (dynamic programming)

**Idea:** Bottom-up table `dp[i][j]` for substring `i..j`.

```java
class Q8Optimized {
    public static int lps(String s) {
        if (s == null || s.isEmpty()) return 0;
        int n = s.length();
        int[][] dp = new int[n][n];

        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1] : 0);
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(n^2)`

---

## 9) Minimum insertions to make a string palindrome

### Normal Approach (recursive)

**Idea:** If ends are equal, move inward; else insert on one side and take minimum.

```java
class Q9Normal {
    public static int minInsertions(String s) {
        if (s == null || s.length() <= 1) return 0;
        return solve(s, 0, s.length() - 1);
    }

    private static int solve(String s, int i, int j) {
        if (i >= j) return 0;
        if (s.charAt(i) == s.charAt(j)) return solve(s, i + 1, j - 1);
        return 1 + Math.min(solve(s, i + 1, j), solve(s, i, j - 1));
    }
}
```

**Complexity**
- Time: Exponential (`O(2^n)`)
- Space: `O(n)` recursion stack

### Optimized Approach (DP)

**Idea:** DP on ranges where `dp[i][j]` = min insertions for `s[i..j]`.

```java
class Q9Optimized {
    public static int minInsertions(String s) {
        if (s == null || s.length() <= 1) return 0;
        int n = s.length();
        int[][] dp = new int[n][n];

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0;
                } else {
                    dp[i][j] = 1 + Math.min(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(n^2)`

---

## 10) Minimum cuts for palindrome partitioning

### Normal Approach (backtracking all partitions)

**Idea:** Try all cut positions; keep minimum cuts when each chosen part is palindrome.

```java
class Q10Normal {
    public static int minCut(String s) {
        if (s == null || s.isEmpty()) return 0;
        return dfs(s, 0) - 1; // partitions - 1 = cuts
    }

    private static int dfs(String s, int start) {
        if (start == s.length()) return 0;
        int best = Integer.MAX_VALUE / 4;
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                best = Math.min(best, 1 + dfs(s, end + 1));
            }
        }
        return best;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: Exponential in worst case
- Space: `O(n)` recursion stack

### Optimized Approach (palindrome table + DP cuts)

**Idea:** Precompute palindrome substrings, then compute minimum cuts for each prefix.

```java
import java.util.Arrays;

class Q10Optimized {
    public static int minCut(String s) {
        if (s == null || s.isEmpty()) return 0;
        int n = s.length();

        boolean[][] pal = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i <= 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                }
            }
        }

        int[] cuts = new int[n];
        Arrays.fill(cuts, Integer.MAX_VALUE / 4);

        for (int end = 0; end < n; end++) {
            if (pal[0][end]) {
                cuts[end] = 0;
            } else {
                for (int start = 1; start <= end; start++) {
                    if (pal[start][end]) {
                        cuts[end] = Math.min(cuts[end], cuts[start - 1] + 1);
                    }
                }
            }
        }
        return cuts[n - 1];
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(n^2)`

---

## 11) Check if a string can become palindrome after removing at most one character

### Normal Approach (try removing every index)

**Idea:** Remove each character once and check palindrome each time.

```java
class Q11Normal {
    public static boolean validPalindrome(String s) {
        if (s == null) return false;
        if (isPalindrome(s, 0, s.length() - 1)) return true;

        for (int i = 0; i < s.length(); i++) {
            if (isPalindromeAfterRemovingIndex(s, i)) return true;
        }
        return false;
    }

    private static boolean isPalindromeAfterRemovingIndex(String s, int remove) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (l == remove) l++;
            if (r == remove) r--;
            if (l < r && s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n^2)`
- Space: `O(1)`

### Optimized Approach (single pass + one skip)

**Idea:** At first mismatch, skip either left or right once and verify.

```java
class Q11Optimized {
    public static boolean validPalindrome(String s) {
        if (s == null) return false;
        int l = 0, r = s.length() - 1;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
            }
            l++;
            r--;
        }
        return true;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## 12) Longest palindrome length that can be built from characters

### Normal Approach (count with HashMap)

**Idea:** Count frequency of each character; use all pairs plus one odd center.

```java
import java.util.HashMap;
import java.util.Map;

class Q12Normal {
    public static int longestPalindromeLength(String s) {
        if (s == null) return 0;
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        int len = 0;
        boolean hasOdd = false;
        for (int count : freq.values()) {
            len += (count / 2) * 2;
            if ((count & 1) == 1) hasOdd = true;
        }
        return hasOdd ? len + 1 : len;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(k)` where `k` is distinct characters

### Optimized Approach (frequency array for ASCII)

**Idea:** Use fixed array for faster counting when charset is limited.

```java
class Q12Optimized {
    public static int longestPalindromeLength(String s) {
        if (s == null) return 0;
        int[] freq = new int[128];
        for (char c : s.toCharArray()) freq[c]++;

        int len = 0;
        boolean hasOdd = false;
        for (int c : freq) {
            len += (c / 2) * 2;
            if ((c & 1) == 1) hasOdd = true;
        }
        return hasOdd ? len + 1 : len;
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(1)` (constant-size array)

---

## 13) Palindrome pairs in an array of words

### Normal Approach (check every pair)

**Idea:** For each pair `(i, j)`, test if `words[i] + words[j]` is palindrome.

```java
import java.util.ArrayList;
import java.util.List;

class Q13Normal {
    public static List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> ans = new ArrayList<>();
        if (words == null) return ans;

        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words.length; j++) {
                if (i == j) continue;
                String combined = words[i] + words[j];
                if (isPalindrome(combined)) {
                    List<Integer> pair = new ArrayList<>();
                    pair.add(i);
                    pair.add(j);
                    ans.add(pair);
                }
            }
        }
        return ans;
    }

    private static boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n^2 * k)` (roughly, for average length `k`)
- Space: `O(1)` extra (excluding output)

### Optimized Approach (hash map + split logic)

**Idea:** Store word to index map; for each split `prefix|suffix`, use reversed counterpart lookups.

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Q13Optimized {
    public static List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> ans = new ArrayList<>();
        if (words == null) return ans;

        Map<String, Integer> index = new HashMap<>();
        for (int i = 0; i < words.length; i++) index.put(words[i], i);

        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            for (int cut = 0; cut <= w.length(); cut++) {
                String left = w.substring(0, cut);
                String right = w.substring(cut);

                if (isPalindrome(left)) {
                    String need = new StringBuilder(right).reverse().toString();
                    Integer j = index.get(need);
                    if (j != null && j != i) {
                        List<Integer> pair = new ArrayList<>();
                        pair.add(j);
                        pair.add(i);
                        ans.add(pair);
                    }
                }

                if (cut != w.length() && isPalindrome(right)) {
                    String need = new StringBuilder(left).reverse().toString();
                    Integer j = index.get(need);
                    if (j != null && j != i) {
                        List<Integer> pair = new ArrayList<>();
                        pair.add(i);
                        pair.add(j);
                        ans.add(pair);
                    }
                }
            }
        }
        return ans;
    }

    private static boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Time: `O(n * k^2)`
- Space: `O(n * k)` for map storage

---

## 14) Answer many palindrome substring queries

### Normal Approach (check each query directly)

**Idea:** For every query `[l, r]`, run two-pointer palindrome check on that substring.

```java
class Q14Normal {
    public static boolean isPalindromeQuery(String s, int l, int r) {
        if (s == null || l < 0 || r >= s.length() || l > r) return false;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Per query time: `O(length of substring)`
- Space: `O(1)`

### Optimized Approach (rolling hash preprocessing)

**Idea:** Build forward and reverse hashes once, answer each query in `O(1)`.

```java
class Q14Optimized {
    static class RollingPalindromeQuery {
        private static final long MOD = 1_000_000_007L;
        private static final long BASE = 911_382_323L;

        private final String s;
        private final long[] pow;
        private final long[] pref;
        private final long[] prefRev;

        RollingPalindromeQuery(String s) {
            this.s = (s == null) ? "" : s;
            int n = this.s.length();
            this.pow = new long[n + 1];
            this.pref = new long[n + 1];
            this.prefRev = new long[n + 1];
            pow[0] = 1;

            String rev = new StringBuilder(this.s).reverse().toString();
            for (int i = 0; i < n; i++) {
                pow[i + 1] = (pow[i] * BASE) % MOD;
                pref[i + 1] = (pref[i] * BASE + this.s.charAt(i)) % MOD;
                prefRev[i + 1] = (prefRev[i] * BASE + rev.charAt(i)) % MOD;
            }
        }

        public boolean isPalindrome(int l, int r) {
            if (l < 0 || r >= s.length() || l > r) return false;
            long h1 = hash(pref, l, r);
            int rl = s.length() - 1 - r;
            int rr = s.length() - 1 - l;
            long h2 = hash(prefRev, rl, rr);
            return h1 == h2;
        }

        private long hash(long[] p, int l, int r) {
            long val = (p[r + 1] - (p[l] * pow[r - l + 1]) % MOD) % MOD;
            if (val < 0) val += MOD;
            return val;
        }
    }
}
```

**Complexity**
- Preprocessing: `O(n)`
- Per query: `O(1)`
- Space: `O(n)`

---

## 15) Find the next palindrome number greater than a given number string

### Normal Approach (increment and test)

**Idea:** Convert to number, keep adding 1 until palindrome appears.
This is only practical for small values.

```java
class Q15Normal {
    public static String nextPalindrome(String num) {
        if (num == null || num.isEmpty()) return "";
        long x = Long.parseLong(num);
        x++;
        while (!isPalindrome(Long.toString(x))) {
            x++;
        }
        return Long.toString(x);
    }

    private static boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

**Complexity**
- Worst-case time: can be very large (many increments)
- Space: `O(n)` due to string conversion

### Optimized Approach (mirror + carry in string)

**Idea:** Mirror left half to right.
If mirrored result is not greater, add carry to middle and mirror again.

```java
class Q15Optimized {
    public static String nextPalindrome(String num) {
        if (num == null || num.isEmpty()) return "";
        char[] arr = num.toCharArray();
        int n = arr.length;

        char[] candidate = arr.clone();
        mirror(candidate);
        if (isGreater(candidate, arr)) {
            return new String(candidate);
        }

        // Add 1 to middle and propagate carry.
        int carry = 1;
        int left = (n - 1) / 2;
        int right = n / 2;

        while (left >= 0 && carry > 0) {
            int digit = (candidate[left] - '0') + carry;
            carry = digit / 10;
            candidate[left] = (char) ('0' + (digit % 10));
            candidate[right] = candidate[left];
            left--;
            right++;
        }

        if (carry > 0) {
            // Example: 999 -> 1001
            StringBuilder sb = new StringBuilder();
            sb.append('1');
            for (int i = 0; i < n - 1; i++) sb.append('0');
            sb.append('1');
            return sb.toString();
        }

        mirror(candidate);
        return new String(candidate);
    }

    private static void mirror(char[] arr) {
        int l = 0, r = arr.length - 1;
        while (l < r) {
            arr[r] = arr[l];
            l++;
            r--;
        }
    }

    private static boolean isGreater(char[] a, char[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) return a[i] > b[i];
        }
        return false; // equal is not greater
    }
}
```

**Complexity**
- Time: `O(n)`
- Space: `O(n)` (char array and output string)

---

## Quick revision tip for 7-day interview prep

Practice order:
1. Q1-Q5 (foundations)
2. Q6-Q11 (most frequently asked variants)
3. Q12-Q15 (medium-level patterns: hashing, pairs, numeric construction)

