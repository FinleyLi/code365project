/*
 * Program Name: writing-style__.c
 * Subject: "____".
 * Input: "____".
 * Output: "____".
 * Since ____/__/__
 * ___/__/__, add more comment
 * ToolKit: Code::Blocks 20.03
 * Author: Finley
 *         Computer Center, Tatung University
 */
#include <stdio.h>

/**
 * do something
 */
// Return value
int Finley(){
    // code goes here
    return 0;
}

/**
 * do something
 */
// no Return value
void print(int size) {
    // code goes here
	print("*");
    print("\n");
}

/**
 * Subject,
 * description
 */
int main() {
    int size = 0;
    while (scanf("%d", &size) > 0 && size > 0 && size <= 40) {
        print(size);
    }
}
