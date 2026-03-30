from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path("/workspace")
MARKDOWN_PATH = ROOT / "PALINDROME_JAVA_ANSWER_BOOK.md"
PDF_PATH = ROOT / "PALINDROME_JAVA_ANSWER_BOOK.pdf"


@dataclass(frozen=True)
class QuestionEntry:
    number: int
    question: str
    answer: str
    java_solution: str
    complexity: str
    optimized: str


@dataclass(frozen=True)
class Section:
    title: str
    entries: List[QuestionEntry]


def _entry(
    number: int,
    question: str,
    answer: str,
    java_solution: str,
    complexity: str,
    optimized: str,
) -> QuestionEntry:
    return QuestionEntry(
        number=number,
        question=question,
        answer=answer,
        java_solution=java_solution,
        complexity=complexity,
        optimized=optimized,
    )


SECTIONS: List[Section] = [
    Section(
        "1) Basic String Palindrome Questions",
        [
            _entry(
                1,
                "Write a Java program to check whether a given string is a palindrome.",
                "Use two pointers, one at the beginning and one at the end. Compare mirrored characters while moving inward. If a mismatch appears, the string is not a palindrome; otherwise it is.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("level");""",
                "Time O(n), Space O(1).",
                "The two-pointer solution is already the optimized interview answer because it avoids building a reversed copy.",
            ),
            _entry(
                2,
                "Check if a string is a palindrome using the two-pointer approach.",
                "The two-pointer approach compares the leftmost and rightmost characters, then shrinks the range toward the center. It is simple, fast, and works in constant extra space.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("radar");""",
                "Time O(n), Space O(1).",
                "This is the optimized approach for ordinary string palindrome checking.",
            ),
            _entry(
                3,
                "Check if a string is a palindrome without using built-in reverse functions.",
                "Avoid reverse helpers entirely and compare the string in place using indexes. That keeps the algorithm memory-efficient and easy to explain.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("madam");""",
                "Time O(n), Space O(1).",
                "Compared with StringBuilder.reverse(), this avoids allocating another string and is more optimal in space.",
            ),
            _entry(
                4,
                "Check if a string is a palindrome using recursion.",
                "Recursively compare the outer characters and continue with the inner substring. The recursion ends successfully once the left index crosses the right index.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindromeRecursive("level");""",
                "Time O(n), Space O(n) due to recursion stack.",
                "An optimized alternative is the iterative two-pointer method, which keeps the same time complexity but reduces space to O(1).",
            ),
            _entry(
                5,
                "Check if a string is a palindrome using a stack.",
                "Push all characters onto a stack, then compare the original left-to-right order with the reverse order obtained by popping from the stack.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindromeWithStack("level");""",
                "Time O(n), Space O(n).",
                "The optimized alternative is the two-pointer method, which drops the stack and uses O(1) extra space.",
            ),
            _entry(
                6,
                "Check if a character array is a palindrome.",
                "Treat the array exactly like a string and compare `char[]` values from both ends. Because arrays are mutable, this also works well when interviews avoid String helpers.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isCharArrayPalindrome(
    new char[]{'r', 'a', 'd', 'a', 'r'}
);""",
                "Time O(n), Space O(1).",
                "The two-pointer scan is already optimal here.",
            ),
            _entry(
                7,
                "Return `true` if a string is a palindrome, otherwise return `false`.",
                "This is just the boolean form of the standard palindrome check. The same mirrored comparison logic applies.",
                """boolean result = PalindromeSolutions.BasicStringSolutions.isPalindrome("civic");""",
                "Time O(n), Space O(1).",
                "The optimized answer is still the in-place two-pointer comparison.",
            ),
            _entry(
                8,
                "Count how many words in a list are palindromes.",
                "Iterate over the list and test each word with the basic palindrome checker. Increase the count whenever a word is palindromic.",
                """long count = PalindromeSolutions.BasicStringSolutions.countPalindromeWords(
    List.of("level", "java", "madam")
);""",
                "Time O(total characters across all words), Space O(1) extra.",
                "If the list is very large, the main optimization is to reuse the same two-pointer logic on each word instead of constructing reversed copies.",
            ),
        ],
    ),
    Section(
        "2) Case, Spaces, and Special Character Variants",
        [
            _entry(
                9,
                "Check whether a string is a palindrome ignoring case differences.",
                "Convert mirrored characters to the same case before comparing them. This preserves the original string while making the comparison case-insensitive.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeIgnoreCase("Level");""",
                "Time O(n), Space O(1).",
                "The optimized approach lowercases only the characters being compared instead of creating a fully lowercased copy first.",
            ),
            _entry(
                10,
                "Check whether a sentence is a palindrome ignoring spaces.",
                "Skip whitespace while moving the left and right pointers inward. Only non-space characters participate in the comparison.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeIgnoreSpaces(
    "n u r s e s r u n"
);""",
                "Time O(n), Space O(1).",
                "Skipping spaces during comparison is more space-efficient than building a cleaned intermediate string.",
            ),
            _entry(
                11,
                "Check whether a sentence is a palindrome ignoring spaces and punctuation.",
                "Skip all characters that are not letters or digits, then compare the remaining meaningful characters in a case-insensitive way.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric(
    "Able was I, ere I saw Elba."
);""",
                "Time O(n), Space O(1).",
                "The optimized method avoids generating a sanitized string and instead filters characters on the fly.",
            ),
            _entry(
                12,
                "Check whether a string is a palindrome by considering only alphanumeric characters.",
                "This is the classic valid-palindrome problem. Ignore every non-alphanumeric character and compare the rest from both ends.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric(
    "A man, a plan, a canal: Panama"
);""",
                "Time O(n), Space O(1).",
                "On-the-fly filtering is the optimized approach compared with building a cleaned copy first.",
            ),
            _entry(
                13,
                "Check whether a Unicode string is a palindrome after normalizing letter case.",
                "Normalize the input to a standard Unicode form, convert it to lowercase, then compare code points rather than raw UTF-16 code units so the logic handles broader character sets correctly.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isUnicodeNormalizedPalindrome("Level");""",
                "Time O(n), Space O(n).",
                "An optimized interview answer may skip full Unicode handling unless the question explicitly asks for it. For ASCII-only input, the simpler two-pointer lowercase comparison is lighter.",
            ),
            _entry(
                14,
                'Validate if a phrase like `"A man, a plan, a canal: Panama"` is a palindrome.',
                "Ignore case, spaces, and punctuation so that only the important letters and digits are compared in mirrored positions.",
                """boolean result = PalindromeSolutions.NormalizedStringSolutions.isPalindromeAlphaNumeric(
    "A man, a plan, a canal: Panama"
);""",
                "Time O(n), Space O(1).",
                "This is already the optimized practical approach for phrase-style palindrome validation.",
            ),
        ],
    ),
    Section(
        "3) Constraint-Based String Questions",
        [
            _entry(
                15,
                "Check if a string is a palindrome in `O(1)` extra space.",
                "Use only indexes and compare the original string directly. No auxiliary stack, array, or reversed string is needed.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeO1Space("racecar");""",
                "Time O(n), Space O(1).",
                "This question explicitly asks for the optimized approach, and the two-pointer scan is that answer.",
            ),
            _entry(
                16,
                "Check if a string is a palindrome without creating another string.",
                "The simplest way is to compare the existing string in place using left and right indexes. That avoids copy construction entirely.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeO1Space("abba");""",
                "Time O(n), Space O(1).",
                "This is more optimal than reversing with StringBuilder because no new string object is created.",
            ),
            _entry(
                17,
                "Check if a string is a palindrome using Java Streams.",
                "Generate the left-half indexes with a stream and verify that every position matches its mirrored partner on the right.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeStream("level");""",
                "Time O(n), Space O(1) extra.",
                "The stream solution is concise, but the optimized interview version is still the standard loop-based two-pointer solution.",
            ),
            _entry(
                18,
                "Check if a string is a palindrome using `StringBuilder`, then discuss why it is less optimal.",
                "Reverse the string with `StringBuilder` and compare it with the original. This is readable but costs extra memory because it builds another string representation.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions.isPalindromeWithStringBuilder("level");""",
                "Time O(n), Space O(n).",
                "The optimized approach is the two-pointer method, which keeps the same time complexity but reduces space to O(1).",
            ),
            _entry(
                19,
                "Check if only a substring from index `l` to `r` is a palindrome.",
                "Restrict the comparison to the requested range and compare characters symmetrically inside that window only.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions.isSubstringPalindrome(
    "abacaba", 1, 5
);""",
                "Time O(r - l + 1), Space O(1).",
                "For many repeated queries, an optimized approach is preprocessing with rolling hash or DP instead of checking every range from scratch.",
            ),
            _entry(
                20,
                "Check if a string can become a palindrome after removing at most one character.",
                "Scan from both ends. At the first mismatch, try skipping the left character once or the right character once; if either remaining range is palindromic, the answer is true.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions
    .canBecomePalindromeAfterRemovingAtMostOne("abca");""",
                "Time O(n), Space O(1).",
                "This is already the optimized linear solution for the one-removal variant.",
            ),
            _entry(
                21,
                "Check if a string can become a palindrome after removing exactly one character.",
                "Try removing each index and test whether the remaining characters form a palindrome. Return true as soon as one removal works.",
                """boolean result = PalindromeSolutions.ConstraintStringSolutions
    .canBecomePalindromeAfterRemovingExactlyOne("abca");""",
                "Time O(n^2), Space O(1).",
                "An optimized approach can be derived from the at-most-one-removal two-pointer idea by handling whether the original string is already a palindrome and then checking mismatch positions directly instead of trying every index.",
            ),
            _entry(
                22,
                "Find the first index whose removal makes the string a palindrome, if possible.",
                "Check each possible removed position from left to right and return the first one that makes the remaining characters palindromic.",
                """int index = PalindromeSolutions.ConstraintStringSolutions
    .firstRemovalIndexForPalindrome("cabba");""",
                "Time O(n^2), Space O(1).",
                "A more optimized approach can focus only on mismatch positions found by a two-pointer scan instead of testing every index.",
            ),
        ],
    ),
    Section(
        "4) Number Palindrome Questions",
        [
            _entry(
                23,
                "Write a Java program to check whether an integer is a palindrome.",
                "Convert the integer to a string and apply the basic string palindrome check. This is easy to explain and suitable for simple interviews.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeInt(12321);""",
                "Time O(d), Space O(d), where d is the number of digits.",
                "The optimized approach is question 24: compare the numeric halves without converting to a string.",
            ),
            _entry(
                24,
                "Check if a number is a palindrome without converting it to a string.",
                "Reverse only the last half of the number and compare it with the first half. This prevents full reversal overflow and keeps memory usage constant.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithoutString(12321);""",
                "Time O(d), Space O(1).",
                "This is the optimized approach over string conversion.",
            ),
            _entry(
                25,
                "Check if a long integer is a palindrome.",
                "Apply the same half-reversal idea as with `int`, but on `long` values.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeLong(123454321L);""",
                "Time O(d), Space O(1).",
                "Half reversal remains the optimized method here too.",
            ),
            _entry(
                26,
                "Reverse an integer safely and use it to test whether the original number is a palindrome.",
                "Reverse digit by digit using a wider numeric type to detect overflow. If reversing succeeds, compare the result with the original integer.",
                """OptionalInt reversed = PalindromeSolutions.NumberPalindromeSolutions.reverseIntSafely(12321);
boolean result = reversed.isPresent() && reversed.getAsInt() == 12321;""",
                "Time O(d), Space O(1).",
                "The optimized palindrome-only version is half reversal from question 24 because it avoids reversing the entire number at all.",
            ),
            _entry(
                27,
                "Check whether a negative number should be treated as a palindrome and justify the rule.",
                "Under the usual numeric interpretation, negative numbers are not palindromes because the minus sign appears only on the left side and cannot be mirrored on the right.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithNegativeRule(-121);""",
                "Time O(d), Space O(1).",
                "The optimized behavior is simply to reject negatives early before doing any other work.",
            ),
            _entry(
                28,
                "Check whether a number is a palindrome in binary representation.",
                "Identify the highest set bit and compare it with the lowest bit, moving inward until all mirrored binary positions are checked.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isBinaryPalindrome(9);""",
                "Time O(log n), Space O(1).",
                "Bit comparison is more optimized than constructing a binary string and reversing it.",
            ),
            _entry(
                29,
                "Check whether a number is a palindrome in any given base `b`.",
                "Extract the digits in base `b`, store them, and compare the digit sequence from both ends.",
                """boolean result = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeInBase(585, 2);""",
                "Time O(log_b n), Space O(log_b n).",
                "For very strict space constraints, an optimized solution can compare leading and trailing digits mathematically without storing the whole representation, though that is more complex to implement.",
            ),
            _entry(
                30,
                "Count all palindrome numbers in a range `[L, R]`.",
                "Iterate from `L` to `R` and test each value with the numeric palindrome method. This is straightforward and correct for moderate ranges.",
                """long count = PalindromeSolutions.NumberPalindromeSolutions
    .countPalindromeNumbersInRange(1, 200);""",
                "Time O((R - L + 1) * log R), Space O(1).",
                "For large ranges, the optimized strategy is to generate palindromes directly instead of testing every number.",
            ),
            _entry(
                31,
                "Generate all palindrome numbers with `n` digits.",
                "Generate only the first half of each palindrome and mirror it to form the full number. This avoids scanning all n-digit numbers.",
                """List<Long> values = PalindromeSolutions.NumberPalindromeSolutions.generateNDigitPalindromes(3);""",
                "Time proportional to the number of generated palindromes, O(10^(ceil(n / 2))). Space is the same including output.",
                "Half-generation plus mirroring is the optimized approach.",
            ),
            _entry(
                32,
                "Find the next palindrome number greater than a given integer.",
                "The current implementation increments the number until a palindrome is found. It is simple but may be slow if the gap is large.",
                """long next = PalindromeSolutions.NumberPalindromeSolutions.nextPalindromeNumber(123);""",
                "Current implementation: Time O(gap * log n), Space O(1).",
                "An optimized approach mirrors the left half of the number and, if needed, increments the middle before mirroring again.",
            ),
            _entry(
                33,
                "Find the nearest palindrome number to a given integer.",
                "Search outward on both sides until a palindrome is discovered. The current implementation returns the lower palindrome first if both sides are equally close.",
                """long nearest = PalindromeSolutions.NumberPalindromeSolutions.nearestPalindromeNumber(123);""",
                "Current implementation: Time O(gap * log n), Space O(1).",
                "An optimized approach generates a small candidate set by mirroring the number and nearby prefixes, then picks the closest candidate.",
            ),
        ],
    ),
    Section(
        "5) Array and Collection Palindrome Questions",
        [
            _entry(
                34,
                "Check whether an integer array is a palindrome.",
                "Compare the first and last elements, then move inward. If every mirrored pair matches, the array is a palindrome.",
                """boolean result = PalindromeSolutions.ArrayCollectionSolutions
    .isArrayPalindrome(new int[]{1, 2, 3, 2, 1});""",
                "Time O(n), Space O(1).",
                "This two-pointer array scan is already optimal.",
            ),
            _entry(
                35,
                "Check whether a generic `List<T>` is a palindrome.",
                "Compare elements at symmetric positions using `Objects.equals`, which handles nulls safely.",
                """boolean result = PalindromeSolutions.ArrayCollectionSolutions
    .isListPalindrome(List.of("a", "b", "a"));""",
                "Time O(n), Space O(1) for random-access lists.",
                "For linked lists, the optimized technique differs and usually involves a stack or list reversal.",
            ),
            _entry(
                36,
                "Check whether an array is a palindrome in-place using two pointers.",
                "Use the same array directly and do not create any copy. Just compare mirrored positions in the original array.",
                """boolean result = PalindromeSolutions.ArrayCollectionSolutions
    .isArrayPalindrome(new int[]{4, 5, 5, 4});""",
                "Time O(n), Space O(1).",
                "This is the optimized in-place approach.",
            ),
            _entry(
                37,
                "Determine whether a deque of characters forms a palindrome.",
                "Remove one character from the front and one from the back and compare them. Continue until the deque size is zero or one.",
                """boolean result = PalindromeSolutions.ArrayCollectionSolutions
    .isDequePalindrome(new ArrayDeque<>(List.of('n', 'o', 'o', 'n')));""",
                "Time O(n), Space O(n) in the current implementation because it copies the deque.",
                "An optimized variant can mutate the original deque directly and reduce extra space to O(1) if preserving the input is not required.",
            ),
            _entry(
                38,
                "Check whether a list of strings is a palindrome by value comparison.",
                "This is a specialization of the generic list palindrome problem: compare the first string with the last, second with second-last, and so on.",
                """boolean result = PalindromeSolutions.ArrayCollectionSolutions
    .isListPalindrome(List.of("red", "blue", "red"));""",
                "Time O(n), Space O(1) for random-access lists.",
                "The same optimized two-index logic applies.",
            ),
            _entry(
                39,
                "Count how many subarrays of length `k` are palindromic.",
                "Slide a window of length `k` across the array and test each window with a two-pointer check.",
                """long count = PalindromeSolutions.ArrayCollectionSolutions
    .countPalindromicSubarrays(new int[]{1, 2, 1, 2, 1}, 3);""",
                "Time O((n - k + 1) * k), Space O(1).",
                "For many queries or very large arrays, an optimized approach could use rolling hash or Manacher-style ideas adapted to arrays.",
            ),
            _entry(
                40,
                "Find the longest palindromic subarray in an integer array.",
                "Expand around every possible single center and every gap center exactly like longest palindromic substring, but on integers instead of characters.",
                """int[] best = PalindromeSolutions.ArrayCollectionSolutions
    .longestPalindromicSubarray(new int[]{1, 2, 3, 2, 1, 9});""",
                "Time O(n^2), Space O(1) extra.",
                "The center-expansion technique is a strong optimized interview answer compared with brute-force checking of all subarrays.",
            ),
        ],
    ),
    Section(
        "6) Linked List Palindrome Questions",
        [
            _entry(
                41,
                "Check whether a singly linked list is a palindrome.",
                "Find the midpoint, reverse the second half, compare both halves, and then optionally restore the original list.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(
    PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 3, 2, 1)
);""",
                "Time O(n), Space O(1).",
                "This reverse-second-half technique is the optimized linked-list approach.",
            ),
            _entry(
                42,
                "Check whether a singly linked list is a palindrome using a stack.",
                "Traverse the list once to push node values, then compare them during a second traversal.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeWithStack(
    PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 1)
);""",
                "Time O(n), Space O(n).",
                "The optimized alternative is reversing the second half to reduce extra space to O(1).",
            ),
            _entry(
                43,
                "Check whether a singly linked list is a palindrome by reversing the second half.",
                "Use slow and fast pointers to reach the middle, reverse the tail portion, and compare it with the first half.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeByReversingSecondHalf(
    PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 2, 1)
);""",
                "Time O(n), Space O(1).",
                "This is the optimized solution compared with stack-based checking.",
            ),
            _entry(
                44,
                "Restore the original linked list after palindrome checking.",
                "After the comparison, reverse the second half again and reconnect it so the input list keeps its initial shape.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(
    PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 3, 2, 1)
);""",
                "Time O(n), Space O(1).",
                "Restoring the list is the polished optimized interview answer when mutation of input is a concern.",
            ),
            _entry(
                45,
                "Check whether a doubly linked list is a palindrome.",
                "Start one pointer at the head and one at the tail, then compare values while moving both toward the center.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isDoublyListPalindrome(
    PalindromeSolutions.LinkedListSolutions.DoublyNode.of(1, 2, 3, 2, 1)
);""",
                "Time O(n), Space O(1).",
                "Because a doubly linked list gives backward access, this direct two-ended scan is already optimal.",
            ),
            _entry(
                46,
                "Check whether a circular linked list is a palindrome under one full traversal.",
                "Read exactly one cycle into a linear sequence of known length, then apply the usual palindrome check to that collected data.",
                """boolean result = PalindromeSolutions.LinkedListSolutions.isCircularListPalindrome(
    PalindromeSolutions.LinkedListSolutions.CircularNode.of(1, 2, 1), 3
);""",
                "Time O(n), Space O(n).",
                "A more optimized approach may use specialized pointer logic, but collecting one full traversal is a clean and reliable answer.",
            ),
        ],
    ),
    Section(
        "7) Substring-Based Palindrome Questions",
        [
            _entry(
                47,
                "Find the longest palindromic substring in a string.",
                "Expand around every possible center and record the best range. Each palindrome is centered either at a character or between two characters.",
                """String best = PalindromeSolutions.SubstringSolutions
    .longestPalindromicSubstring("forgeeksskeegfor");""",
                "Time O(n^2), Space O(1).",
                "Center expansion is the optimized general-purpose interview solution. Manacher's algorithm can improve time to O(n) but is harder to explain.",
            ),
            _entry(
                48,
                "Count all palindromic substrings in a string.",
                "Expand around every center and count each successful expansion as one palindrome.",
                """long count = PalindromeSolutions.SubstringSolutions.countPalindromicSubstrings("aaa");""",
                "Time O(n^2), Space O(1).",
                "Center expansion is a strong optimized answer compared with brute-force checking of every substring.",
            ),
            _entry(
                49,
                "Print all distinct palindromic substrings of a string.",
                "Expand around centers and store each found substring in a set so duplicate palindromes appear only once.",
                """Set<String> values = PalindromeSolutions.SubstringSolutions
    .distinctPalindromicSubstrings("ababa");""",
                "Worst-case time O(n^3) with substring materialization, Space O(n^2) worst case.",
                "If only counting is needed, avoid materializing substrings. If distinct reporting is required, using a set is a practical approach.",
            ),
            _entry(
                50,
                "Find the length of the longest palindromic substring.",
                "Run the longest-palindromic-substring algorithm and return the length instead of the actual substring.",
                """int length = PalindromeSolutions.SubstringSolutions
    .lengthOfLongestPalindromicSubstring("babad");""",
                "Time O(n^2), Space O(1).",
                "The optimized approach is still center expansion, unless the interview specifically expects Manacher's algorithm.",
            ),
            _entry(
                51,
                "Return the starting index of the longest palindromic substring.",
                "Track the best palindrome range while expanding around centers and return the left boundary of that best range.",
                """int index = PalindromeSolutions.SubstringSolutions
    .startIndexOfLongestPalindromicSubstring("forgeeksskeegfor");""",
                "Time O(n^2), Space O(1).",
                "Center expansion remains the optimized answer for readability and simplicity.",
            ),
            _entry(
                52,
                "Find the longest even-length palindromic substring.",
                "Only expand around gaps between adjacent characters, because even-length palindromes have no single central character.",
                """String best = PalindromeSolutions.SubstringSolutions
    .longestEvenPalindromicSubstring("abccba");""",
                "Time O(n^2), Space O(1).",
                "Restricting to gap centers is the optimized specialization of the center-expansion method.",
            ),
            _entry(
                53,
                "Find the longest odd-length palindromic substring.",
                "Only expand around actual characters because odd-length palindromes have a single center element.",
                """String best = PalindromeSolutions.SubstringSolutions
    .longestOddPalindromicSubstring("bananas");""",
                "Time O(n^2), Space O(1).",
                "Restricting to character centers is the optimized specialized version of center expansion.",
            ),
            _entry(
                54,
                "Find all palindromic substrings longer than length `k`.",
                "Expand around all centers and keep only the palindromes whose length exceeds `k`.",
                """List<String> values = PalindromeSolutions.SubstringSolutions
    .palindromicSubstringsLongerThan("abacdcaba", 2);""",
                "Worst-case time O(n^3) with substring construction, Space O(output).",
                "If only counts are required, a more optimized approach avoids building the substring objects themselves.",
            ),
            _entry(
                55,
                "Count palindromic substrings for multiple test cases efficiently.",
                "Apply the same center-expansion logic independently to each test case. This is practical for moderate input sizes and easy to implement correctly.",
                """List<Long> counts = testCases.stream()
    .map(PalindromeSolutions.SubstringSolutions::countPalindromicSubstrings)
    .toList();""",
                "Time is the sum of O(length^2) for each test case, Space O(1) extra per case.",
                "For very large numbers of repeated queries on the same string, preprocessing approaches such as Manacher's algorithm or query-specific data structures become the optimized option.",
            ),
        ],
    ),
    Section(
        "8) Subsequence and DP-Based Questions",
        [
            _entry(
                56,
                "Find the length of the longest palindromic subsequence.",
                "Define `dp[i][j]` as the longest palindromic subsequence length in the substring from `i` to `j`. If both ends match, include them; otherwise drop one end and take the better answer.",
                """int length = PalindromeSolutions.DynamicProgrammingSolutions
    .longestPalindromicSubsequenceLength("bbbab");""",
                "Time O(n^2), Space O(n^2).",
                "Dynamic programming is the optimized standard approach over brute-force subsequence enumeration.",
            ),
            _entry(
                57,
                "Print one longest palindromic subsequence.",
                "First fill the DP table for LPS length, then walk the table from both ends to reconstruct one valid subsequence.",
                """String lps = PalindromeSolutions.DynamicProgrammingSolutions
    .oneLongestPalindromicSubsequence("bbbab");""",
                "Time O(n^2), Space O(n^2).",
                "The optimized strategy is to reconstruct from the DP table rather than enumerate all subsequences.",
            ),
            _entry(
                58,
                "Count the number of palindromic subsequences in a string.",
                "Use DP to count answers for smaller ranges and combine them carefully. When the boundary characters differ, subtract overlap to avoid double-counting.",
                """long count = PalindromeSolutions.DynamicProgrammingSolutions
    .countPalindromicSubsequences("aaa");""",
                "Time O(n^2), Space O(n^2).",
                "DP is the optimized approach; brute force over all subsequences is exponential.",
            ),
            _entry(
                59,
                "Find the minimum number of insertions needed to make a string a palindrome.",
                "The answer equals `n - LPS`, because every character not belonging to an optimal palindromic subsequence must be inserted somewhere to mirror another character.",
                """int answer = PalindromeSolutions.DynamicProgrammingSolutions
    .minInsertionsToPalindrome("abcda");""",
                "Time O(n^2), Space O(n^2).",
                "Using the longest palindromic subsequence relation is the optimized dynamic-programming insight.",
            ),
            _entry(
                60,
                "Find the minimum number of deletions needed to make a string a palindrome.",
                "This is symmetric to minimum insertions: remove every character that is not part of a longest palindromic subsequence.",
                """int answer = PalindromeSolutions.DynamicProgrammingSolutions
    .minDeletionsToPalindrome("abcda");""",
                "Time O(n^2), Space O(n^2).",
                "The optimized insight is again `n - LPS`.",
            ),
            _entry(
                61,
                "Find the minimum number of replacements needed to make a string a palindrome.",
                "Walk inward from both ends. Every mismatched mirrored pair can be fixed with exactly one replacement.",
                """int answer = PalindromeSolutions.DynamicProgrammingSolutions
    .minReplacementsToPalindrome("abcdef");""",
                "Time O(n), Space O(1).",
                "Counting mismatched pairs directly is already optimal.",
            ),
            _entry(
                62,
                "Determine whether a string is a `k`-palindrome.",
                "A string is a `k`-palindrome if it can be made palindromic after deleting at most `k` characters. Compute minimum deletions or equivalently use the LPS relation.",
                """boolean result = PalindromeSolutions.DynamicProgrammingSolutions
    .isKPalindrome("abcdecba", 1);""",
                "Time O(n^2), Space O(n^2).",
                "The optimized approach is dynamic programming instead of trying all deletion combinations.",
            ),
            _entry(
                63,
                "Partition a string into palindromic substrings using dynamic programming.",
                "Precompute which ranges are palindromes, then backtrack using only valid palindromic pieces to build all partitions.",
                """List<List<String>> parts = PalindromeSolutions.DynamicProgrammingSolutions
    .palindromePartitions("aab");""",
                "Time O(n^2 + output_size), Space O(n^2 + output_size).",
                "The optimized idea is to separate palindrome preprocessing from partition generation.",
            ),
            _entry(
                64,
                "Find the minimum cuts needed for palindrome partitioning.",
                "Use a palindrome table and a `cuts[i]` array that stores the minimum cuts needed for the prefix ending at `i`. If a suffix is palindromic, it can serve as the final partition segment.",
                """int cuts = PalindromeSolutions.DynamicProgrammingSolutions
    .minCutPalindromePartition("aab");""",
                "Time O(n^2), Space O(n^2).",
                "This DP is the optimized answer over brute-force partitioning.",
            ),
            _entry(
                65,
                "Count the number of ways to partition a string so every part is a palindrome.",
                "After precomputing palindrome ranges, count how many valid partitions start at each index using dynamic programming from right to left.",
                """long ways = PalindromeSolutions.DynamicProgrammingSolutions
    .countPalindromePartitions("aab");""",
                "Time O(n^2), Space O(n^2).",
                "Dynamic programming is the optimized solution; brute force quickly becomes exponential.",
            ),
        ],
    ),
    Section(
        "9) Rearrangement and Construction Questions",
        [
            _entry(
                66,
                "Check whether any permutation of a string can form a palindrome.",
                "Count character frequencies. A palindrome permutation is possible only if at most one character appears an odd number of times.",
                """boolean result = PalindromeSolutions.RearrangementConstructionSolutions
    .canPermutePalindrome("carrace");""",
                "Time O(n log sigma) in the current TreeMap implementation, Space O(sigma).",
                "The optimized logic is frequency parity checking; using a HashMap can reduce the map overhead to near O(n).",
            ),
            _entry(
                67,
                "Rearrange the characters of a string to form one palindrome, if possible.",
                "Build half of the palindrome from paired characters, keep one odd character for the center, and mirror the half to the other side.",
                """String value = PalindromeSolutions.RearrangementConstructionSolutions
    .buildOnePalindrome("aabbccd");""",
                "Time O(n log sigma), Space O(sigma).",
                "The optimized construction uses counts instead of trying permutations.",
            ),
            _entry(
                68,
                "Generate all palindromic permutations of a string.",
                "Generate unique permutations of only the half-string and mirror each result. This is much better than generating all permutations of the full string and filtering them.",
                """List<String> values = PalindromeSolutions.RearrangementConstructionSolutions
    .generatePalindromicPermutations("aabb");""",
                "Time O(p * n), Space O(p * n), where p is the number of generated palindromes.",
                "Generating permutations of the half-string is the optimized approach compared with full-permutation brute force.",
            ),
            _entry(
                69,
                "Build the longest possible palindrome using the characters of a string.",
                "Take all even counts and one odd center if available. Every other odd leftover contributes only its largest even part.",
                """int length = PalindromeSolutions.RearrangementConstructionSolutions
    .longestPossiblePalindromeLength("abccccdd");""",
                "Time O(n log sigma), Space O(sigma).",
                "The optimized insight is to use all possible pairs and only one odd center.",
            ),
            _entry(
                70,
                "Build the lexicographically smallest palindrome from the given characters.",
                "Sort or store characters in ascending order, build the left half from the smallest available pairs, place the middle if needed, then mirror it.",
                """String value = PalindromeSolutions.RearrangementConstructionSolutions
    .lexicographicallySmallestPalindrome("aabbccd");""",
                "Time O(n log sigma), Space O(sigma).",
                "Using ordered frequency storage is the optimized construction for lexicographic requirements.",
            ),
            _entry(
                71,
                "Determine the minimum swaps needed to rearrange a string into a palindrome.",
                "For arbitrary swaps, first choose a target palindrome arrangement, then compute the minimum swaps needed to transform the source arrangement into that target using index mapping and cycle decomposition.",
                """String target = buildTargetPalindrome(value);
int swaps = minArbitrarySwaps(source, target);""",
                "Usually O(n log n) to O(n^2) depending on duplicate handling, Space O(n).",
                "Compared with adjacent-swap simulation, arbitrary-swap counting can be more efficient when the interview allows swapping any two positions.",
            ),
            _entry(
                72,
                "Determine the minimum adjacent swaps needed to make a string a palindrome.",
                "Move matching characters toward the left and right ends by repeated adjacent swaps. When a character has no partner, it must be the middle character and is bubbled inward.",
                """int swaps = PalindromeSolutions.RearrangementConstructionSolutions
    .minAdjacentSwapsToMakePalindrome("mamad");""",
                "Time O(n^2), Space O(1).",
                "This greedy adjacent-swap strategy is the standard optimized answer for the adjacent-only version.",
            ),
            _entry(
                73,
                "Add the minimum number of characters to the end of a string to make it a palindrome.",
                "Find the earliest suffix that is already a palindrome. All preceding characters must be appended in reverse order to the end.",
                """int count = PalindromeSolutions.RearrangementConstructionSolutions
    .minCharsToAppendAtEnd("abcd");
String shortest = PalindromeSolutions.RearrangementConstructionSolutions
    .shortestPalindromeByAppendingEnd("abcd");""",
                "Current implementation: Time O(n^2), Space O(1) extra for the count.",
                "A more optimized version can use rolling hash or prefix-function style preprocessing to reduce repeated suffix checking.",
            ),
            _entry(
                74,
                "Add the minimum number of characters to the front of a string to make it a palindrome.",
                "Find the longest palindromic prefix. Everything after that prefix must be reversed and added in front.",
                """int count = PalindromeSolutions.RearrangementConstructionSolutions
    .minCharsToAddInFront("aacecaaa");""",
                "Time O(n), Space O(n).",
                "Using the longest-palindromic-prefix idea with KMP-style preprocessing is the optimized approach.",
            ),
            _entry(
                75,
                "Construct the shortest palindrome by adding characters in front of the string.",
                "This is the constructive form of question 74. Reverse the suffix that lies outside the longest palindromic prefix and prepend it.",
                """String value = PalindromeSolutions.RearrangementConstructionSolutions
    .shortestPalindromeByAddingFront("abcd");""",
                "Time O(n), Space O(n).",
                "The KMP/prefix-function-based prefix detection is the optimized approach here.",
            ),
        ],
    ),
    Section(
        "10) Pairing and Combination Questions",
        [
            _entry(
                76,
                "Given a list of words, find all pairs whose concatenation is a palindrome.",
                "For each word, split it into every possible prefix and suffix. If one side is a palindrome, the reversed other side may be the needed partner in a hash map.",
                """List<List<Integer>> pairs = PalindromeSolutions.PairingCombinationSolutions
    .palindromePairs(new String[]{"bat", "tab", "cat"});""",
                "Time O(n * k^2), Space O(n * k).",
                "Using a hash map for reverse lookups is the optimized approach compared with testing every pair directly in O(n^2 * k).",
            ),
            _entry(
                77,
                "Count the number of palindrome pairs in an array of strings.",
                "Generate all palindrome pairs using the same prefix-suffix split method and count them.",
                """int count = PalindromeSolutions.PairingCombinationSolutions
    .countPalindromePairs(new String[]{"bat", "tab", "cat"});""",
                "Time O(n * k^2), Space O(n * k).",
                "The optimized strategy is the same hash-map-based palindrome pair search.",
            ),
            _entry(
                78,
                "Check whether two given strings can be combined to form a palindrome.",
                "Try both concatenation orders, because `a + b` and `b + a` are different candidates.",
                """boolean result = PalindromeSolutions.PairingCombinationSolutions
    .canCombineToPalindrome("abc", "cba");""",
                "Time O(n + m), Space O(n + m) in the current implementation.",
                "A more optimized low-level implementation could compare characters without materializing the concatenated strings.",
            ),
            _entry(
                79,
                "Find the longest palindrome that can be formed by concatenating two strings.",
                "The repository implementation concatenates the strings in both orders and finds the longest palindromic substring within each concatenation, returning the better one.",
                """String best = PalindromeSolutions.PairingCombinationSolutions
    .longestPalindromeFromConcatenatingTwoStrings("abaxy", "zyxf");""",
                "Time O((n + m)^2), Space O(1) extra beyond produced substrings.",
                "An optimized interview solution depends on the exact problem interpretation. Some variants use DP or center expansion over constrained cross-boundary joins.",
            ),
            _entry(
                80,
                "Build the longest palindrome from a list of two-letter words.",
                "Pair each word with its reverse to contribute four characters. Symmetric words like `\"gg\"` can also place one leftover word in the center.",
                """int length = PalindromeSolutions.PairingCombinationSolutions
    .longestPalindromeFromTwoLetterWords(new String[]{"lc", "cl", "gg"});""",
                "Time O(w), Space O(w), where w is the number of words.",
                "Counting frequencies in a hash map is the optimized approach.",
            ),
        ],
    ),
    Section(
        "11) Matrix, Grid, and Pattern Variants",
        [
            _entry(
                81,
                "Check whether each row of a character matrix is a palindrome.",
                "Treat each row as a `char[]` palindrome check and count or report which rows succeed.",
                """long rows = PalindromeSolutions.MatrixGridPatternSolutions.countPalindromicRows(matrix);""",
                "Time O(r * c), Space O(1).",
                "This row-wise direct scan is already optimal.",
            ),
            _entry(
                82,
                "Check whether each column of a matrix is a palindrome.",
                "For each column, compare the top cell with the bottom cell, then move inward until the center is reached.",
                """long cols = PalindromeSolutions.MatrixGridPatternSolutions.countPalindromicColumns(matrix);""",
                "Time O(r * c), Space O(1).",
                "This vertical mirrored scan is already optimal.",
            ),
            _entry(
                83,
                "Count palindromic rows and palindromic columns in a matrix.",
                "Count row palindromes and column palindromes independently, then add the results.",
                """long total = PalindromeSolutions.MatrixGridPatternSolutions
    .countPalindromicRowsAndColumns(matrix);""",
                "Time O(r * c), Space O(1).",
                "No better asymptotic approach is needed because every cell must be part of some row or column check.",
            ),
            _entry(
                84,
                "Determine whether a path string formed in a grid is a palindrome.",
                "Once the path labels are collected into a string, the problem reduces to the basic string palindrome check.",
                """boolean result = PalindromeSolutions.MatrixGridPatternSolutions
    .isGridPathPalindrome("abccba");""",
                "Time O(path length), Space O(1) extra after the path string is built.",
                "If path enumeration itself is part of the task, optimized graph traversal becomes the real challenge rather than the palindrome check.",
            ),
            _entry(
                85,
                "Find all palindromic diagonals in a square matrix.",
                "Collect diagonal strings in both major directions and keep only those that read the same forward and backward.",
                """List<String> values = PalindromeSolutions.MatrixGridPatternSolutions
    .palindromicDiagonals(matrix);""",
                "Current implementation: Time O(r * c * min(r, c)), Space O(output).",
                "An optimized approach could avoid rebuilding diagonal strings repeatedly by streaming comparisons directly from both ends of each diagonal.",
            ),
        ],
    ),
    Section(
        "12) Hashing, Queries, and Large Input Questions",
        [
            _entry(
                86,
                "Answer multiple palindrome substring queries efficiently.",
                "Preprocess the string once so each query can be answered quickly. The repository uses a rolling-hash palindrome checker for constant-time queries after linear preprocessing.",
                """var checker = new PalindromeSolutions.HashingQuerySolutions
    .RollingHashPalindromeChecker("racecar");
boolean result = checker.isPalindrome(1, 5);""",
                "Preprocessing O(n), Query O(1), Space O(n).",
                "Preprocessing plus O(1) queries is the optimized approach over checking each query range from scratch.",
            ),
            _entry(
                87,
                "Preprocess a string so each query `[l, r]` can be checked for palindrome status quickly.",
                "Build prefix hashes for the original string and its reverse, together with the powers of the hash base. This preprocessing is what enables constant-time queries later.",
                """var checker = new PalindromeSolutions.HashingQuerySolutions
    .RollingHashPalindromeChecker("abacaba");""",
                "Preprocessing O(n), Space O(n).",
                "This is itself the optimized approach for repeated queries.",
            ),
            _entry(
                88,
                "Use rolling hash to check whether substrings are palindromes.",
                "Compute the forward hash of the substring and compare it with the corresponding backward hash from the reversed string.",
                """boolean result = new PalindromeSolutions.HashingQuerySolutions
    .RollingHashPalindromeChecker("abacaba")
    .isPalindrome(2, 4);""",
                "Preprocessing O(n), Query O(1), Space O(n).",
                "In production, double hashing is often the optimized safer variant because it reduces collision risk.",
            ),
            _entry(
                89,
                "Support updates to characters and answer palindrome range queries.",
                "The current mutable engine rebuilds the rolling-hash helper after each update, then answers queries in O(1).",
                """var engine = new PalindromeSolutions.HashingQuerySolutions
    .MutablePalindromeQueryEngine("racecar");
engine.update(3, 'e');
boolean result = engine.isPalindrome(0, 6);""",
                "Current implementation: Update O(n), Query O(1), Space O(n).",
                "A more optimized approach uses Fenwick trees or segment trees with forward and reverse hashes so updates can be reduced to O(log n).",
            ),
            _entry(
                90,
                "Check whether a very large string is a palindrome when it cannot fit fully in memory.",
                "Open the file with random access and compare one byte from the beginning with one byte from the end, moving inward without loading the full contents.",
                """boolean result = PalindromeSolutions.HashingQuerySolutions
    .isLargeAsciiFilePalindrome(Path.of("huge.txt"));""",
                "Time O(n), Space O(1).",
                "Two-ended random access is the optimized strategy for large external data.",
            ),
            _entry(
                91,
                "Check whether a stream of incoming characters currently forms a palindrome.",
                "Append the incoming characters to a growing buffer and test the current content whenever needed.",
                """var stream = new PalindromeSolutions.HashingQuerySolutions.StreamPalindromeChecker();
stream.append('r');
stream.append('a');
stream.append('d');
stream.append('a');
stream.append('r');
boolean result = stream.isCurrentPalindrome();""",
                "Append O(1) amortized, current palindrome check O(n), Space O(n).",
                "An optimized approach for many queries would maintain rolling hashes incrementally rather than rescanning the whole current string each time.",
            ),
            _entry(
                92,
                "Design a data structure that supports append and palindrome-check operations.",
                "Maintain the evolving string and a helper structure for palindrome queries. The current implementation stores the current characters and rebuilds the rolling hash helper on updates or appends.",
                """var engine = new PalindromeSolutions.HashingQuerySolutions
    .MutablePalindromeQueryEngine("ab");
engine.append('a');
boolean result = engine.isPalindrome(0, engine.currentValue().length() - 1);""",
                "Current implementation: Append O(n), Query O(1), Space O(n).",
                "The optimized version is an online hash structure where append updates hashes incrementally in O(1) or O(log n).",
            ),
        ],
    ),
    Section(
        "13) Advanced Interview and Competitive Coding Questions",
        [
            _entry(
                93,
                "Find the shortest palindrome by adding characters only at the front.",
                "Find the longest palindromic prefix, then prepend the reverse of the leftover suffix.",
                """String value = PalindromeSolutions.RearrangementConstructionSolutions
    .shortestPalindromeByAddingFront("abcd");""",
                "Time O(n), Space O(n).",
                "Using prefix-function/KMP logic to find the longest palindromic prefix is the optimized approach.",
            ),
            _entry(
                94,
                "Find the longest palindrome that can be formed from a multiset of characters.",
                "A multiset view means only character counts matter. Use all even counts and place at most one odd-count character in the center.",
                """int length = PalindromeSolutions.RearrangementConstructionSolutions
    .longestPossiblePalindromeLength("abccccdd");""",
                "Time O(n log sigma), Space O(sigma).",
                "Frequency counting is the optimized approach; there is no need to generate permutations.",
            ),
            _entry(
                95,
                "Find the maximum product of lengths of two disjoint palindromic subsequences.",
                "Enumerate subsequences with bitmasks, keep the length of the masks that form palindromes, and combine disjoint masks for the best product.",
                """int answer = PalindromeSolutions.AdvancedSolutions
    .maxProductOfTwoDisjointPalindromicSubsequences("leetcodecom");""",
                "Time O(n * 2^n), Space O(2^n).",
                "The implemented bitmask DP is already the optimized competitive-programming style solution for small n. The key optimization is pruning through subset DP instead of comparing every pair of subsequences naively.",
            ),
            _entry(
                96,
                'Count "super palindromes" where both the number and its square are palindromes.',
                "Instead of testing every number, generate palindromic roots directly, square them, and check whether the square is also palindromic and falls in the requested range.",
                """int count = PalindromeSolutions.AdvancedSolutions
    .countSuperPalindromes(1L, 100000L);""",
                "Time depends on the number of palindromic roots up to sqrt(R); extra space O(1).",
                "Generating palindromic roots directly is the optimized approach compared with scanning every integer in the interval.",
            ),
            _entry(
                97,
                "Find the largest palindromic number that can be formed from the digits of a string.",
                "Count digit frequencies, build the left half from the largest digits first, reserve the largest leftover digit for the center, and mirror the left half.",
                """String value = PalindromeSolutions.AdvancedSolutions
    .largestPalindromicNumber("444947137");""",
                "Time O(n), Space O(1) extra beyond output.",
                "This greedy counting approach is the optimized solution.",
            ),
            _entry(
                98,
                "Find the smallest palindromic number larger than a given numeric string.",
                "Mirror the left half onto the right. If the result is not strictly larger than the input, increment the middle and propagate carry, then mirror again.",
                """String value = PalindromeSolutions.AdvancedSolutions
    .smallestPalindromicNumberLargerThan("23545");""",
                "Time O(n), Space O(n).",
                "Mirroring plus middle carry propagation is the optimized classic approach.",
            ),
            _entry(
                99,
                "Determine whether a string can be split into exactly three palindromic substrings.",
                "Precompute which substrings are palindromes, then try every possible first cut and second cut. If all three resulting pieces are palindromes, return true.",
                """boolean result = PalindromeSolutions.AdvancedSolutions
    .canSplitIntoThreePalindromes("abcbdd");""",
                "Time O(n^2), Space O(n^2).",
                "The optimized approach is DP-based preprocessing rather than testing every partition with fresh palindrome scans.",
            ),
            _entry(
                100,
                "Find all ways to partition a string into exactly `k` palindromic parts.",
                "Use the palindrome table for valid ranges, then backtrack while also tracking how many parts remain to be chosen.",
                """List<List<String>> parts = PalindromeSolutions.AdvancedSolutions
    .partitionsIntoKPalindromes("aab", 2);""",
                "Time O(n^2 + output_size), Space O(n^2 + output_size).",
                "Precomputing palindrome ranges is the key optimization.",
            ),
            _entry(
                101,
                "Given a string, maximize palindrome length after at most `k` character changes.",
                "Count how many mirrored pairs mismatch. Each allowed change can fix one mismatched pair, so the current implementation estimates how much of the string can be made palindromic.",
                """int length = PalindromeSolutions.AdvancedSolutions
    .maxPalindromeLengthAfterAtMostKChanges("abcdef", 2);""",
                "Time O(n), Space O(1).",
                "For the specific goal of maximizing achievable palindrome length under this model, counting mismatches is the optimized direct approach.",
            ),
            _entry(
                102,
                "Given two strings, find the longest palindromic subsequence using characters from both.",
                "Concatenate the strings and compute the LPS DP table, but only accept solutions whose left boundary comes from the first string and whose right boundary comes from the second.",
                """int length = PalindromeSolutions.AdvancedSolutions
    .longestPalindromicSubsequenceUsingBothStrings("cacb", "cbba");""",
                "Time O((n + m)^2), Space O((n + m)^2).",
                "Using a combined DP table with cross-boundary validation is the optimized dynamic-programming strategy.",
            ),
            _entry(
                103,
                "Count palindromic paths in a tree or graph where labels are characters.",
                "A common tree solution tracks a parity bitmask of character counts along the current path. A path can form a palindrome if at most one character has odd frequency, which means the final mask has at most one set bit.",
                """int count = countPseudoPalindromicPaths(root, 0);""",
                "Tree version typically runs in O(V + E) time with O(H) recursion stack. General graphs depend on traversal constraints and visited-state design.",
                "The optimized approach is parity-bitmask tracking rather than storing the full multiset of path characters.",
            ),
            _entry(
                104,
                "Check whether a sentence remains a palindrome after applying a series of character updates.",
                "Maintain the mutable sentence and answer full-range palindrome checks after each update. If the problem ignores punctuation or case, normalize the text before storing it.",
                """var engine = new PalindromeSolutions.HashingQuerySolutions
    .MutablePalindromeQueryEngine("neveroddoreven");
engine.update(5, 'x');
boolean result = engine.isPalindrome(0, engine.currentValue().length() - 1);""",
                "Current implementation: Update O(n), Query O(1), Space O(n).",
                "An optimized version would use dynamic rolling hashes or segment trees to reduce update cost.",
            ),
            _entry(
                105,
                "Find the minimum operations needed to transform one string into a palindrome.",
                "In this repository, operations are modeled as insertions, so the answer is computed through the minimum-insertions DP relation based on longest palindromic subsequence.",
                """int ops = PalindromeSolutions.AdvancedSolutions
    .minOperationsToTransformToPalindrome("abcda");""",
                "Time O(n^2), Space O(n^2).",
                "The optimized answer depends on the exact operation set allowed. For insertions/deletions, the LPS-based DP is the standard optimization.",
            ),
        ],
    ),
    Section(
        "14) Popular Follow-Up Variations for Interviews",
        [
            _entry(
                106,
                "Solve the basic palindrome problem first, then optimize for `O(1)` extra space.",
                "Start from a straightforward solution, then refine it into the two-pointer method that compares the original sequence directly without auxiliary storage.",
                """boolean result = PalindromeSolutions.InterviewFollowUps.isPalindromeO1Space("level");""",
                "Time O(n), Space O(1).",
                "The O(1)-space two-pointer approach is the optimized answer.",
            ),
            _entry(
                107,
                "Solve palindrome checking without using library helpers such as `reverse()`.",
                "Do not depend on `reverse()` or `StringBuilder`; compare the input directly from both ends with indexes.",
                """boolean result = PalindromeSolutions.InterviewFollowUps
    .isPalindromeNoLibraryHelpers("radar");""",
                "Time O(n), Space O(1).",
                "Direct index comparison is the optimized and most interview-friendly approach.",
            ),
            _entry(
                108,
                "Solve the same problem for mutable input such as `char[]`.",
                "The logic is unchanged: compare the left and right ends and move inward until the center is reached.",
                """boolean result = PalindromeSolutions.InterviewFollowUps
    .isPalindromeMutable(new char[]{'n', 'o', 'o', 'n'});""",
                "Time O(n), Space O(1).",
                "The optimized answer is still the in-place two-pointer scan.",
            ),
            _entry(
                109,
                "Explain the trade-offs between iterative, recursive, stack-based, and stream-based solutions.",
                "Iterative two pointers are usually best because they are simple and O(1) space. Recursive solutions are elegant but consume call-stack memory. Stack-based solutions are intuitive but use extra space. Stream-based versions are expressive but often less direct and not usually the fastest.",
                """boolean iterative = PalindromeSolutions.BasicStringSolutions.isPalindrome("level");
boolean recursive = PalindromeSolutions.BasicStringSolutions.isPalindromeRecursive("level");
boolean stack = PalindromeSolutions.BasicStringSolutions.isPalindromeWithStack("level");
boolean stream = PalindromeSolutions.ConstraintStringSolutions.isPalindromeStream("level");""",
                "Iterative O(n)/O(1), Recursive O(n)/O(n), Stack O(n)/O(n), Stream O(n)/O(1) extra.",
                "The optimized practical answer for most interviews is the iterative two-pointer solution.",
            ),
            _entry(
                110,
                "Modify the solution to ignore case, spaces, punctuation, or all non-alphanumeric characters.",
                "Normalize the comparison rules while scanning instead of changing the core palindrome idea. Skip irrelevant characters and lowercase letters before comparing them.",
                """boolean result = PalindromeSolutions.InterviewFollowUps
    .isPalindromeIgnoringNoise("A man, a plan, a canal: Panama");""",
                "Time O(n), Space O(1).",
                "The optimized version ignores noise during the scan instead of allocating a cleaned copy first.",
            ),
            _entry(
                111,
                "Extend the solution from strings to arrays, lists, and linked lists.",
                "The palindrome concept never changes: compare mirrored positions. What changes is how those positions are accessed in each data structure.",
                """boolean arrayOk = PalindromeSolutions.ArrayCollectionSolutions
    .isArrayPalindrome(new int[]{1, 2, 1});
boolean listOk = PalindromeSolutions.ArrayCollectionSolutions
    .isListPalindrome(List.of("x", "y", "x"));
boolean linkedOk = PalindromeSolutions.LinkedListSolutions.isPalindromeAndRestore(
    PalindromeSolutions.LinkedListSolutions.SinglyNode.of(1, 2, 1)
);""",
                "Arrays/lists O(n), linked lists O(n); extra space depends on the linked-list technique used.",
                "Optimized array/list solutions use two pointers, while optimized linked-list solutions reverse the second half instead of using a stack.",
            ),
            _entry(
                112,
                "Optimize from brute force to dynamic programming for substring and subsequence problems.",
                "Brute force often checks every possible substring, partition, or subsequence and becomes too slow. For substrings, center expansion avoids redundant work. For subsequences and partitioning, dynamic programming stores results for overlapping subproblems and reuses them.",
                """String bestSubstring = PalindromeSolutions.SubstringSolutions
    .longestPalindromicSubstring("babad");
int bestSubsequence = PalindromeSolutions.DynamicProgrammingSolutions
    .longestPalindromicSubsequenceLength("bbbab");""",
                "Brute-force substring methods are often O(n^3) or worse; optimized substring and DP subsequence methods are typically O(n^2).",
                "The key optimized idea is reuse: center expansion for substrings, DP tables for subsequences and partitioning.",
            ),
            _entry(
                113,
                "Discuss edge cases such as empty strings, single characters, null input, negative numbers, and overflow.",
                "Good palindrome solutions define what happens for empty input, one-character input, and nulls. Numeric variants should reject negative numbers under the usual signed-number rule and protect reversal logic against overflow.",
                """boolean empty = PalindromeSolutions.BasicStringSolutions.isPalindrome("");
boolean single = PalindromeSolutions.BasicStringSolutions.isPalindrome("a");
boolean negative = PalindromeSolutions.NumberPalindromeSolutions.isPalindromeWithNegativeRule(-121);
OptionalInt reversed = PalindromeSolutions.NumberPalindromeSolutions.reverseIntSafely(Integer.MAX_VALUE);""",
                "Edge handling adds only O(1) overhead beyond the main algorithm.",
                "The optimized mindset is to reject impossible cases early and guard risky operations such as numeric reversal.",
            ),
        ],
    ),
]


def markdown_lines() -> List[str]:
    lines: List[str] = []
    lines.append("# Java Palindrome Answer Book")
    lines.append("")
    lines.append("This document answers all 113 original palindrome questions one by one.")
    lines.append("Each question is followed immediately by:")
    lines.append("")
    lines.append("- a direct answer")
    lines.append("- a Java solution or usage snippet")
    lines.append("- time/space complexity")
    lines.append("- an optimized approach note where applicable")
    lines.append("")
    lines.append("Primary runnable source:")
    lines.append("")
    lines.append("- `src/main/java/PalindromeSolutions.java`")
    lines.append("")
    for section in SECTIONS:
        lines.append("---")
        lines.append("")
        lines.append(f"## {section.title}")
        lines.append("")
        for entry in section.entries:
            lines.append(f"### Question {entry.number}")
            lines.append("")
            lines.append(entry.question)
            lines.append("")
            lines.append("**Answer**")
            lines.append("")
            lines.append(entry.answer)
            lines.append("")
            lines.append("**Java Solution**")
            lines.append("")
            lines.append("```java")
            lines.extend(entry.java_solution.splitlines())
            lines.append("```")
            lines.append("")
            lines.append("**Complexity**")
            lines.append("")
            lines.append(f"- {entry.complexity}")
            lines.append("")
            lines.append("**Optimized Approach**")
            lines.append("")
            lines.append(entry.optimized)
            lines.append("")
    return lines


def write_markdown() -> None:
    MARKDOWN_PATH.write_text("\n".join(markdown_lines()) + "\n", encoding="utf-8")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="BookTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#111827"),
            spaceBefore=12,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="QuestionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=14,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=8,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTight",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Label",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.4,
            leading=12,
            textColor=colors.HexColor("#111827"),
            spaceBefore=4,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            fontName="Courier",
            fontSize=7.2,
            leading=9,
            leftIndent=10,
            rightIndent=10,
            borderWidth=0.5,
            borderColor=colors.HexColor("#cbd5e1"),
            backColor=colors.HexColor("#f8fafc"),
            spaceBefore=2,
            spaceAfter=6,
        )
    )
    return styles


def build_pdf() -> None:
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Java Palindrome Answer Book",
        author="Cursor Cloud Agent",
    )

    story = []
    story.append(Paragraph("Java Palindrome Answer Book", styles["BookTitle"]))
    story.append(
        Paragraph(
            "All 113 palindrome questions with answers, Java snippets, complexity, and optimization notes.",
            styles["BodyTight"],
        )
    )
    story.append(Spacer(1, 10))

    for section_index, section in enumerate(SECTIONS):
        if section_index > 0:
            story.append(PageBreak())
        story.append(Paragraph(section.title, styles["SectionHeading"]))
        for entry in section.entries:
            story.append(Paragraph(f"Question {entry.number}", styles["QuestionHeading"]))
            story.append(Paragraph(entry.question, styles["BodyTight"]))
            story.append(Paragraph("Answer", styles["Label"]))
            story.append(Paragraph(entry.answer, styles["BodyTight"]))
            story.append(Paragraph("Java Solution", styles["Label"]))
            story.append(Preformatted(entry.java_solution, styles["CodeBlock"]))
            story.append(Paragraph("Complexity", styles["Label"]))
            story.append(Paragraph(entry.complexity, styles["BodyTight"]))
            story.append(Paragraph("Optimized Approach", styles["Label"]))
            story.append(Paragraph(entry.optimized, styles["BodyTight"]))
            story.append(Spacer(1, 4))

    doc.build(story)


def main() -> None:
    write_markdown()
    build_pdf()
    print(f"Wrote markdown: {MARKDOWN_PATH}")
    print(f"Wrote pdf: {PDF_PATH}")


if __name__ == "__main__":
    main()
