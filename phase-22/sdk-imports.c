/* Original Phase 22 SDK-generated static-analysis sample; never executed. */
extern int puts(const char *);
extern unsigned getpid(void);
static const char *message = "Phase 22 static SDK sample";
static volatile int counter;
int main(void) { counter++; puts(message); return (int)getpid(); }
