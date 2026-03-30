import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.file.Path;
import java.text.Normalizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Objects;
import java.util.OptionalInt;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.IntStream;

public final class PalindromeSolutions {
    private PalindromeSolutions() {
    }

    public static void main(String[] args) {
        System.out.println("1. Basic string palindrome: "
                + BasicStringSolutions.isPalindrome("level"));
        System.out.println("2. Ignore punctuation: "
                + NormalizedStringSolutions.isPalindromeAlphaNumeric("A man, a plan, a canal: Panama"));
        System.out.println("3. Remove one character: "
                + ConstraintStringSolutions.canBecomePalindromeAfterRemovingAtMostOne("abca"));
        System.out.println("4. Number palindrome: "
                + NumberPalindromeSolutions.isPalindromeWithoutString(12321));
        System.out.println("5. Array palindrome: "
                + ArrayCollectionSolutions.isArrayPalindrome(new int[]{1, 2, 3, 2, 1}));
        System.out.println("6. Linked list palindrome: "
                + LinkedListSolutions.isPalindromeAndRestore(LinkedListSolutions.SinglyNode.of(1, 2, 3, 2, 1)));
        System.out.println("7. Longest palindromic substring: "
                + SubstringSolutions.longestPalindromicSubstring("forgeeksskeegfor"));
        System.out.println("8. Longest palindromic subsequence length: "
                + DynamicProgrammingSolutions.longestPalindromicSubsequenceLength("bbbab"));
        System.out.println("9. One rearranged palindrome: "
                + RearrangementConstructionSolutions.buildOnePalindrome("aabbccd"));
        System.out.println("10. Palindrome pairs: "
                + PairingCombinationSolutions.palindromePairs(new String[]{"bat", "tab", "cat"}));
        System.out.println("11. Palindromic rows and columns: "
                + MatrixGridPatternSolutions.countPalindromicRowsAndColumns(new char[][]{
                        {'a', 'b', 'a'},
                        {'c', 'd', 'c'},
                        {'a', 'b', 'a'}
                }));
        HashingQuerySolutions.RollingHashPalindromeChecker checker =
                new HashingQuerySolutions.RollingHashPalindromeChecker("racecar");
        System.out.println("12. Query [1, 5] is palindrome: " + checker.isPalindrome(1, 5));
        System.out.println("13. Split into three palindromes: "
                + AdvancedSolutions.canSplitIntoThreePalindromes("abcbdd"));
        System.out.println("14. Char[] follow-up palindrome: "
                + InterviewFollowUps.isPalindromeMutable(new char[]{'r', 'a', 'd', 'a', 'r'}));
    }

    private static String reverse(String value) {
        return new StringBuilder(value).reverse().toString();
    }

    private static long pow10(int exponent) {
        long value = 1L;
        for (int i = 0; i < exponent; i++) {
            value *= 10L;
        }
        return value;
    }

    private static boolean isPalindromeRange(CharSequence value, int left, int right) {
        if (value == null) {
            return false;
        }
        while (left < right) {
            if (value.charAt(left) != value.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private static boolean isPalindromeRange(int[] values, int left, int right) {
        if (values == null) {
            return false;
        }
        while (left < right) {
            if (values[left] != values[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private static int[] expandAroundCenter(String value, int left, int right) {
        while (left >= 0 && right < value.length() && value.charAt(left) == value.charAt(right)) {
            left--;
            right++;
        }
        return new int[]{left + 1, right - 1};
    }

    private static int[] expandAroundCenter(int[] values, int left, int right) {
        while (left >= 0 && right < values.length && values[left] == values[right]) {
            left--;
            right++;
        }
        return new int[]{left + 1, right - 1};
    }

    private static int rangeLength(int[] range) {
        return range[1] - range[0] + 1;
    }

    private static int[] longerRange(int[] current, int[] candidate) {
        return rangeLength(candidate) > rangeLength(current) ? candidate : current;
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

    private static int[][] buildLongestPalindromicSubsequenceTable(String value) {
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
        return dp;
    }

    public static final class BasicStringSolutions {
        private BasicStringSolutions() {
        }

        public static boolean isPalindrome(String value) {
            return isPalindromeRange(value, 0, value == null ? -1 : value.length() - 1);
        }

        public static boolean isPalindromeRecursive(String value) {
            if (value == null) {
                return false;
            }
            return isPalindromeRecursive(value, 0, value.length() - 1);
        }

        private static boolean isPalindromeRecursive(String value, int left, int right) {
            if (left >= right) {
                return true;
            }
            return value.charAt(left) == value.charAt(right)
                    && isPalindromeRecursive(value, left + 1, right - 1);
        }

        public static boolean isPalindromeWithStack(String value) {
            if (value == null) {
                return false;
            }
            Deque<Character> stack = new ArrayDeque<>();
            for (char ch : value.toCharArray()) {
                stack.push(ch);
            }
            for (int index = 0; index < value.length(); index++) {
                if (value.charAt(index) != stack.pop()) {
                    return false;
                }
            }
            return true;
        }

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

        public static long countPalindromeWords(List<String> words) {
            if (words == null) {
                return 0L;
            }
            long count = 0L;
            for (String word : words) {
                if (isPalindrome(word)) {
                    count++;
                }
            }
            return count;
        }
    }

    public static final class NormalizedStringSolutions {
        private NormalizedStringSolutions() {
        }

        public static boolean isPalindromeIgnoreCase(String value) {
            if (value == null) {
                return false;
            }
            int left = 0;
            int right = value.length() - 1;
            while (left < right) {
                if (Character.toLowerCase(value.charAt(left))
                        != Character.toLowerCase(value.charAt(right))) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }

        public static boolean isPalindromeIgnoreSpaces(String value) {
            if (value == null) {
                return false;
            }
            int left = 0;
            int right = value.length() - 1;
            while (left < right) {
                while (left < right && Character.isWhitespace(value.charAt(left))) {
                    left++;
                }
                while (left < right && Character.isWhitespace(value.charAt(right))) {
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

        public static boolean isUnicodeNormalizedPalindrome(String value) {
            if (value == null) {
                return false;
            }
            String normalized = Normalizer.normalize(value, Normalizer.Form.NFKC)
                    .toLowerCase(Locale.ROOT);
            int[] codePoints = normalized.codePoints().toArray();
            int left = 0;
            int right = codePoints.length - 1;
            while (left < right) {
                if (codePoints[left] != codePoints[right]) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
    }

    public static final class ConstraintStringSolutions {
        private ConstraintStringSolutions() {
        }

        public static boolean isPalindromeO1Space(String value) {
            return BasicStringSolutions.isPalindrome(value);
        }

        public static boolean isPalindromeStream(String value) {
            if (value == null) {
                return false;
            }
            return IntStream.range(0, value.length() / 2)
                    .allMatch(index -> value.charAt(index)
                            == value.charAt(value.length() - 1 - index));
        }

        public static boolean isPalindromeWithStringBuilder(String value) {
            if (value == null) {
                return false;
            }
            return value.contentEquals(new StringBuilder(value).reverse());
        }

        public static boolean isSubstringPalindrome(String value, int left, int right) {
            if (value == null || left < 0 || right >= value.length() || left > right) {
                return false;
            }
            return isPalindromeRange(value, left, right);
        }

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

        public static boolean canBecomePalindromeAfterRemovingExactlyOne(String value) {
            return firstRemovalIndexForPalindrome(value) != -1;
        }

        public static int firstRemovalIndexForPalindrome(String value) {
            if (value == null) {
                return -1;
            }
            for (int index = 0; index < value.length(); index++) {
                if (isPalindromeAfterRemovingIndex(value, index)) {
                    return index;
                }
            }
            return -1;
        }

        private static boolean isPalindromeAfterRemovingIndex(String value, int skipIndex) {
            int left = 0;
            int right = value.length() - 1;
            while (left < right) {
                if (left == skipIndex) {
                    left++;
                    continue;
                }
                if (right == skipIndex) {
                    right--;
                    continue;
                }
                if (value.charAt(left) != value.charAt(right)) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
    }

    public static final class NumberPalindromeSolutions {
        private NumberPalindromeSolutions() {
        }

        public static boolean isPalindromeInt(int value) {
            return value >= 0 && BasicStringSolutions.isPalindrome(Integer.toString(value));
        }

        public static boolean isPalindromeWithNegativeRule(int value) {
            return value >= 0 && isPalindromeWithoutString(value);
        }

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

        public static boolean isPalindromeLong(long value) {
            if (value < 0 || (value % 10 == 0 && value != 0)) {
                return false;
            }
            long reversedHalf = 0L;
            while (value > reversedHalf) {
                reversedHalf = reversedHalf * 10 + value % 10;
                value /= 10;
            }
            return value == reversedHalf || value == reversedHalf / 10;
        }

        public static OptionalInt reverseIntSafely(int value) {
            long current = Math.abs((long) value);
            long reversed = 0L;
            while (current > 0) {
                reversed = reversed * 10 + current % 10;
                current /= 10;
            }
            if (value < 0) {
                reversed = -reversed;
            }
            if (reversed < Integer.MIN_VALUE || reversed > Integer.MAX_VALUE) {
                return OptionalInt.empty();
            }
            return OptionalInt.of((int) reversed);
        }

        public static boolean isBinaryPalindrome(int value) {
            if (value < 0) {
                return false;
            }
            if (value == 0) {
                return true;
            }
            int left = 31 - Integer.numberOfLeadingZeros(value);
            int right = 0;
            while (left > right) {
                int leftBit = (value >> left) & 1;
                int rightBit = (value >> right) & 1;
                if (leftBit != rightBit) {
                    return false;
                }
                left--;
                right++;
            }
            return true;
        }

        public static boolean isPalindromeInBase(long value, int base) {
            if (value < 0 || base < 2) {
                return false;
            }
            List<Integer> digits = new ArrayList<>();
            if (value == 0) {
                digits.add(0);
            }
            while (value > 0) {
                digits.add((int) (value % base));
                value /= base;
            }
            int left = 0;
            int right = digits.size() - 1;
            while (left < right) {
                if (!digits.get(left).equals(digits.get(right))) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }

        public static long countPalindromeNumbersInRange(long left, long right) {
            if (left > right) {
                return 0L;
            }
            long count = 0L;
            for (long value = Math.max(0L, left); value <= right; value++) {
                if (isPalindromeLong(value)) {
                    count++;
                }
            }
            return count;
        }

        public static List<Long> generateNDigitPalindromes(int digits) {
            if (digits <= 0 || digits > 18) {
                return List.of();
            }
            int halfLength = (digits + 1) / 2;
            long start = digits == 1 ? 0L : pow10(halfLength - 1);
            long end = pow10(halfLength) - 1;
            List<Long> palindromes = new ArrayList<>();
            for (long half = start; half <= end; half++) {
                String firstHalf = Long.toString(half);
                String mirrorSource = digits % 2 == 0
                        ? firstHalf
                        : firstHalf.substring(0, firstHalf.length() - 1);
                palindromes.add(Long.parseLong(firstHalf + reverse(mirrorSource)));
            }
            return palindromes;
        }

        public static long nextPalindromeNumber(long value) {
            long candidate = Math.max(0L, value + 1L);
            while (!isPalindromeLong(candidate)) {
                candidate++;
            }
            return candidate;
        }

        public static long nearestPalindromeNumber(long value) {
            if (value < 0) {
                return 0L;
            }
            if (isPalindromeLong(value)) {
                return value;
            }
            for (long delta = 1L; ; delta++) {
                long lower = value - delta;
                if (lower >= 0 && isPalindromeLong(lower)) {
                    return lower;
                }
                long upper = value + delta;
                if (isPalindromeLong(upper)) {
                    return upper;
                }
            }
        }
    }

    public static final class ArrayCollectionSolutions {
        private ArrayCollectionSolutions() {
        }

        public static boolean isArrayPalindrome(int[] values) {
            return isPalindromeRange(values, 0, values == null ? -1 : values.length - 1);
        }

        public static <T> boolean isListPalindrome(List<T> values) {
            if (values == null) {
                return false;
            }
            int left = 0;
            int right = values.size() - 1;
            while (left < right) {
                if (!Objects.equals(values.get(left), values.get(right))) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }

        public static boolean isDequePalindrome(Deque<Character> values) {
            if (values == null) {
                return false;
            }
            Deque<Character> copy = new ArrayDeque<>(values);
            while (copy.size() > 1) {
                Character first = copy.pollFirst();
                Character last = copy.pollLast();
                if (!Objects.equals(first, last)) {
                    return false;
                }
            }
            return true;
        }

        public static long countPalindromicSubarrays(int[] values, int k) {
            if (values == null || k <= 0 || k > values.length) {
                return 0L;
            }
            long count = 0L;
            for (int start = 0; start + k - 1 < values.length; start++) {
                if (isPalindromeRange(values, start, start + k - 1)) {
                    count++;
                }
            }
            return count;
        }

        public static int[] longestPalindromicSubarray(int[] values) {
            if (values == null || values.length == 0) {
                return new int[0];
            }
            int[] best = new int[]{0, 0};
            for (int center = 0; center < values.length; center++) {
                best = longerRange(best, expandAroundCenter(values, center, center));
                best = longerRange(best, expandAroundCenter(values, center, center + 1));
            }
            return Arrays.copyOfRange(values, best[0], best[1] + 1);
        }
    }

    public static final class LinkedListSolutions {
        private LinkedListSolutions() {
        }

        public static final class SinglyNode {
            public final int value;
            public SinglyNode next;

            public SinglyNode(int value) {
                this.value = value;
            }

            public static SinglyNode of(int... values) {
                if (values == null || values.length == 0) {
                    return null;
                }
                SinglyNode head = new SinglyNode(values[0]);
                SinglyNode tail = head;
                for (int index = 1; index < values.length; index++) {
                    tail.next = new SinglyNode(values[index]);
                    tail = tail.next;
                }
                return head;
            }
        }

        public static final class DoublyNode {
            public final int value;
            public DoublyNode prev;
            public DoublyNode next;

            public DoublyNode(int value) {
                this.value = value;
            }

            public static DoublyNode of(int... values) {
                if (values == null || values.length == 0) {
                    return null;
                }
                DoublyNode head = new DoublyNode(values[0]);
                DoublyNode tail = head;
                for (int index = 1; index < values.length; index++) {
                    DoublyNode node = new DoublyNode(values[index]);
                    node.prev = tail;
                    tail.next = node;
                    tail = node;
                }
                return head;
            }
        }

        public static final class CircularNode {
            public final int value;
            public CircularNode next;

            public CircularNode(int value) {
                this.value = value;
            }

            public static CircularNode of(int... values) {
                if (values == null || values.length == 0) {
                    return null;
                }
                CircularNode head = new CircularNode(values[0]);
                CircularNode tail = head;
                for (int index = 1; index < values.length; index++) {
                    tail.next = new CircularNode(values[index]);
                    tail = tail.next;
                }
                tail.next = head;
                return head;
            }
        }

        public static boolean isPalindromeWithStack(SinglyNode head) {
            Deque<Integer> stack = new ArrayDeque<>();
            for (SinglyNode current = head; current != null; current = current.next) {
                stack.push(current.value);
            }
            for (SinglyNode current = head; current != null; current = current.next) {
                if (current.value != stack.pop()) {
                    return false;
                }
            }
            return true;
        }

        public static boolean isPalindromeByReversingSecondHalf(SinglyNode head) {
            return isPalindromeByReversingSecondHalf(head, true);
        }

        public static boolean isPalindromeAndRestore(SinglyNode head) {
            return isPalindromeByReversingSecondHalf(head, true);
        }

        private static boolean isPalindromeByReversingSecondHalf(SinglyNode head, boolean restore) {
            if (head == null || head.next == null) {
                return true;
            }
            SinglyNode slow = head;
            SinglyNode fast = head;
            while (fast.next != null && fast.next.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            SinglyNode reversedSecondHalf = reverseList(slow.next);
            SinglyNode reversedHead = reversedSecondHalf;
            SinglyNode firstHalf = head;
            boolean matches = true;
            while (reversedSecondHalf != null) {
                if (firstHalf.value != reversedSecondHalf.value) {
                    matches = false;
                    break;
                }
                firstHalf = firstHalf.next;
                reversedSecondHalf = reversedSecondHalf.next;
            }
            if (restore) {
                slow.next = reverseList(reversedHead);
            }
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

        public static boolean isDoublyListPalindrome(DoublyNode head) {
            if (head == null) {
                return true;
            }
            DoublyNode tail = head;
            while (tail.next != null) {
                tail = tail.next;
            }
            DoublyNode left = head;
            DoublyNode right = tail;
            while (left != right && right.next != left) {
                if (left.value != right.value) {
                    return false;
                }
                left = left.next;
                right = right.prev;
            }
            return true;
        }

        public static boolean isCircularListPalindrome(CircularNode head, int length) {
            if (head == null) {
                return true;
            }
            if (length < 0) {
                return false;
            }
            List<Integer> values = new ArrayList<>(length);
            CircularNode current = head;
            for (int index = 0; index < length; index++) {
                values.add(current.value);
                current = current.next;
            }
            return ArrayCollectionSolutions.isListPalindrome(values);
        }
    }

    public static final class SubstringSolutions {
        private SubstringSolutions() {
        }

        public static String longestPalindromicSubstring(String value) {
            if (value == null || value.isEmpty()) {
                return "";
            }
            int[] best = new int[]{0, 0};
            for (int center = 0; center < value.length(); center++) {
                best = longerRange(best, expandAroundCenter(value, center, center));
                best = longerRange(best, expandAroundCenter(value, center, center + 1));
            }
            return value.substring(best[0], best[1] + 1);
        }

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
            while (left >= 0 && right < value.length() && value.charAt(left) == value.charAt(right)) {
                count++;
                left--;
                right++;
            }
            return count;
        }

        public static Set<String> distinctPalindromicSubstrings(String value) {
            if (value == null) {
                return Set.of();
            }
            Set<String> result = new LinkedHashSet<>();
            for (int center = 0; center < value.length(); center++) {
                collectFromCenter(value, center, center, result);
                collectFromCenter(value, center, center + 1, result);
            }
            return result;
        }

        private static void collectFromCenter(String value, int left, int right, Set<String> result) {
            while (left >= 0 && right < value.length() && value.charAt(left) == value.charAt(right)) {
                result.add(value.substring(left, right + 1));
                left--;
                right++;
            }
        }

        public static int lengthOfLongestPalindromicSubstring(String value) {
            return longestPalindromicSubstring(value).length();
        }

        public static int startIndexOfLongestPalindromicSubstring(String value) {
            if (value == null || value.isEmpty()) {
                return -1;
            }
            int[] best = new int[]{0, 0};
            for (int center = 0; center < value.length(); center++) {
                best = longerRange(best, expandAroundCenter(value, center, center));
                best = longerRange(best, expandAroundCenter(value, center, center + 1));
            }
            return best[0];
        }

        public static String longestEvenPalindromicSubstring(String value) {
            if (value == null || value.isEmpty()) {
                return "";
            }
            int[] best = new int[]{0, -1};
            for (int center = 0; center < value.length(); center++) {
                best = longerRange(best, expandAroundCenter(value, center, center + 1));
            }
            return best[1] < best[0] ? "" : value.substring(best[0], best[1] + 1);
        }

        public static String longestOddPalindromicSubstring(String value) {
            if (value == null || value.isEmpty()) {
                return "";
            }
            int[] best = new int[]{0, 0};
            for (int center = 0; center < value.length(); center++) {
                best = longerRange(best, expandAroundCenter(value, center, center));
            }
            return value.substring(best[0], best[1] + 1);
        }

        public static List<String> palindromicSubstringsLongerThan(String value, int k) {
            if (value == null) {
                return List.of();
            }
            Set<String> result = new LinkedHashSet<>();
            for (int center = 0; center < value.length(); center++) {
                collectLongerSubstrings(value, center, center, k, result);
                collectLongerSubstrings(value, center, center + 1, k, result);
            }
            return new ArrayList<>(result);
        }

        private static void collectLongerSubstrings(
                String value, int left, int right, int k, Set<String> result) {
            while (left >= 0 && right < value.length() && value.charAt(left) == value.charAt(right)) {
                if (right - left + 1 > k) {
                    result.add(value.substring(left, right + 1));
                }
                left--;
                right++;
            }
        }
    }

    public static final class DynamicProgrammingSolutions {
        private DynamicProgrammingSolutions() {
        }

        public static int longestPalindromicSubsequenceLength(String value) {
            if (value == null || value.isEmpty()) {
                return 0;
            }
            return buildLongestPalindromicSubsequenceTable(value)[0][value.length() - 1];
        }

        public static String oneLongestPalindromicSubsequence(String value) {
            if (value == null || value.isEmpty()) {
                return "";
            }
            int[][] dp = buildLongestPalindromicSubsequenceTable(value);
            char[] result = new char[dp[0][value.length() - 1]];
            int left = 0;
            int right = result.length - 1;
            int start = 0;
            int end = value.length() - 1;
            while (start <= end) {
                if (start == end) {
                    result[left] = value.charAt(start);
                    break;
                }
                if (value.charAt(start) == value.charAt(end)) {
                    result[left++] = value.charAt(start);
                    result[right--] = value.charAt(end);
                    start++;
                    end--;
                } else if (dp[start + 1][end] >= dp[start][end - 1]) {
                    start++;
                } else {
                    end--;
                }
            }
            return new String(result);
        }

        public static long countPalindromicSubsequences(String value) {
            if (value == null || value.isEmpty()) {
                return 0L;
            }
            int n = value.length();
            long[][] dp = new long[n][n];
            for (int start = n - 1; start >= 0; start--) {
                dp[start][start] = 1L;
                for (int end = start + 1; end < n; end++) {
                    if (value.charAt(start) == value.charAt(end)) {
                        dp[start][end] = dp[start + 1][end] + dp[start][end - 1] + 1L;
                    } else {
                        long overlap = start + 1 <= end - 1 ? dp[start + 1][end - 1] : 0L;
                        dp[start][end] = dp[start + 1][end] + dp[start][end - 1] - overlap;
                    }
                }
            }
            return dp[0][n - 1];
        }

        public static int minInsertionsToPalindrome(String value) {
            if (value == null) {
                return 0;
            }
            return value.length() - longestPalindromicSubsequenceLength(value);
        }

        public static int minDeletionsToPalindrome(String value) {
            return minInsertionsToPalindrome(value);
        }

        public static int minReplacementsToPalindrome(String value) {
            if (value == null) {
                return 0;
            }
            int left = 0;
            int right = value.length() - 1;
            int replacements = 0;
            while (left < right) {
                if (value.charAt(left) != value.charAt(right)) {
                    replacements++;
                }
                left++;
                right--;
            }
            return replacements;
        }

        public static boolean isKPalindrome(String value, int k) {
            return minDeletionsToPalindrome(value) <= k;
        }

        public static List<List<String>> palindromePartitions(String value) {
            if (value == null) {
                return List.of();
            }
            boolean[][] table = buildPalindromeTable(value);
            List<List<String>> result = new ArrayList<>();
            collectPartitions(value, 0, table, new ArrayList<>(), result);
            return result;
        }

        private static void collectPartitions(
                String value,
                int start,
                boolean[][] table,
                List<String> path,
                List<List<String>> result) {
            if (start == value.length()) {
                result.add(new ArrayList<>(path));
                return;
            }
            for (int end = start; end < value.length(); end++) {
                if (table[start][end]) {
                    path.add(value.substring(start, end + 1));
                    collectPartitions(value, end + 1, table, path, result);
                    path.remove(path.size() - 1);
                }
            }
        }

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

        public static long countPalindromePartitions(String value) {
            if (value == null) {
                return 0L;
            }
            boolean[][] table = buildPalindromeTable(value);
            long[] ways = new long[value.length() + 1];
            ways[value.length()] = 1L;
            for (int start = value.length() - 1; start >= 0; start--) {
                for (int end = start; end < value.length(); end++) {
                    if (table[start][end]) {
                        ways[start] += ways[end + 1];
                    }
                }
            }
            return ways[0];
        }
    }

    public static final class RearrangementConstructionSolutions {
        private RearrangementConstructionSolutions() {
        }

        public static boolean canPermutePalindrome(String value) {
            if (value == null) {
                return false;
            }
            Map<Character, Integer> counts = buildSortedFrequencyMap(value);
            int oddCount = 0;
            for (int count : counts.values()) {
                if ((count & 1) == 1) {
                    oddCount++;
                }
            }
            return oddCount <= 1;
        }

        public static String buildOnePalindrome(String value) {
            if (value == null) {
                return "";
            }
            Map<Character, Integer> counts = buildSortedFrequencyMap(value);
            int oddCount = 0;
            Character middle = null;
            StringBuilder half = new StringBuilder();
            for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
                if ((entry.getValue() & 1) == 1) {
                    oddCount++;
                    middle = entry.getKey();
                }
                for (int index = 0; index < entry.getValue() / 2; index++) {
                    half.append(entry.getKey());
                }
            }
            if (oddCount > 1) {
                return "";
            }
            String leftHalf = half.toString();
            return leftHalf + (middle == null ? "" : middle) + reverse(leftHalf);
        }

        public static List<String> generatePalindromicPermutations(String value) {
            if (value == null) {
                return List.of();
            }
            String palindrome = buildOnePalindrome(value);
            if (palindrome.isEmpty() && !value.isEmpty()) {
                return List.of();
            }
            Map<Character, Integer> counts = buildSortedFrequencyMap(value);
            StringBuilder halfBuilder = new StringBuilder();
            String middle = "";
            for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
                if ((entry.getValue() & 1) == 1) {
                    middle = Character.toString(entry.getKey());
                }
                for (int index = 0; index < entry.getValue() / 2; index++) {
                    halfBuilder.append(entry.getKey());
                }
            }
            char[] half = halfBuilder.toString().toCharArray();
            Arrays.sort(half);
            List<String> result = new ArrayList<>();
            buildHalfPermutations(half, new boolean[half.length], new StringBuilder(), middle, result);
            return result;
        }

        private static void buildHalfPermutations(
                char[] half,
                boolean[] used,
                StringBuilder path,
                String middle,
                List<String> result) {
            if (path.length() == half.length) {
                String left = path.toString();
                result.add(left + middle + reverse(left));
                return;
            }
            for (int index = 0; index < half.length; index++) {
                if (used[index]) {
                    continue;
                }
                if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
                    continue;
                }
                used[index] = true;
                path.append(half[index]);
                buildHalfPermutations(half, used, path, middle, result);
                path.deleteCharAt(path.length() - 1);
                used[index] = false;
            }
        }

        private static Map<Character, Integer> buildSortedFrequencyMap(String value) {
            Map<Character, Integer> counts = new TreeMap<>();
            for (char ch : value.toCharArray()) {
                counts.merge(ch, 1, Integer::sum);
            }
            return counts;
        }

        public static int longestPossiblePalindromeLength(String value) {
            if (value == null) {
                return 0;
            }
            Map<Character, Integer> counts = buildSortedFrequencyMap(value);
            int length = 0;
            boolean usedCenter = false;
            for (int count : counts.values()) {
                length += (count / 2) * 2;
                if ((count & 1) == 1 && !usedCenter) {
                    usedCenter = true;
                }
            }
            return length + (usedCenter ? 1 : 0);
        }

        public static String lexicographicallySmallestPalindrome(String value) {
            return buildOnePalindrome(value);
        }

        public static int minAdjacentSwapsToMakePalindrome(String value) {
            if (value == null) {
                return -1;
            }
            if (!canPermutePalindrome(value)) {
                return -1;
            }
            char[] chars = value.toCharArray();
            int left = 0;
            int right = chars.length - 1;
            int swaps = 0;
            while (left < right) {
                int match = right;
                while (match > left && chars[match] != chars[left]) {
                    match--;
                }
                if (match == left) {
                    swap(chars, left, left + 1);
                    swaps++;
                } else {
                    while (match < right) {
                        swap(chars, match, match + 1);
                        swaps++;
                        match++;
                    }
                    left++;
                    right--;
                }
            }
            return swaps;
        }

        private static void swap(char[] chars, int left, int right) {
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
        }

        public static int minCharsToAppendAtEnd(String value) {
            if (value == null) {
                return 0;
            }
            for (int start = 0; start < value.length(); start++) {
                if (isPalindromeRange(value, start, value.length() - 1)) {
                    return start;
                }
            }
            return value.length();
        }

        public static String shortestPalindromeByAppendingEnd(String value) {
            if (value == null) {
                return "";
            }
            int toAppend = minCharsToAppendAtEnd(value);
            return value + reverse(value.substring(0, toAppend));
        }

        public static int minCharsToAddInFront(String value) {
            if (value == null) {
                return 0;
            }
            return value.length() - longestPalindromicPrefixLength(value);
        }

        public static String shortestPalindromeByAddingFront(String value) {
            if (value == null) {
                return "";
            }
            int prefixLength = longestPalindromicPrefixLength(value);
            String suffix = value.substring(prefixLength);
            return reverse(suffix) + value;
        }

        private static int longestPalindromicPrefixLength(String value) {
            String combined = value + "#" + reverse(value);
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
    }

    public static final class PairingCombinationSolutions {
        private PairingCombinationSolutions() {
        }

        public static List<List<Integer>> palindromePairs(String[] words) {
            if (words == null) {
                return List.of();
            }
            String[] normalized = new String[words.length];
            Map<String, List<Integer>> positions = new HashMap<>();
            for (int index = 0; index < words.length; index++) {
                normalized[index] = words[index] == null ? "" : words[index];
                positions.computeIfAbsent(normalized[index], key -> new ArrayList<>()).add(index);
            }

            List<List<Integer>> result = new ArrayList<>();
            Set<String> seen = new LinkedHashSet<>();
            for (int index = 0; index < normalized.length; index++) {
                String word = normalized[index];
                for (int cut = 0; cut <= word.length(); cut++) {
                    String prefix = word.substring(0, cut);
                    String suffix = word.substring(cut);

                    if (isPalindromeRange(prefix, 0, prefix.length() - 1)) {
                        addPairs(positions.get(reverse(suffix)), index, true, seen, result);
                    }
                    if (cut != word.length() && isPalindromeRange(suffix, 0, suffix.length() - 1)) {
                        addPairs(positions.get(reverse(prefix)), index, false, seen, result);
                    }
                }
            }
            return result;
        }

        private static void addPairs(
                List<Integer> matches,
                int currentIndex,
                boolean prepend,
                Set<String> seen,
                List<List<Integer>> result) {
            if (matches == null) {
                return;
            }
            for (int matchIndex : matches) {
                if (matchIndex == currentIndex) {
                    continue;
                }
                int left = prepend ? matchIndex : currentIndex;
                int right = prepend ? currentIndex : matchIndex;
                String key = left + ":" + right;
                if (seen.add(key)) {
                    result.add(List.of(left, right));
                }
            }
        }

        public static int countPalindromePairs(String[] words) {
            return palindromePairs(words).size();
        }

        public static boolean canCombineToPalindrome(String first, String second) {
            if (first == null || second == null) {
                return false;
            }
            return BasicStringSolutions.isPalindrome(first + second)
                    || BasicStringSolutions.isPalindrome(second + first);
        }

        public static String longestPalindromeFromConcatenatingTwoStrings(String first, String second) {
            if (first == null || second == null) {
                return "";
            }
            String candidateOne = SubstringSolutions.longestPalindromicSubstring(first + second);
            String candidateTwo = SubstringSolutions.longestPalindromicSubstring(second + first);
            return candidateOne.length() >= candidateTwo.length() ? candidateOne : candidateTwo;
        }

        public static int longestPalindromeFromTwoLetterWords(String[] words) {
            if (words == null) {
                return 0;
            }
            Map<String, Integer> counts = new HashMap<>();
            for (String word : words) {
                String normalized = word == null ? "" : word;
                counts.merge(normalized, 1, Integer::sum);
            }
            int length = 0;
            boolean hasCenter = false;
            Set<String> visited = new HashSet<>();
            for (Map.Entry<String, Integer> entry : counts.entrySet()) {
                String word = entry.getKey();
                if (visited.contains(word) || word.length() != 2) {
                    continue;
                }
                String reversed = reverse(word);
                if (word.equals(reversed)) {
                    length += (entry.getValue() / 2) * 4;
                    if ((entry.getValue() & 1) == 1) {
                        hasCenter = true;
                    }
                } else if (counts.containsKey(reversed)) {
                    length += Math.min(entry.getValue(), counts.get(reversed)) * 4;
                    visited.add(reversed);
                }
                visited.add(word);
            }
            return length + (hasCenter ? 2 : 0);
        }
    }

    public static final class MatrixGridPatternSolutions {
        private MatrixGridPatternSolutions() {
        }

        public static long countPalindromicRows(char[][] matrix) {
            validateRectangularMatrix(matrix);
            if (matrix == null) {
                return 0L;
            }
            long count = 0L;
            for (char[] row : matrix) {
                if (BasicStringSolutions.isCharArrayPalindrome(row)) {
                    count++;
                }
            }
            return count;
        }

        public static long countPalindromicColumns(char[][] matrix) {
            validateRectangularMatrix(matrix);
            if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
                return 0L;
            }
            long count = 0L;
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

        public static long countPalindromicRowsAndColumns(char[][] matrix) {
            return countPalindromicRows(matrix) + countPalindromicColumns(matrix);
        }

        public static boolean isGridPathPalindrome(String path) {
            return BasicStringSolutions.isPalindrome(path);
        }

        public static List<String> palindromicDiagonals(char[][] matrix) {
            validateRectangularMatrix(matrix);
            if (matrix == null || matrix.length == 0) {
                return List.of();
            }
            List<String> result = new ArrayList<>();
            int rows = matrix.length;
            int cols = matrix[0].length;

            for (int col = 0; col < cols; col++) {
                addDiagonalIfPalindrome(matrix, 0, col, 1, 1, "NW-SE", result);
            }
            for (int row = 1; row < rows; row++) {
                addDiagonalIfPalindrome(matrix, row, 0, 1, 1, "NW-SE", result);
            }
            for (int col = 0; col < cols; col++) {
                addDiagonalIfPalindrome(matrix, 0, col, 1, -1, "NE-SW", result);
            }
            for (int row = 1; row < rows; row++) {
                addDiagonalIfPalindrome(matrix, row, cols - 1, 1, -1, "NE-SW", result);
            }
            return result;
        }

        private static void addDiagonalIfPalindrome(
                char[][] matrix, int row, int col, int rowStep, int colStep,
                String direction, List<String> result) {
            StringBuilder diagonal = new StringBuilder();
            while (row >= 0 && row < matrix.length && col >= 0 && col < matrix[0].length) {
                diagonal.append(matrix[row][col]);
                row += rowStep;
                col += colStep;
            }
            String value = diagonal.toString();
            if (BasicStringSolutions.isPalindrome(value)) {
                result.add(direction + ":" + value);
            }
        }

        private static void validateRectangularMatrix(char[][] matrix) {
            if (matrix == null || matrix.length == 0) {
                return;
            }
            int width = matrix[0].length;
            for (char[] row : matrix) {
                if (row == null || row.length != width) {
                    throw new IllegalArgumentException("Matrix must be rectangular.");
                }
            }
        }
    }

    public static final class HashingQuerySolutions {
        private HashingQuerySolutions() {
        }

        public static final class RollingHashPalindromeChecker {
            private static final long MOD = 1_000_000_007L;
            private static final long BASE = 911_382_323L;

            private final String value;
            private final long[] powers;
            private final long[] prefix;
            private final long[] reversePrefix;

            public RollingHashPalindromeChecker(String value) {
                this.value = value == null ? "" : value;
                int n = this.value.length();
                this.powers = new long[n + 1];
                this.prefix = new long[n + 1];
                this.reversePrefix = new long[n + 1];
                powers[0] = 1L;
                String reversed = reverse(this.value);
                for (int index = 0; index < n; index++) {
                    powers[index + 1] = (powers[index] * BASE) % MOD;
                    prefix[index + 1] = (prefix[index] * BASE + this.value.charAt(index)) % MOD;
                    reversePrefix[index + 1] = (reversePrefix[index] * BASE + reversed.charAt(index)) % MOD;
                }
            }

            public boolean isPalindrome(int left, int right) {
                if (left < 0 || right >= value.length() || left > right) {
                    return false;
                }
                long forwardHash = rangeHash(prefix, left, right);
                int reverseLeft = value.length() - 1 - right;
                int reverseRight = value.length() - 1 - left;
                long reverseHash = rangeHash(reversePrefix, reverseLeft, reverseRight);
                return forwardHash == reverseHash;
            }

            private long rangeHash(long[] source, int left, int right) {
                long hash = source[right + 1] - (source[left] * powers[right - left + 1]) % MOD;
                if (hash < 0) {
                    hash += MOD;
                }
                return hash;
            }
        }

        public static final class MutablePalindromeQueryEngine {
            private char[] value;
            private RollingHashPalindromeChecker checker;

            public MutablePalindromeQueryEngine(String initialValue) {
                this.value = (initialValue == null ? "" : initialValue).toCharArray();
                rebuild();
            }

            public void update(int index, char newValue) {
                if (index < 0 || index >= value.length) {
                    throw new IndexOutOfBoundsException("Index out of range: " + index);
                }
                value[index] = newValue;
                rebuild();
            }

            public void append(char newValue) {
                char[] updated = Arrays.copyOf(value, value.length + 1);
                updated[updated.length - 1] = newValue;
                value = updated;
                rebuild();
            }

            public boolean isPalindrome(int left, int right) {
                return checker.isPalindrome(left, right);
            }

            public String currentValue() {
                return new String(value);
            }

            private void rebuild() {
                checker = new RollingHashPalindromeChecker(new String(value));
            }
        }

        public static boolean isLargeAsciiFilePalindrome(Path path) throws IOException {
            try (RandomAccessFile file = new RandomAccessFile(path.toFile(), "r")) {
                long left = 0L;
                long right = file.length() - 1;
                while (left < right) {
                    file.seek(left);
                    int leftByte = file.read();
                    file.seek(right);
                    int rightByte = file.read();
                    if (leftByte != rightByte) {
                        return false;
                    }
                    left++;
                    right--;
                }
                return true;
            }
        }

        public static final class StreamPalindromeChecker {
            private final StringBuilder builder = new StringBuilder();

            public void append(char value) {
                builder.append(value);
            }

            public boolean isCurrentPalindrome() {
                return BasicStringSolutions.isPalindrome(builder.toString());
            }

            public String currentValue() {
                return builder.toString();
            }
        }
    }

    public static final class AdvancedSolutions {
        private AdvancedSolutions() {
        }

        public static int maxProductOfTwoDisjointPalindromicSubsequences(String value) {
            if (value == null || value.isEmpty()) {
                return 0;
            }
            if (value.length() > 20) {
                throw new IllegalArgumentException("Use a shorter string for the bitmask solution.");
            }
            int totalMasks = 1 << value.length();
            int[] palindromeLength = new int[totalMasks];
            for (int mask = 1; mask < totalMasks; mask++) {
                StringBuilder subsequence = new StringBuilder();
                for (int index = 0; index < value.length(); index++) {
                    if ((mask & (1 << index)) != 0) {
                        subsequence.append(value.charAt(index));
                    }
                }
                if (BasicStringSolutions.isPalindrome(subsequence.toString())) {
                    palindromeLength[mask] = subsequence.length();
                }
            }
            int[] bestSubset = Arrays.copyOf(palindromeLength, palindromeLength.length);
            for (int bit = 0; bit < value.length(); bit++) {
                for (int mask = 0; mask < totalMasks; mask++) {
                    if ((mask & (1 << bit)) != 0) {
                        bestSubset[mask] = Math.max(bestSubset[mask], bestSubset[mask ^ (1 << bit)]);
                    }
                }
            }
            int answer = 0;
            int all = totalMasks - 1;
            for (int mask = 1; mask < totalMasks; mask++) {
                if (palindromeLength[mask] == 0) {
                    continue;
                }
                answer = Math.max(answer, palindromeLength[mask] * bestSubset[all ^ mask]);
            }
            return answer;
        }

        public static int countSuperPalindromes(long left, long right) {
            if (left > right) {
                return 0;
            }
            int count = 0;
            long limit = (long) Math.sqrt(right);
            for (long half = 1L; ; half++) {
                long palindrome = buildNumericPalindromeFromHalf(half, true);
                if (palindrome > limit) {
                    break;
                }
                long square = palindrome * palindrome;
                if (square >= left && square <= right && NumberPalindromeSolutions.isPalindromeLong(square)) {
                    count++;
                }
            }
            for (long half = 1L; ; half++) {
                long palindrome = buildNumericPalindromeFromHalf(half, false);
                if (palindrome > limit) {
                    break;
                }
                long square = palindrome * palindrome;
                if (square >= left && square <= right && NumberPalindromeSolutions.isPalindromeLong(square)) {
                    count++;
                }
            }
            return count;
        }

        private static long buildNumericPalindromeFromHalf(long half, boolean oddLength) {
            long palindrome = half;
            if (oddLength) {
                half /= 10L;
            }
            while (half > 0) {
                palindrome = palindrome * 10L + half % 10L;
                half /= 10L;
            }
            return palindrome;
        }

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
                for (int index = 0; index < pairs; index++) {
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
            String right = reverse(leftHalf);
            return leftHalf + (middle == -1 ? "" : Integer.toString(middle)) + right;
        }

        public static String smallestPalindromicNumberLargerThan(String numeric) {
            if (numeric == null || numeric.isEmpty()) {
                return "";
            }
            if (numeric.chars().allMatch(ch -> ch == '9')) {
                return "1" + "0".repeat(Math.max(0, numeric.length() - 1)) + "1";
            }
            char[] candidate = numeric.toCharArray();
            for (int left = 0; left < candidate.length / 2; left++) {
                candidate[candidate.length - 1 - left] = candidate[left];
            }
            if (compare(candidate, numeric.toCharArray()) > 0) {
                return new String(candidate);
            }
            int middle = (candidate.length - 1) / 2;
            int carry = 1;
            while (middle >= 0 && carry > 0) {
                int digit = (candidate[middle] - '0') + carry;
                candidate[middle] = (char) ('0' + (digit % 10));
                carry = digit / 10;
                candidate[candidate.length - 1 - middle] = candidate[middle];
                middle--;
            }
            if (carry > 0) {
                return "1" + "0".repeat(Math.max(0, numeric.length() - 1)) + "1";
            }
            for (int left = 0; left < candidate.length / 2; left++) {
                candidate[candidate.length - 1 - left] = candidate[left];
            }
            return new String(candidate);
        }

        private static int compare(char[] left, char[] right) {
            for (int index = 0; index < left.length; index++) {
                if (left[index] != right[index]) {
                    return left[index] - right[index];
                }
            }
            return 0;
        }

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
                    if (table[firstEnd + 1][secondEnd] && table[secondEnd + 1][value.length() - 1]) {
                        return true;
                    }
                }
            }
            return false;
        }

        public static List<List<String>> partitionsIntoKPalindromes(String value, int k) {
            if (value == null || k <= 0) {
                return List.of();
            }
            boolean[][] table = buildPalindromeTable(value);
            List<List<String>> result = new ArrayList<>();
            collectKPartitions(value, 0, k, table, new ArrayList<>(), result);
            return result;
        }

        private static void collectKPartitions(
                String value,
                int start,
                int remainingParts,
                boolean[][] table,
                List<String> path,
                List<List<String>> result) {
            if (start == value.length()) {
                if (remainingParts == 0) {
                    result.add(new ArrayList<>(path));
                }
                return;
            }
            if (remainingParts == 0) {
                return;
            }
            for (int end = start; end < value.length(); end++) {
                if (table[start][end]) {
                    path.add(value.substring(start, end + 1));
                    collectKPartitions(value, end + 1, remainingParts - 1, table, path, result);
                    path.remove(path.size() - 1);
                }
            }
        }

        public static int maxPalindromeLengthAfterAtMostKChanges(String value, int k) {
            if (value == null) {
                return 0;
            }
            int mismatches = 0;
            int left = 0;
            int right = value.length() - 1;
            while (left < right) {
                if (value.charAt(left) != value.charAt(right)) {
                    mismatches++;
                }
                left++;
                right--;
            }
            if (k >= mismatches) {
                return value.length();
            }
            return Math.max(0, value.length() - 2 * (mismatches - k));
        }

        public static int longestPalindromicSubsequenceUsingBothStrings(String first, String second) {
            if (first == null || second == null || first.isEmpty() || second.isEmpty()) {
                return 0;
            }
            String combined = first + second;
            int split = first.length();
            int[][] dp = buildLongestPalindromicSubsequenceTable(combined);
            int answer = 0;
            for (int left = 0; left < split; left++) {
                for (int right = split; right < combined.length(); right++) {
                    if (combined.charAt(left) == combined.charAt(right)) {
                        int inside = left + 1 <= right - 1 ? dp[left + 1][right - 1] : 0;
                        answer = Math.max(answer, 2 + inside);
                    }
                }
            }
            return answer;
        }

        public static int minOperationsToTransformToPalindrome(String value) {
            return DynamicProgrammingSolutions.minInsertionsToPalindrome(value);
        }
    }

    public static final class InterviewFollowUps {
        private InterviewFollowUps() {
        }

        public static boolean isPalindromeO1Space(String value) {
            return ConstraintStringSolutions.isPalindromeO1Space(value);
        }

        public static boolean isPalindromeNoLibraryHelpers(String value) {
            return BasicStringSolutions.isPalindrome(value);
        }

        public static boolean isPalindromeMutable(char[] value) {
            return BasicStringSolutions.isCharArrayPalindrome(value);
        }

        public static boolean isPalindromeIgnoringNoise(String value) {
            return NormalizedStringSolutions.isPalindromeAlphaNumeric(value);
        }

        public static boolean isNullEmptyOrSingleCharacterPalindrome(String value) {
            return value != null && BasicStringSolutions.isPalindrome(value);
        }

        public static boolean isNonNegativeNumberPalindrome(int value) {
            return NumberPalindromeSolutions.isPalindromeWithNegativeRule(value);
        }
    }
}
