# Java Palindrome Question + Solution Pairs

This guide turns the palindrome question bank into question-and-solution notes.
Each section covers a major palindrome type with a representative Java solution,
a short explanation, and time/space complexity.

Full runnable implementations live in:

- `src/main/java/PalindromeSolutions.java`

---

## 1) Basic String Palindrome

### Question

Write a Java program to check whether a given string is a palindrome.

### Java Solution

```java
public static boolean isPalindrome(String value) {
    if (value == null) {
        return false;
    }
    int left = 0;
    int right = value.length() - 1;

    while (left < right) {
        if (value.charAt(left) != value.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- Use two pointers: one from the start and one from the end.
- Compare matching characters while moving inward.
- The first mismatch means the string is not a palindrome.
- If all mirrored characters match, the string is a palindrome.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 2) Palindrome Ignoring Case, Spaces, and Punctuation

### Question

Validate whether a sentence like `"A man, a plan, a canal: Panama"` is a palindrome
while ignoring case and non-alphanumeric characters.

### Java Solution

```java
public static boolean isPalindromeAlphaNumeric(String value) {
    if (value == null) {
        return false;
    }

    int left = 0;
    int right = value.length() - 1;

    while (left < right) {
        while (left < right && !Character.isLetterOrDigit(value.charAt(left))) {
            left++;
        }
        while (left < right && !Character.isLetterOrDigit(value.charAt(right))) {
            right--;
        }

        if (Character.toLowerCase(value.charAt(left))
                != Character.toLowerCase(value.charAt(right))) {
            return false;
        }

        left++;
        right--;
    }
    return true;
}
```

### Explanation

- Skip all characters that should not participate in the comparison.
- Convert letters to the same case before comparing.
- This is the standard interview solution for "valid palindrome" phrases.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 3) Remove At Most One Character to Make a Palindrome

### Question

Check whether a string can become a palindrome after removing at most one character.

### Java Solution

```java
public static boolean canBecomePalindromeAfterRemovingAtMostOne(String value) {
    if (value == null) {
        return false;
    }

    int left = 0;
    int right = value.length() - 1;

    while (left < right) {
        if (value.charAt(left) != value.charAt(right)) {
            return isPalindromeRange(value, left + 1, right)
                    || isPalindromeRange(value, left, right - 1);
        }
        left++;
        right--;
    }
    return true;
}

private static boolean isPalindromeRange(String value, int left, int right) {
    while (left < right) {
        if (value.charAt(left) != value.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- Scan from both ends.
- At the first mismatch, try skipping either the left character or the right character.
- If either remaining substring is a palindrome, the answer is `true`.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 4) Integer Palindrome Without Converting to a String

### Question

Check whether an integer is a palindrome without converting it to a string.

### Java Solution

```java
public static boolean isPalindromeWithoutString(int value) {
    if (value < 0 || (value % 10 == 0 && value != 0)) {
        return false;
    }

    int reversedHalf = 0;
    while (value > reversedHalf) {
        reversedHalf = reversedHalf * 10 + value % 10;
        value /= 10;
    }

    return value == reversedHalf || value == reversedHalf / 10;
}
```

### Explanation

- Negative numbers are not treated as palindromes here.
- Instead of reversing the whole number, reverse only half of it.
- This avoids overflow risk and is more efficient than full reversal.
- For odd-length numbers, ignore the middle digit with `reversedHalf / 10`.

### Complexity

- **Time:** `O(log10 n)`
- **Space:** `O(1)`

---

## 5) Palindrome in Arrays and Collections

### Question

Check whether an integer array is a palindrome.

### Java Solution

```java
public static boolean isArrayPalindrome(int[] values) {
    if (values == null) {
        return false;
    }

    int left = 0;
    int right = values.length - 1;

    while (left < right) {
        if (values[left] != values[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- The same two-pointer idea used for strings also works for arrays.
- This pattern extends easily to `List<T>` by using `Objects.equals`.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 6) Linked List Palindrome With List Restoration

### Question

Check whether a singly linked list is a palindrome and restore the original list afterward.

### Java Solution

```java
static class SinglyNode {
    int value;
    SinglyNode next;

    SinglyNode(int value) {
        this.value = value;
    }
}

public static boolean isPalindromeAndRestore(SinglyNode head) {
    if (head == null || head.next == null) {
        return true;
    }

    SinglyNode slow = head;
    SinglyNode fast = head;
    while (fast.next != null && fast.next.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    SinglyNode secondHalf = reverseList(slow.next);
    SinglyNode secondHalfHead = secondHalf;
    SinglyNode firstHalf = head;
    boolean matches = true;

    while (secondHalf != null) {
        if (firstHalf.value != secondHalf.value) {
            matches = false;
            break;
        }
        firstHalf = firstHalf.next;
        secondHalf = secondHalf.next;
    }

    slow.next = reverseList(secondHalfHead);
    return matches;
}

private static SinglyNode reverseList(SinglyNode head) {
    SinglyNode previous = null;
    SinglyNode current = head;

    while (current != null) {
        SinglyNode next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
}
```

### Explanation

- Use slow/fast pointers to find the middle.
- Reverse the second half of the list.
- Compare the first half with the reversed second half.
- Reverse again to restore the original structure.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 7) Longest Palindromic Substring

### Question

Find the longest palindromic substring in a string.

### Java Solution

```java
public static String longestPalindromicSubstring(String value) {
    if (value == null || value.isEmpty()) {
        return "";
    }

    int bestStart = 0;
    int bestEnd = 0;

    for (int center = 0; center < value.length(); center++) {
        int[] odd = expandAroundCenter(value, center, center);
        int[] even = expandAroundCenter(value, center, center + 1);

        if (odd[1] - odd[0] > bestEnd - bestStart) {
            bestStart = odd[0];
            bestEnd = odd[1];
        }
        if (even[1] - even[0] > bestEnd - bestStart) {
            bestStart = even[0];
            bestEnd = even[1];
        }
    }

    return value.substring(bestStart, bestEnd + 1);
}

private static int[] expandAroundCenter(String value, int left, int right) {
    while (left >= 0
            && right < value.length()
            && value.charAt(left) == value.charAt(right)) {
        left--;
        right++;
    }
    return new int[]{left + 1, right - 1};
}
```

### Explanation

- Every palindrome expands around a center.
- Odd-length palindromes have one center character.
- Even-length palindromes have a center gap between two characters.
- Expand from every possible center and keep the best range.

### Complexity

- **Time:** `O(n^2)`
- **Space:** `O(1)`

---

## 8) Count All Palindromic Substrings

### Question

Count all palindromic substrings in a given string.

### Java Solution

```java
public static long countPalindromicSubstrings(String value) {
    if (value == null) {
        return 0L;
    }

    long count = 0L;
    for (int center = 0; center < value.length(); center++) {
        count += countFromCenter(value, center, center);
        count += countFromCenter(value, center, center + 1);
    }
    return count;
}

private static int countFromCenter(String value, int left, int right) {
    int count = 0;
    while (left >= 0
            && right < value.length()
            && value.charAt(left) == value.charAt(right)) {
        count++;
        left--;
        right++;
    }
    return count;
}
```

### Explanation

- This reuses the center-expansion idea.
- Every time expansion succeeds, one more palindromic substring is found.
- It is a common follow-up after the longest palindromic substring problem.

### Complexity

- **Time:** `O(n^2)`
- **Space:** `O(1)`

---

## 9) Longest Palindromic Subsequence

### Question

Find the length of the longest palindromic subsequence in a string.

### Java Solution

```java
public static int longestPalindromicSubsequenceLength(String value) {
    if (value == null || value.isEmpty()) {
        return 0;
    }

    int n = value.length();
    int[][] dp = new int[n][n];

    for (int start = n - 1; start >= 0; start--) {
        dp[start][start] = 1;
        for (int end = start + 1; end < n; end++) {
            if (value.charAt(start) == value.charAt(end)) {
                dp[start][end] = 2 + (start + 1 <= end - 1 ? dp[start + 1][end - 1] : 0);
            } else {
                dp[start][end] = Math.max(dp[start + 1][end], dp[start][end - 1]);
            }
        }
    }

    return dp[0][n - 1];
}
```

### Explanation

- A substring is contiguous, but a subsequence is not.
- `dp[i][j]` stores the answer for the substring from `i` to `j`.
- If the ends match, include both.
- Otherwise, drop one end and take the better answer.

### Complexity

- **Time:** `O(n^2)`
- **Space:** `O(n^2)`

---

## 10) Minimum Cuts for Palindrome Partitioning

### Question

Given a string, partition it so every part is a palindrome and return the minimum number of cuts.

### Java Solution

```java
public static int minCutPalindromePartition(String value) {
    if (value == null || value.isEmpty()) {
        return 0;
    }

    boolean[][] table = buildPalindromeTable(value);
    int[] cuts = new int[value.length()];
    Arrays.fill(cuts, Integer.MAX_VALUE / 4);

    for (int end = 0; end < value.length(); end++) {
        if (table[0][end]) {
            cuts[end] = 0;
            continue;
        }

        for (int start = 1; start <= end; start++) {
            if (table[start][end]) {
                cuts[end] = Math.min(cuts[end], cuts[start - 1] + 1);
            }
        }
    }

    return cuts[value.length() - 1];
}

private static boolean[][] buildPalindromeTable(String value) {
    int n = value.length();
    boolean[][] table = new boolean[n][n];

    for (int start = n - 1; start >= 0; start--) {
        table[start][start] = true;
        for (int end = start + 1; end < n; end++) {
            table[start][end] = value.charAt(start) == value.charAt(end)
                    && (end - start == 1 || table[start + 1][end - 1]);
        }
    }
    return table;
}
```

### Explanation

- First precompute which substrings are palindromes.
- Then use `cuts[i]` to track the minimum cuts needed for `value[0..i]`.
- If `value[start..end]` is a palindrome, that segment can be the last partition.

### Complexity

- **Time:** `O(n^2)`
- **Space:** `O(n^2)`

---

## 11) Build One Palindrome From the Characters of a String

### Question

Rearrange the characters of a string to form one palindrome, if possible.

### Java Solution

```java
public static String buildOnePalindrome(String value) {
    if (value == null) {
        return "";
    }

    Map<Character, Integer> counts = new TreeMap<>();
    for (char ch : value.toCharArray()) {
        counts.merge(ch, 1, Integer::sum);
    }

    int oddCount = 0;
    Character middle = null;
    StringBuilder half = new StringBuilder();

    for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
        if ((entry.getValue() & 1) == 1) {
            oddCount++;
            middle = entry.getKey();
        }
        for (int i = 0; i < entry.getValue() / 2; i++) {
            half.append(entry.getKey());
        }
    }

    if (oddCount > 1) {
        return "";
    }

    String leftHalf = half.toString();
    return leftHalf + (middle == null ? "" : middle) + new StringBuilder(leftHalf).reverse();
}
```

### Explanation

- At most one character may have an odd frequency.
- Put half of each frequency on the left side.
- Place the odd-frequency character in the middle if it exists.
- Mirror the left half to build the right half.

### Complexity

- **Time:** `O(n log sigma)` with `TreeMap`, where `sigma` is the number of distinct characters
- **Space:** `O(sigma)`

> If lexicographic ordering is not needed, a `HashMap` version is effectively `O(n)`.

---

## 12) Shortest Palindrome by Adding Characters in Front

### Question

Construct the shortest palindrome by adding characters only to the front of the string.

### Java Solution

```java
public static String shortestPalindromeByAddingFront(String value) {
    if (value == null) {
        return "";
    }

    int prefixLength = longestPalindromicPrefixLength(value);
    String suffix = value.substring(prefixLength);
    return new StringBuilder(suffix).reverse() + value;
}

private static int longestPalindromicPrefixLength(String value) {
    String reversed = new StringBuilder(value).reverse().toString();
    String combined = value + "#" + reversed;
    int[] lps = new int[combined.length()];

    for (int index = 1; index < combined.length(); index++) {
        int length = lps[index - 1];
        while (length > 0 && combined.charAt(index) != combined.charAt(length)) {
            length = lps[length - 1];
        }
        if (combined.charAt(index) == combined.charAt(length)) {
            length++;
        }
        lps[index] = length;
    }

    return lps[combined.length() - 1];
}
```

### Explanation

- Find the longest prefix that is already a palindrome.
- The remaining suffix must be mirrored and added to the front.
- The KMP prefix table helps compute that longest palindromic prefix efficiently.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## 13) Palindrome Pairs in a List of Words

### Question

Given an array of words, find all index pairs whose concatenation is a palindrome.

### Java Solution

```java
public static List<List<Integer>> palindromePairs(String[] words) {
    if (words == null) {
        return List.of();
    }

    Map<String, Integer> indexByWord = new HashMap<>();
    for (int i = 0; i < words.length; i++) {
        indexByWord.put(words[i], i);
    }

    List<List<Integer>> result = new ArrayList<>();
    Set<String> seen = new HashSet<>();

    for (int i = 0; i < words.length; i++) {
        String word = words[i];

        for (int cut = 0; cut <= word.length(); cut++) {
            String prefix = word.substring(0, cut);
            String suffix = word.substring(cut);

            if (isPalindrome(prefix)) {
                String needed = new StringBuilder(suffix).reverse().toString();
                Integer match = indexByWord.get(needed);
                if (match != null && match != i && seen.add(match + ":" + i)) {
                    result.add(List.of(match, i));
                }
            }

            if (cut != word.length() && isPalindrome(suffix)) {
                String needed = new StringBuilder(prefix).reverse().toString();
                Integer match = indexByWord.get(needed);
                if (match != null && match != i && seen.add(i + ":" + match)) {
                    result.add(List.of(i, match));
                }
            }
        }
    }

    return result;
}

private static boolean isPalindrome(String value) {
    int left = 0;
    int right = value.length() - 1;
    while (left < right) {
        if (value.charAt(left) != value.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- Split every word into `prefix | suffix`.
- If the prefix is a palindrome, the reversed suffix can be placed before the word.
- If the suffix is a palindrome, the reversed prefix can be placed after the word.
- A hash map makes reverse-lookups fast.

### Complexity

- **Time:** `O(n * k^2)`, where `n` is the number of words and `k` is the average word length
- **Space:** `O(n * k)`

---

## 14) Count Palindromic Rows and Columns in a Matrix

### Question

Count how many rows and columns of a matrix form palindromes.

### Java Solution

```java
public static long countPalindromicRowsAndColumns(char[][] matrix) {
    return countPalindromicRows(matrix) + countPalindromicColumns(matrix);
}

private static long countPalindromicRows(char[][] matrix) {
    long count = 0;
    for (char[] row : matrix) {
        if (isCharArrayPalindrome(row)) {
            count++;
        }
    }
    return count;
}

private static long countPalindromicColumns(char[][] matrix) {
    long count = 0;
    for (int column = 0; column < matrix[0].length; column++) {
        int top = 0;
        int bottom = matrix.length - 1;
        boolean palindrome = true;

        while (top < bottom) {
            if (matrix[top][column] != matrix[bottom][column]) {
                palindrome = false;
                break;
            }
            top++;
            bottom--;
        }

        if (palindrome) {
            count++;
        }
    }
    return count;
}

private static boolean isCharArrayPalindrome(char[] value) {
    int left = 0;
    int right = value.length - 1;
    while (left < right) {
        if (value[left] != value[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- A row palindrome is just a palindrome check on a `char[]`.
- A column palindrome compares mirrored cells vertically.
- This is a good extension problem after mastering string and array palindromes.

### Complexity

- **Time:** `O(r * c)`
- **Space:** `O(1)`

Where `r` is the number of rows and `c` is the number of columns.

---

## 15) Multiple Palindrome Substring Queries Using Rolling Hash

### Question

Preprocess a string so that many queries `[l, r]` can be answered quickly for palindrome status.

### Java Solution

```java
static final class RollingHashPalindromeChecker {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 911_382_323L;

    private final String value;
    private final long[] powers;
    private final long[] prefix;
    private final long[] reversePrefix;

    RollingHashPalindromeChecker(String value) {
        this.value = value == null ? "" : value;
        int n = this.value.length();
        this.powers = new long[n + 1];
        this.prefix = new long[n + 1];
        this.reversePrefix = new long[n + 1];

        powers[0] = 1L;
        String reversed = new StringBuilder(this.value).reverse().toString();

        for (int i = 0; i < n; i++) {
            powers[i + 1] = (powers[i] * BASE) % MOD;
            prefix[i + 1] = (prefix[i] * BASE + this.value.charAt(i)) % MOD;
            reversePrefix[i + 1] = (reversePrefix[i] * BASE + reversed.charAt(i)) % MOD;
        }
    }

    boolean isPalindrome(int left, int right) {
        if (left < 0 || right >= value.length() || left > right) {
            return false;
        }

        long forwardHash = rangeHash(prefix, left, right);
        int reverseLeft = value.length() - 1 - right;
        int reverseRight = value.length() - 1 - left;
        long backwardHash = rangeHash(reversePrefix, reverseLeft, reverseRight);
        return forwardHash == backwardHash;
    }

    private long rangeHash(long[] source, int left, int right) {
        long hash = source[right + 1] - (source[left] * powers[right - left + 1]) % MOD;
        return hash < 0 ? hash + MOD : hash;
    }
}
```

### Explanation

- Precompute prefix hashes for the string and its reverse.
- A substring is a palindrome when its forward hash equals the matching reverse hash.
- This is useful when there are many queries on the same string.

### Complexity

- **Preprocessing Time:** `O(n)`
- **Query Time:** `O(1)`
- **Space:** `O(n)`

> In strict production settings, double hashing is preferred to reduce collision risk.

---

## 16) Split a String Into Exactly Three Palindromic Parts

### Question

Determine whether a string can be split into exactly three palindromic substrings.

### Java Solution

```java
public static boolean canSplitIntoThreePalindromes(String value) {
    if (value == null || value.length() < 3) {
        return false;
    }

    boolean[][] table = buildPalindromeTable(value);

    for (int firstEnd = 0; firstEnd < value.length() - 2; firstEnd++) {
        if (!table[0][firstEnd]) {
            continue;
        }

        for (int secondEnd = firstEnd + 1; secondEnd < value.length() - 1; secondEnd++) {
            if (table[firstEnd + 1][secondEnd]
                    && table[secondEnd + 1][value.length() - 1]) {
                return true;
            }
        }
    }
    return false;
}

private static boolean[][] buildPalindromeTable(String value) {
    int n = value.length();
    boolean[][] table = new boolean[n][n];

    for (int start = n - 1; start >= 0; start--) {
        table[start][start] = true;
        for (int end = start + 1; end < n; end++) {
            table[start][end] = value.charAt(start) == value.charAt(end)
                    && (end - start == 1 || table[start + 1][end - 1]);
        }
    }
    return table;
}
```

### Explanation

- Precompute palindrome status for every substring.
- Try every possible end for the first and second part.
- Check whether all three resulting pieces are palindromes.

### Complexity

- **Time:** `O(n^2)`
- **Space:** `O(n^2)`

---

## 17) Largest Palindromic Number From a String of Digits

### Question

Given a string of digits, build the largest palindromic number possible.

### Java Solution

```java
public static String largestPalindromicNumber(String digits) {
    if (digits == null || digits.isEmpty()) {
        return "";
    }

    int[] counts = new int[10];
    for (char ch : digits.toCharArray()) {
        counts[ch - '0']++;
    }

    StringBuilder left = new StringBuilder();
    for (int digit = 9; digit >= 0; digit--) {
        int pairs = counts[digit] / 2;
        if (digit == 0 && left.length() == 0) {
            continue;
        }
        for (int i = 0; i < pairs; i++) {
            left.append(digit);
        }
        counts[digit] -= pairs * 2;
    }

    int middle = -1;
    for (int digit = 9; digit >= 0; digit--) {
        if (counts[digit] > 0) {
            middle = digit;
            break;
        }
    }

    if (left.length() == 0) {
        if (middle != -1) {
            return Integer.toString(middle);
        }
        return digits.indexOf('0') >= 0 ? "0" : "";
    }

    String leftHalf = left.toString();
    String rightHalf = new StringBuilder(leftHalf).reverse().toString();
    return leftHalf + (middle == -1 ? "" : middle) + rightHalf;
}
```

### Explanation

- Use the largest digits first to maximize the left half.
- Keep one highest remaining digit for the middle if possible.
- Mirror the left half to build the right half.
- Avoid leading zeroes unless the answer is just `"0"`.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)` extra, ignoring output construction

---

## 18) Follow-Up: Palindrome Check for `char[]`

### Question

Solve the palindrome check problem for mutable input such as `char[]`, without using `reverse()`.

### Java Solution

```java
public static boolean isCharArrayPalindrome(char[] value) {
    if (value == null) {
        return false;
    }

    int left = 0;
    int right = value.length - 1;

    while (left < right) {
        if (value[left] != value[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

### Explanation

- This is the same two-pointer pattern as the string version.
- It is a common interview follow-up because it avoids immutable string helpers.
- The idea also generalizes to arrays and lists.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## Quick Interview Notes

### Common patterns you should know

- **Two pointers:** basic string, array, and mutable input palindrome checks
- **Normalization:** ignore spaces, punctuation, or case
- **Expand around center:** longest palindromic substring, count palindromic substrings
- **Dynamic programming:** subsequences, partitioning, minimum cuts
- **Frequency counting:** rearrangement and palindrome construction
- **Reversal of second half:** linked list palindrome
- **Hashing / preprocessing:** fast substring queries

### Common edge cases

- `null` input
- empty string
- single character
- negative numbers
- numbers ending in `0`
- duplicate words in palindrome pair problems
- leading zeroes in numeric palindrome construction

### Where to find the full implementations

The runnable source file already added to the repository contains these methods and more:

- `BasicStringSolutions`
- `NormalizedStringSolutions`
- `ConstraintStringSolutions`
- `NumberPalindromeSolutions`
- `ArrayCollectionSolutions`
- `LinkedListSolutions`
- `SubstringSolutions`
- `DynamicProgrammingSolutions`
- `RearrangementConstructionSolutions`
- `PairingCombinationSolutions`
- `MatrixGridPatternSolutions`
- `HashingQuerySolutions`
- `AdvancedSolutions`
- `InterviewFollowUps`
