# Java Palindrome Question + Solution Pairs (All 113)

This guide expands the original palindrome question bank so every question is
covered one by one.

For brevity, each entry shows either:

- the exact Java method to call from `src/main/java/PalindromeSolutions.java`, or
- a compact Java snippet when the question is more strategy-based than
  utility-method based.

Full runnable implementations already in the repository live in:

- `src/main/java/PalindromeSolutions.java`

---

## 1) Basic String Palindrome Questions

### 1. Write a Java program to check whether a given string is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("level");`
- **Explanation:** Uses two pointers to compare mirrored characters from both ends.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 2. Check if a string is a palindrome using the two-pointer approach.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("radar");`
- **Explanation:** This is the standard two-pointer solution: move inward while the characters match.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 3. Check if a string is a palindrome without using built-in reverse functions.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("madam");`
- **Explanation:** The method never builds a reversed copy, so it avoids extra string creation.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 4. Check if a string is a palindrome using recursion.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindromeRecursive("level");`
- **Explanation:** Recursively compare the outer characters and shrink the range toward the center.
- **Complexity:** Time `O(n)`, Space `O(n)` because of the recursion stack.

### 5. Check if a string is a palindrome using a stack.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindromeWithStack("level");`
- **Explanation:** Push all characters, then compare the original string with the reverse order popped from the stack.
- **Complexity:** Time `O(n)`, Space `O(n)`.

### 6. Check if a character array is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isCharArrayPalindrome(new char[]{'r', 'a', 'd', 'a', 'r'});`
- **Explanation:** The same mirrored two-pointer logic works directly on mutable character arrays.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 7. Return `true` if a string is a palindrome, otherwise return `false`.
- **Java solution:** `boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("civic");`
- **Explanation:** This is the boolean-return form of the basic palindrome check.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 8. Count how many words in a list are palindromes.
- **Java solution:** `long count = PalindromeSolutions.BasicStringSolutions.countPalindromeWords(List.of("level", "java", "madam"));`
- **Explanation:** Iterate through the list and apply the basic palindrome test to each word.
- **Complexity:** Time `O(total_characters)`, Space `O(1)` extra.

---

## 2) Case, Spaces, and Special Character Variants

### 9. Check whether a string is a palindrome ignoring case differences.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeIgnoreCase("Level");`
- **Explanation:** Compare mirrored characters after converting them to the same letter case.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 10. Check whether a sentence is a palindrome ignoring spaces.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeIgnoreSpaces("n u r s e s r u n");`
- **Explanation:** Skip whitespace while comparing from both ends.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 11. Check whether a sentence is a palindrome ignoring spaces and punctuation.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric("Able was I, ere I saw Elba.");`
- **Explanation:** Skip every non-alphanumeric character, which removes both punctuation and spaces from the comparison.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 12. Check whether a string is a palindrome by considering only alphanumeric characters.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric("A man, a plan, a canal: Panama");`
- **Explanation:** This is the standard "valid palindrome" interview variant.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 13. Check whether a Unicode string is a palindrome after normalizing letter case.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isUnicodeNormalizedPalindrome("Level");`
- **Explanation:** Normalize Unicode text first, then compare code points instead of raw UTF-16 chars.
- **Complexity:** Time `O(n)`, Space `O(n)` because normalization and code point conversion create derived data.

### 14. Validate if a phrase like `"A man, a plan, a canal: Panama"` is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric("A man, a plan, a canal: Panama");`
- **Explanation:** Ignore punctuation, spaces, and case so only meaningful mirrored characters remain.
- **Complexity:** Time `O(n)`, Space `O(1)`.

---

## 3) Constraint-Based String Questions

### 15. Check if a string is a palindrome in `O(1)` extra space.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeO1Space("racecar");`
- **Explanation:** Reuse the two-pointer scan so no extra reversed string or stack is needed.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 16. Check if a string is a palindrome without creating another string.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeO1Space("abba");`
- **Explanation:** Compare the original string in place through index access only.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 17. Check if a string is a palindrome using Java Streams.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeStream("level");`
- **Explanation:** Stream over the left half of the indexes and compare each with its mirrored index.
- **Complexity:** Time `O(n)`, Space `O(1)` extra.

### 18. Check if a string is a palindrome using `StringBuilder`, then discuss why it is less optimal.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeWithStringBuilder("level");`
- **Explanation:** This is concise, but it allocates a reversed copy, so it uses more memory than the two-pointer solution.
- **Complexity:** Time `O(n)`, Space `O(n)`.

### 19. Check if only a substring from index `l` to `r` is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.isSubstringPalindrome("abacaba", 1, 5);`
- **Explanation:** Run the same mirrored comparison, but only inside the requested range.
- **Complexity:** Time `O(r - l + 1)`, Space `O(1)`.

### 20. Check if a string can become a palindrome after removing at most one character.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.canBecomePalindromeAfterRemovingAtMostOne("abca");`
- **Explanation:** At the first mismatch, try skipping either the left or the right character once.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 21. Check if a string can become a palindrome after removing exactly one character.
- **Java solution:** `boolean result = PalindromeSolutions.ConstraintStringSolutions.canBecomePalindromeAfterRemovingExactlyOne("abca");`
- **Explanation:** The current implementation tries each possible removal and checks whether the remaining string is a palindrome.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 22. Find the first index whose removal makes the string a palindrome, if possible.
- **Java solution:** `int index = PalindromeSolutions.ConstraintStringSolutions.firstRemovalIndexForPalindrome("cabba");`
- **Explanation:** Test each removal candidate from left to right and return the first one that works.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

---

## 4) Number Palindrome Questions

### 23. Write a Java program to check whether an integer is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeInt(12321);`
- **Explanation:** This variant converts the integer to a string and reuses the basic string palindrome logic.
- **Complexity:** Time `O(d)`, Space `O(d)`, where `d` is the number of digits.

### 24. Check if a number is a palindrome without converting it to a string.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithoutString(12321);`
- **Explanation:** Reverse only half of the number, then compare the remaining half with the reversed half.
- **Complexity:** Time `O(d)`, Space `O(1)`.

### 25. Check if a long integer is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeLong(123454321L);`
- **Explanation:** Uses the same half-reversal technique as the `int` solution, but on `long`.
- **Complexity:** Time `O(d)`, Space `O(1)`.

### 26. Reverse an integer safely and use it to test whether the original number is a palindrome.
- **Java solution:** `OptionalInt reversed = PalindromeSolutions.NumberPalindromeSolutions.reverseIntSafely(12321); boolean result = reversed.isPresent() && reversed.getAsInt() == 12321;`
- **Explanation:** Reverse with overflow protection, then compare the reversed value with the original.
- **Complexity:** Time `O(d)`, Space `O(1)`.

### 27. Check whether a negative number should be treated as a palindrome and justify the rule.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithNegativeRule(-121);`
- **Explanation:** The implementation treats negative numbers as non-palindromes because the minus sign does not mirror on the right side.
- **Complexity:** Time `O(d)`, Space `O(1)`.

### 28. Check whether a number is a palindrome in binary representation.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isBinaryPalindrome(9);`
- **Explanation:** Compare the most significant and least significant bits while moving inward.
- **Complexity:** Time `O(log n)`, Space `O(1)`.

### 29. Check whether a number is a palindrome in any given base `b`.
- **Java solution:** `boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeInBase(585, 2);`
- **Explanation:** Convert the number into base `b` digits, then compare those digits from both ends.
- **Complexity:** Time `O(log_b n)`, Space `O(log_b n)`.

### 30. Count all palindrome numbers in a range `[L, R]`.
- **Java solution:** `long count = PalindromeSolutions.NumberPalindromeSolutions.countPalindromeNumbersInRange(1, 200);`
- **Explanation:** Scan the range and apply the numeric palindrome test to each value.
- **Complexity:** Time `O((R - L + 1) * log R)`, Space `O(1)`.

### 31. Generate all palindrome numbers with `n` digits.
- **Java solution:** `List<Long> values = PalindromeSolutions.NumberPalindromeSolutions.generateNDigitPalindromes(3);`
- **Explanation:** Generate the first half of the digits, then mirror it to build the full palindrome.
- **Complexity:** Time `O(10^(ceil(n / 2)))`, Space `O(10^(ceil(n / 2)))` including output.

### 32. Find the next palindrome number greater than a given integer.
- **Java solution:** `long next = PalindromeSolutions.NumberPalindromeSolutions.nextPalindromeNumber(123);`
- **Explanation:** The current implementation increments the value until it reaches the next palindrome.
- **Complexity:** Time `O(gap * log n)` in the current implementation, where `gap` is the distance to the next palindrome; Space `O(1)`.

### 33. Find the nearest palindrome number to a given integer.
- **Java solution:** `long nearest = PalindromeSolutions.NumberPalindromeSolutions.nearestPalindromeNumber(123);`
- **Explanation:** Search outward on both sides until a palindrome is found, preferring the lower one on ties.
- **Complexity:** Time `O(gap * log n)` in the current implementation; Space `O(1)`.

---

## 5) Array and Collection Palindrome Questions

### 34. Check whether an integer array is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.ArrayCollectionSolutions.isArrayPalindrome(new int[]{1, 2, 3, 2, 1});`
- **Explanation:** Compare the left and right ends of the array while moving inward.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 35. Check whether a generic `List<T>` is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.ArrayCollectionSolutions.isListPalindrome(List.of("a", "b", "a"));`
- **Explanation:** Compare list elements by value with `Objects.equals`.
- **Complexity:** Time `O(n)` and Space `O(1)` assuming random-access lists such as `ArrayList`.

### 36. Check whether an array is a palindrome in-place using two pointers.
- **Java solution:** `boolean result = PalindromeSolutions.ArrayCollectionSolutions.isArrayPalindrome(new int[]{4, 5, 5, 4});`
- **Explanation:** This is the in-place two-pointer version for arrays.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 37. Determine whether a deque of characters forms a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.ArrayCollectionSolutions.isDequePalindrome(new ArrayDeque<>(List.of('n', 'o', 'o', 'n')));`
- **Explanation:** Remove matching elements from the front and the back until the deque is empty or a mismatch appears.
- **Complexity:** Time `O(n)`, Space `O(n)` because the implementation copies the deque before testing it.

### 38. Check whether a list of strings is a palindrome by value comparison.
- **Java solution:** `boolean result = PalindromeSolutions.ArrayCollectionSolutions.isListPalindrome(List.of("red", "blue", "red"));`
- **Explanation:** This is the generic list palindrome check specialized to `String` values.
- **Complexity:** Time `O(n)`, Space `O(1)` assuming random-access lists.

### 39. Count how many subarrays of length `k` are palindromic.
- **Java solution:** `long count = PalindromeSolutions.ArrayCollectionSolutions.countPalindromicSubarrays(new int[]{1, 2, 1, 2, 1}, 3);`
- **Explanation:** Slide a window of length `k` and test each window with a two-pointer palindrome check.
- **Complexity:** Time `O((n - k + 1) * k)`, Space `O(1)`.

### 40. Find the longest palindromic subarray in an integer array.
- **Java solution:** `int[] best = PalindromeSolutions.ArrayCollectionSolutions.longestPalindromicSubarray(new int[]{1, 2, 3, 2, 1, 9});`
- **Explanation:** Expand around every possible array center, just like longest palindromic substring.
- **Complexity:** Time `O(n^2)`, Space `O(1)` extra.

---

## 6) Linked List Palindrome Questions

### 41. Check whether a singly linked list is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 3, 2, 1));`
- **Explanation:** Reverse the second half, compare both halves, then restore the original list.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 42. Check whether a singly linked list is a palindrome using a stack.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeWithStack(PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 1));`
- **Explanation:** Push all node values onto a stack, then compare the popped order with the forward traversal.
- **Complexity:** Time `O(n)`, Space `O(n)`.

### 43. Check whether a singly linked list is a palindrome by reversing the second half.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeByReversingSecondHalf(PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 2, 1));`
- **Explanation:** Find the midpoint with slow/fast pointers, reverse the second half, then compare both halves.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 44. Restore the original linked list after palindrome checking.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 3, 2, 1));`
- **Explanation:** Reverse the second half a second time after comparison so the input list is unchanged.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 45. Check whether a doubly linked list is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isDoublyListPalindrome(PalindromeSolutions.LinkedListSolutions.DoublyNode.of(1, 2, 3, 2, 1));`
- **Explanation:** Walk from the head and the tail toward the center.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 46. Check whether a circular linked list is a palindrome under one full traversal.
- **Java solution:** `boolean result = PalindromeSolutions.LinkedListSolutions.isCircularListPalindrome(PalindromeSolutions.LinkedListSolutions.CircularNode.of(1, 2, 1), 3);`
- **Explanation:** Read exactly one full cycle into a linear list, then use the standard list palindrome test.
- **Complexity:** Time `O(n)`, Space `O(n)`.

---

## 7) Substring-Based Palindrome Questions

### 47. Find the longest palindromic substring in a string.
- **Java solution:** `String best = PalindromeSolutions.SubstringSolutions.longestPalindromicSubstring("forgeeksskeegfor");`
- **Explanation:** Expand around every odd and even center and keep the longest range.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 48. Count all palindromic substrings in a string.
- **Java solution:** `long count = PalindromeSolutions.SubstringSolutions.countPalindromicSubstrings("aaa");`
- **Explanation:** Every successful center expansion contributes one more palindromic substring.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 49. Print all distinct palindromic substrings of a string.
- **Java solution:** `Set<String> values = PalindromeSolutions.SubstringSolutions.distinctPalindromicSubstrings("ababa");`
- **Explanation:** Expand around centers and insert each discovered palindrome into a set so duplicates collapse.
- **Complexity:** Time `O(n^3)` worst case because substring creation is output-sensitive in modern Java, Space `O(n^2)` worst case.

### 50. Find the length of the longest palindromic substring.
- **Java solution:** `int length = PalindromeSolutions.SubstringSolutions.lengthOfLongestPalindromicSubstring("babad");`
- **Explanation:** Reuse the longest-palindromic-substring logic and return only the length.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 51. Return the starting index of the longest palindromic substring.
- **Java solution:** `int index = PalindromeSolutions.SubstringSolutions.startIndexOfLongestPalindromicSubstring("forgeeksskeegfor");`
- **Explanation:** Track the best palindrome range while expanding and return its starting boundary.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 52. Find the longest even-length palindromic substring.
- **Java solution:** `String best = PalindromeSolutions.SubstringSolutions.longestEvenPalindromicSubstring("abccba");`
- **Explanation:** Expand only around center gaps between adjacent characters.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 53. Find the longest odd-length palindromic substring.
- **Java solution:** `String best = PalindromeSolutions.SubstringSolutions.longestOddPalindromicSubstring("bananas");`
- **Explanation:** Expand only around single-character centers.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 54. Find all palindromic substrings longer than length `k`.
- **Java solution:** `List<String> values = PalindromeSolutions.SubstringSolutions.palindromicSubstringsLongerThan("abacdcaba", 2);`
- **Explanation:** Expand around every center and keep only the substrings whose length is greater than `k`.
- **Complexity:** Time `O(n^3)` worst case with substring materialization, Space `O(output)`.

### 55. Count palindromic substrings for multiple test cases efficiently.
- **Java solution:** `List<Long> counts = testCases.stream().map(PalindromeSolutions.SubstringSolutions::countPalindromicSubstrings).toList();`
- **Explanation:** Apply the center-expansion counter to each test case; this is efficient enough for moderate input sizes.
- **Complexity:** Time `O(sum_of_each_case_length^2)`, Space `O(1)` extra per test case.

---

## 8) Subsequence and DP-Based Questions

### 56. Find the length of the longest palindromic subsequence.
- **Java solution:** `int length = PalindromeSolutions.DynamicProgrammingSolutions.longestPalindromicSubsequenceLength("bbbab");`
- **Explanation:** Use dynamic programming where `dp[i][j]` stores the best palindromic subsequence length inside the substring `i..j`.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 57. Print one longest palindromic subsequence.
- **Java solution:** `String lps = PalindromeSolutions.DynamicProgrammingSolutions.oneLongestPalindromicSubsequence("bbbab");`
- **Explanation:** Reconstruct one valid answer by walking the filled DP table from both ends toward the center.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 58. Count the number of palindromic subsequences in a string.
- **Java solution:** `long count = PalindromeSolutions.DynamicProgrammingSolutions.countPalindromicSubsequences("aaa");`
- **Explanation:** DP counts palindromic subsequences by combining answers from smaller ranges and subtracting overlap when needed.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 59. Find the minimum number of insertions needed to make a string a palindrome.
- **Java solution:** `int answer = PalindromeSolutions.DynamicProgrammingSolutions.minInsertionsToPalindrome("abcda");`
- **Explanation:** The minimum insertions equal `length - longest palindromic subsequence length`.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 60. Find the minimum number of deletions needed to make a string a palindrome.
- **Java solution:** `int answer = PalindromeSolutions.DynamicProgrammingSolutions.minDeletionsToPalindrome("abcda");`
- **Explanation:** This uses the same relation as insertions: remove every character not used by an optimal palindromic subsequence.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 61. Find the minimum number of replacements needed to make a string a palindrome.
- **Java solution:** `int answer = PalindromeSolutions.DynamicProgrammingSolutions.minReplacementsToPalindrome("abcdef");`
- **Explanation:** Every mirrored mismatch can be fixed with one replacement, so count mismatched character pairs.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 62. Determine whether a string is a `k`-palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.DynamicProgrammingSolutions.isKPalindrome("abcdecba", 1);`
- **Explanation:** A string is `k`-palindrome when it can become a palindrome after deleting at most `k` characters.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 63. Partition a string into palindromic substrings using dynamic programming.
- **Java solution:** `List<List<String>> parts = PalindromeSolutions.DynamicProgrammingSolutions.palindromePartitions("aab");`
- **Explanation:** Precompute palindrome ranges, then backtrack using that DP table to enumerate valid partitions.
- **Complexity:** Time `O(n^2 + output_size)`, Space `O(n^2 + output_size)`.

### 64. Find the minimum cuts needed for palindrome partitioning.
- **Java solution:** `int cuts = PalindromeSolutions.DynamicProgrammingSolutions.minCutPalindromePartition("aab");`
- **Explanation:** Use a palindrome table plus `cuts[i]`, the fewest cuts needed for the prefix ending at `i`.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 65. Count the number of ways to partition a string so every part is a palindrome.
- **Java solution:** `long ways = PalindromeSolutions.DynamicProgrammingSolutions.countPalindromePartitions("aab");`
- **Explanation:** Dynamic programming accumulates how many valid palindrome partitions start at each index.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

---

## 9) Rearrangement and Construction Questions

### 66. Check whether any permutation of a string can form a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.RearrangementConstructionSolutions.canPermutePalindrome("carrace");`
- **Explanation:** At most one character may have an odd frequency if any permutation is going to be palindromic.
- **Complexity:** Time `O(n log sigma)` in the current `TreeMap` implementation, Space `O(sigma)`.

### 67. Rearrange the characters of a string to form one palindrome, if possible.
- **Java solution:** `String value = PalindromeSolutions.RearrangementConstructionSolutions.buildOnePalindrome("aabbccd");`
- **Explanation:** Put half of each frequency on the left, one odd-frequency character in the middle, and mirror the left half.
- **Complexity:** Time `O(n log sigma)`, Space `O(sigma)`.

### 68. Generate all palindromic permutations of a string.
- **Java solution:** `List<String> values = PalindromeSolutions.RearrangementConstructionSolutions.generatePalindromicPermutations("aabb");`
- **Explanation:** Generate unique permutations of the half-string, then mirror each one to build a full palindrome.
- **Complexity:** Time `O(p * n)`, Space `O(p * n)`, where `p` is the number of generated palindromes.

### 69. Build the longest possible palindrome using the characters of a string.
- **Java solution:** `int length = PalindromeSolutions.RearrangementConstructionSolutions.longestPossiblePalindromeLength("abccccdd");`
- **Explanation:** Use all even counts completely and, if any odd counts exist, place exactly one odd character in the center.
- **Complexity:** Time `O(n log sigma)` in the current implementation, Space `O(sigma)`.

### 70. Build the lexicographically smallest palindrome from the given characters.
- **Java solution:** `String value = PalindromeSolutions.RearrangementConstructionSolutions.lexicographicallySmallestPalindrome("aabbccd");`
- **Explanation:** The implementation relies on sorted character frequencies so the left half is built in ascending order before mirroring.
- **Complexity:** Time `O(n log sigma)`, Space `O(sigma)`.

### 71. Determine the minimum swaps needed to rearrange a string into a palindrome.
- **Java solution (strategy snippet):** `String target = buildTargetPalindrome(value); int swaps = minArbitrarySwaps(source, target);`
- **Explanation:** For arbitrary swaps, first choose a target palindromic arrangement, then compute the minimum swaps needed to transform the source permutation into that target, typically via position mapping and cycle counting.
- **Complexity:** Time `O(n log n)` to `O(n^2)` depending on how duplicates are matched, Space `O(n)`.

### 72. Determine the minimum adjacent swaps needed to make a string a palindrome.
- **Java solution:** `int swaps = PalindromeSolutions.RearrangementConstructionSolutions.minAdjacentSwapsToMakePalindrome("mamad");`
- **Explanation:** Greedily bubble matching characters toward both ends; if no match exists, move the odd middle character inward one step.
- **Complexity:** Time `O(n^2)`, Space `O(1)`.

### 73. Add the minimum number of characters to the end of a string to make it a palindrome.
- **Java solution:** `int count = PalindromeSolutions.RearrangementConstructionSolutions.minCharsToAppendAtEnd("abcd");`
- **Explanation:** Find the earliest suffix that is already a palindrome; everything before it must be appended in reverse.
- **Complexity:** Time `O(n^2)` in the current implementation, Space `O(1)`.

### 74. Add the minimum number of characters to the front of a string to make it a palindrome.
- **Java solution:** `int count = PalindromeSolutions.RearrangementConstructionSolutions.minCharsToAddInFront("aacecaaa");`
- **Explanation:** Compute the longest palindromic prefix, then add the reverse of the remaining suffix in front.
- **Complexity:** Time `O(n)`, Space `O(n)`.

### 75. Construct the shortest palindrome by adding characters in front of the string.
- **Java solution:** `String value = PalindromeSolutions.RearrangementConstructionSolutions.shortestPalindromeByAddingFront("abcd");`
- **Explanation:** This is the constructive form of question 74: reverse the non-palindromic suffix and prepend it.
- **Complexity:** Time `O(n)`, Space `O(n)`.

---

## 10) Pairing and Combination Questions

### 76. Given a list of words, find all pairs whose concatenation is a palindrome.
- **Java solution:** `List<List<Integer>> pairs = PalindromeSolutions.PairingCombinationSolutions.palindromePairs(new String[]{"bat", "tab", "cat"});`
- **Explanation:** Split each word into every possible prefix and suffix, then look up the reversed complement in a hash map.
- **Complexity:** Time `O(n * k^2)`, Space `O(n * k)`.

### 77. Count the number of palindrome pairs in an array of strings.
- **Java solution:** `int count = PalindromeSolutions.PairingCombinationSolutions.countPalindromePairs(new String[]{"bat", "tab", "cat"});`
- **Explanation:** Reuse the palindrome-pair generation logic and return the number of discovered index pairs.
- **Complexity:** Time `O(n * k^2)`, Space `O(n * k)`.

### 78. Check whether two given strings can be combined to form a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.PairingCombinationSolutions.canCombineToPalindrome("abc", "cba");`
- **Explanation:** Test both concatenation orders because either `first + second` or `second + first` may be the palindrome.
- **Complexity:** Time `O(n + m)`, Space `O(n + m)` in the current string-based implementation.

### 79. Find the longest palindrome that can be formed by concatenating two strings.
- **Java solution:** `String best = PalindromeSolutions.PairingCombinationSolutions.longestPalindromeFromConcatenatingTwoStrings("abaxy", "zyxf");`
- **Explanation:** The current implementation checks both concatenation orders and returns the longest palindromic substring found inside them.
- **Complexity:** Time `O((n + m)^2)`, Space `O(1)` extra beyond substring creation.

### 80. Build the longest palindrome from a list of two-letter words.
- **Java solution:** `int length = PalindromeSolutions.PairingCombinationSolutions.longestPalindromeFromTwoLetterWords(new String[]{"lc", "cl", "gg"});`
- **Explanation:** Pair a word with its reverse to contribute `4`, and optionally place one symmetric word like `"gg"` in the center.
- **Complexity:** Time `O(w)`, Space `O(w)`, where `w` is the number of words.

---

## 11) Matrix, Grid, and Pattern Variants

### 81. Check whether each row of a character matrix is a palindrome.
- **Java solution:** `long rows = PalindromeSolutions.MatrixGridPatternSolutions.countPalindromicRows(matrix);`
- **Explanation:** Test every row as a `char[]` palindrome and count how many succeed.
- **Complexity:** Time `O(r * c)`, Space `O(1)`.

### 82. Check whether each column of a matrix is a palindrome.
- **Java solution:** `long cols = PalindromeSolutions.MatrixGridPatternSolutions.countPalindromicColumns(matrix);`
- **Explanation:** Compare mirrored cells from top and bottom for each column independently.
- **Complexity:** Time `O(r * c)`, Space `O(1)`.

### 83. Count palindromic rows and palindromic columns in a matrix.
- **Java solution:** `long total = PalindromeSolutions.MatrixGridPatternSolutions.countPalindromicRowsAndColumns(matrix);`
- **Explanation:** Sum the number of palindromic rows and the number of palindromic columns.
- **Complexity:** Time `O(r * c)`, Space `O(1)`.

### 84. Determine whether a path string formed in a grid is a palindrome.
- **Java solution:** `boolean result = PalindromeSolutions.MatrixGridPatternSolutions.isGridPathPalindrome("abccba");`
- **Explanation:** Once the path labels are collected into a string, this reduces to the ordinary string palindrome check.
- **Complexity:** Time `O(path_length)`, Space `O(1)` extra after the path string exists.

### 85. Find all palindromic diagonals in a square matrix.
- **Java solution:** `List<String> values = PalindromeSolutions.MatrixGridPatternSolutions.palindromicDiagonals(matrix);`
- **Explanation:** Collect diagonals in both directions and keep only the ones whose diagonal string reads the same forward and backward.
- **Complexity:** Time `O(r * c * min(r, c))` in the current construction-heavy approach, Space `O(output)`.

---

## 12) Hashing, Queries, and Large Input Questions

### 86. Answer multiple palindrome substring queries efficiently.
- **Java solution:** `var checker = new PalindromeSolutions.HashingQuerySolutions.RollingHashPalindromeChecker("racecar"); boolean result = checker.isPalindrome(1, 5);`
- **Explanation:** Preprocess rolling hashes once, then answer each palindrome substring query in constant time.
- **Complexity:** Preprocessing `O(n)`, Query `O(1)`, Space `O(n)`.

### 87. Preprocess a string so each query `[l, r]` can be checked for palindrome status quickly.
- **Java solution:** `var checker = new PalindromeSolutions.HashingQuerySolutions.RollingHashPalindromeChecker("abacaba");`
- **Explanation:** The preprocessing step builds forward hashes, reverse hashes, and powers of the base.
- **Complexity:** Preprocessing `O(n)`, Space `O(n)`.

### 88. Use rolling hash to check whether substrings are palindromes.
- **Java solution:** `boolean result = new PalindromeSolutions.HashingQuerySolutions.RollingHashPalindromeChecker("abacaba").isPalindrome(2, 4);`
- **Explanation:** Compare the substring hash with the corresponding reversed-range hash.
- **Complexity:** Preprocessing `O(n)`, Query `O(1)`, Space `O(n)`.

### 89. Support updates to characters and answer palindrome range queries.
- **Java solution:** `var engine = new PalindromeSolutions.HashingQuerySolutions.MutablePalindromeQueryEngine("racecar"); engine.update(3, 'e'); boolean result = engine.isPalindrome(0, 6);`
- **Explanation:** The current implementation rebuilds the rolling-hash structure after every update, then answers range queries through hashing.
- **Complexity:** Update `O(n)`, Query `O(1)`, Space `O(n)`.

### 90. Check whether a very large string is a palindrome when it cannot fit fully in memory.
- **Java solution:** `boolean result = PalindromeSolutions.HashingQuerySolutions.isLargeAsciiFilePalindrome(Path.of("huge.txt"));`
- **Explanation:** Use random access to compare bytes from the beginning and end of the file without loading the entire contents into RAM.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 91. Check whether a stream of incoming characters currently forms a palindrome.
- **Java solution:** `var stream = new PalindromeSolutions.HashingQuerySolutions.StreamPalindromeChecker(); stream.append('r'); stream.append('a'); stream.append('d'); stream.append('a'); stream.append('r'); boolean result = stream.isCurrentPalindrome();`
- **Explanation:** Append incoming characters incrementally and test whether the currently collected string is a palindrome.
- **Complexity:** Append `O(1)` amortized, current palindrome check `O(n)`, Space `O(n)`.

### 92. Design a data structure that supports append and palindrome-check operations.
- **Java solution:** `var engine = new PalindromeSolutions.HashingQuerySolutions.MutablePalindromeQueryEngine("ab"); engine.append('a'); boolean result = engine.isPalindrome(0, engine.currentValue().length() - 1);`
- **Explanation:** This data structure supports appends, optional indexed updates, and fast palindrome queries over the maintained string.
- **Complexity:** Append `O(n)` in the current rebuild-based implementation, Query `O(1)`, Space `O(n)`.

---

## 13) Advanced Interview and Competitive Coding Questions

### 93. Find the shortest palindrome by adding characters only at the front.
- **Java solution:** `String value = PalindromeSolutions.RearrangementConstructionSolutions.shortestPalindromeByAddingFront("abcd");`
- **Explanation:** This is the same optimized KMP-based construction used in question 75.
- **Complexity:** Time `O(n)`, Space `O(n)`.

### 94. Find the longest palindrome that can be formed from a multiset of characters.
- **Java solution:** `int length = PalindromeSolutions.RearrangementConstructionSolutions.longestPossiblePalindromeLength("abccccdd");`
- **Explanation:** A multiset version is frequency-based: use all even counts and possibly one odd count in the center.
- **Complexity:** Time `O(n log sigma)` in the current implementation, Space `O(sigma)`.

### 95. Find the maximum product of lengths of two disjoint palindromic subsequences.
- **Java solution:** `int answer = PalindromeSolutions.AdvancedSolutions.maxProductOfTwoDisjointPalindromicSubsequences("leetcodecom");`
- **Explanation:** Enumerate subsequences by bitmask, record which masks form palindromes, then combine disjoint masks for the best product.
- **Complexity:** Time `O(n * 2^n)`, Space `O(2^n)`, practical only for short strings.

### 96. Count "super palindromes" where both the number and its square are palindromes.
- **Java solution:** `int count = PalindromeSolutions.AdvancedSolutions.countSuperPalindromes(1L, 100000L);`
- **Explanation:** Generate palindromic roots directly, square them, and test whether the square is also palindromic.
- **Complexity:** Time depends on the number of generated palindromic roots up to `sqrt(R)`; each test is logarithmic in the numeric value. Extra space is `O(1)`.

### 97. Find the largest palindromic number that can be formed from the digits of a string.
- **Java solution:** `String value = PalindromeSolutions.AdvancedSolutions.largestPalindromicNumber("444947137");`
- **Explanation:** Build the left half greedily from the largest digits, keep the largest leftover digit for the center, and mirror the left half.
- **Complexity:** Time `O(n)`, Space `O(1)` extra beyond output.

### 98. Find the smallest palindromic number larger than a given numeric string.
- **Java solution:** `String value = PalindromeSolutions.AdvancedSolutions.smallestPalindromicNumberLargerThan("23545");`
- **Explanation:** Mirror the left half to the right; if the result is not strictly larger, increment the middle and propagate carry outward.
- **Complexity:** Time `O(n)`, Space `O(n)` for the character array and returned string.

### 99. Determine whether a string can be split into exactly three palindromic substrings.
- **Java solution:** `boolean result = PalindromeSolutions.AdvancedSolutions.canSplitIntoThreePalindromes("abcbdd");`
- **Explanation:** Precompute palindrome ranges and try every valid first and second cut.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

### 100. Find all ways to partition a string into exactly `k` palindromic parts.
- **Java solution:** `List<List<String>> parts = PalindromeSolutions.AdvancedSolutions.partitionsIntoKPalindromes("aab", 2);`
- **Explanation:** Use the palindrome DP table with backtracking, but stop recursion after exactly `k` parts.
- **Complexity:** Time `O(n^2 + output_size)`, Space `O(n^2 + output_size)`.

### 101. Given a string, maximize palindrome length after at most `k` character changes.
- **Java solution:** `int length = PalindromeSolutions.AdvancedSolutions.maxPalindromeLengthAfterAtMostKChanges("abcdef", 2);`
- **Explanation:** Each change can fix one mismatched mirrored pair, so the current implementation counts mismatches and measures how much of the string can be made palindromic.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 102. Given two strings, find the longest palindromic subsequence using characters from both.
- **Java solution:** `int length = PalindromeSolutions.AdvancedSolutions.longestPalindromicSubsequenceUsingBothStrings("cacb", "cbba");`
- **Explanation:** Run LPS DP on the concatenated string, but only accept subsequences that start in the first string and end in the second.
- **Complexity:** Time `O((n + m)^2)`, Space `O((n + m)^2)`.

### 103. Count palindromic paths in a tree or graph where labels are characters.
- **Java solution (strategy snippet):** `int count = countPseudoPalindromicPaths(root, 0);`
- **Explanation:** A common tree variant tracks the parity of character counts along each root-to-node path with a bitmask; a path can form a palindrome if at most one bit is set in the final mask. For general graphs, add visited-state handling to avoid cycles.
- **Complexity:** Tree version `O(V + E)` time and `O(H)` recursion space, where `H` is tree height. General graphs depend on traversal constraints.

### 104. Check whether a sentence remains a palindrome after applying a series of character updates.
- **Java solution:** `var engine = new PalindromeSolutions.HashingQuerySolutions.MutablePalindromeQueryEngine("neveroddoreven"); engine.update(5, 'x'); boolean result = engine.isPalindrome(0, engine.currentValue().length() - 1);`
- **Explanation:** After each update, rebuild the query structure and test the full current range. If the interview ignores punctuation or spaces, normalize the sentence before storing it.
- **Complexity:** Update `O(n)`, Query `O(1)`, Space `O(n)`.

### 105. Find the minimum operations needed to transform one string into a palindrome.
- **Java solution:** `int ops = PalindromeSolutions.AdvancedSolutions.minOperationsToTransformToPalindrome("abcda");`
- **Explanation:** In this repository, "operations" are modeled as insertions, which is the classic DP interview version.
- **Complexity:** Time `O(n^2)`, Space `O(n^2)`.

---

## 14) Popular Follow-Up Variations for Interviews

### 106. Solve the basic palindrome problem first, then optimize for `O(1)` extra space.
- **Java solution:** `boolean result = PalindromeSolutions.InterviewFollowUps.isPalindromeO1Space("level");`
- **Explanation:** The optimized answer is the two-pointer scan, which avoids stacks, recursion, or reversed copies.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 107. Solve palindrome checking without using library helpers such as `reverse()`.
- **Java solution:** `boolean result = PalindromeSolutions.InterviewFollowUps.isPalindromeNoLibraryHelpers("radar");`
- **Explanation:** Compare the original string directly from both ends instead of calling helper APIs.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 108. Solve the same problem for mutable input such as `char[]`.
- **Java solution:** `boolean result = PalindromeSolutions.InterviewFollowUps.isPalindromeMutable(new char[]{'n', 'o', 'o', 'n'});`
- **Explanation:** The same mirrored comparison works on mutable arrays and is a common follow-up in interviews.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 109. Explain the trade-offs between iterative, recursive, stack-based, and stream-based solutions.
- **Java solution:** `boolean a = PalindromeSolutions.BasicStringSolutions.isPalindrome("level"); boolean b = PalindromeSolutions.BasicStringSolutions.isPalindromeRecursive("level"); boolean c = PalindromeSolutions.BasicStringSolutions.isPalindromeWithStack("level"); boolean d = PalindromeSolutions.ConstraintStringSolutions.isPalindromeStream("level");`
- **Explanation:** Iterative two pointers are usually best for interviews because they are simple and `O(1)` space. Recursion is elegant but uses the call stack. Stack-based solutions are easy to reason about but use extra memory. Streams are concise but usually less direct and less performance-oriented.
- **Complexity:** Iterative `O(n)/O(1)`, Recursive `O(n)/O(n)`, Stack `O(n)/O(n)`, Stream `O(n)/O(1)` extra.

### 110. Modify the solution to ignore case, spaces, punctuation, or all non-alphanumeric characters.
- **Java solution:** `boolean result = PalindromeSolutions.InterviewFollowUps.isPalindromeIgnoringNoise("A man, a plan, a canal: Panama");`
- **Explanation:** Normalize the comparison by skipping irrelevant characters and lowercasing letters before comparing.
- **Complexity:** Time `O(n)`, Space `O(1)`.

### 111. Extend the solution from strings to arrays, lists, and linked lists.
- **Java solution:** `boolean arrayOk = PalindromeSolutions.ArrayCollectionSolutions.isArrayPalindrome(new int[]{1, 2, 1}); boolean listOk = PalindromeSolutions.ArrayCollectionSolutions.isListPalindrome(List.of("x", "y", "x")); boolean linkedOk = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 1));`
- **Explanation:** The core palindrome idea stays the same: compare mirrored positions. Only the access pattern changes depending on the data structure.
- **Complexity:** Arrays/lists `O(n)` time, linked lists `O(n)` time; extra space ranges from `O(1)` to `O(n)` depending on the chosen linked-list technique.

### 112. Optimize from brute force to dynamic programming for substring and subsequence problems.
- **Java solution:** `String bestSubstring = PalindromeSolutions.SubstringSolutions.longestPalindromicSubstring("babad"); int bestSubsequence = PalindromeSolutions.DynamicProgrammingSolutions.longestPalindromicSubsequenceLength("bbbab");`
- **Explanation:** Brute force checks every candidate range or subsequence and quickly becomes too slow. For substrings, center expansion reduces unnecessary checks. For subsequences and partitioning, dynamic programming reuses overlapping subproblems.
- **Complexity:** Brute-force substring approaches are typically `O(n^3)` or worse; optimized substring and DP subsequence solutions are `O(n^2)`.

### 113. Discuss edge cases such as empty strings, single characters, null input, negative numbers, and overflow.
- **Java solution:** `boolean empty = PalindromeSolutions.BasicStringSolutions.isPalindrome(""); boolean single = PalindromeSolutions.BasicStringSolutions.isPalindrome("a"); boolean negative = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithNegativeRule(-121); OptionalInt reversed = PalindromeSolutions.NumberPalindromeSolutions.reverseIntSafely(Integer.MAX_VALUE);`
- **Explanation:** Production-ready solutions should define clear behavior for `null`, accept empty and single-character palindromes where appropriate, reject negative numeric palindromes under the signed-number rule, and guard integer reversal against overflow.
- **Complexity:** Edge-case handling adds `O(1)` overhead on top of the main algorithm.
