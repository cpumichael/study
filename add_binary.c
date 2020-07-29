
/*
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 
Constraints:

    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.

*/

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char *
ab(char *a, char *b, char *c)
{
    // adds binary looking null terminated strings and stores
    // the result in another preallocated buffer that is large
    // enough to hold the result of at a buffer the size of
    // MAX(len(a), len(b)) + 2 characters
    // assumes proper null terminated strings consisting of only 0's
    // and 1's
    int ret=0, i, j, a_len = strlen(a), b_len = strlen(b);
    int out_len = 0;

    // ignore initial 0 input
    while (*a == '0') { a += 1; a_len--; }
    while (*b == '0') { b += 1; b_len--; }

    if (a_len > b_len) {
        out_len = a_len + 1;
    } else if (a_len == b_len) {
        out_len = a_len + 2;
    } else if (b_len > a_len) {
        out_len = b_len + 1;
    }

    // sum up all of a & b's respective bits
    for (j = 0, i = a_len - 1; i >= 0; i--, j++) {
        ret += (a[i] == '1') << j;
    }
    for (j = 0, i = b_len - 1; i >= 0; i--, j++) {
        ret += (b[i] == '1') << j;
    }
    
    memset(c, 0, out_len + 1); // ensure c is cleared out including the null

    // copy the proper bit values to c
    for (i = out_len - 1, j = 0; i >= 0; i--, j++) {
        c[i] = ((ret >> j) & 1) ? '1' : '0';
    }

    // clean up any initial 0s
    while (c[0] == '0') {
        memmove(&c[0], &c[1], out_len);
    }

    return c;
}

int
main(int argc, char **argv)
{
    char *res = malloc(100);
    char *a = argv[1];
    char *b = argv[2];

    printf("%s + %s = %s\n", a, b, ab(a, b, res));

    return 0;
}

// vim: cindent sw=4 ts=4 et showmatch
