/* Original compiler-generated FreeBSD negative control. Static import only. */
static int square(int x) { return x*x; }
int _start(void) { volatile int input=7; return square(input); }
