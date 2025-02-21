# Exploit Development

List of vulnerable applications separated by topics:

---

## Stack Corruption

### Smashing the Stack - Classic Buffer Overflow
> Short descripttion of what a classic Buffer Overflow is all about

> keywords: eip, 41414141, no-protection

[Link Here](https://github.com/jpdejavitecs/ExploitDevelopment/blob/master/protections/classic-bof.md)

### Egghunters
> Short descripttion of what an Egghunter is all about

> keywords: small-buffer

[Link here](https://github.com/jpdejavitecs/ExploitDevelopment/blob/master/protections/egghunters.md)

### Structured Exception Handling (SEH)
> Short descripttion of what a SEH is all about

> keywords: seh, windows, cpp, dll

[Link here](https://github.com/jpdejavitecs/bufferoverflow/blob/master/protections/seh.md)

### Data Execution Prevention (DEP)
> Short descripttion of what a DEP is all about

> keywords: rop, return-oriented-programming

[Link here](https://github.com/jpdejavitecs/bufferoverflow/blob/master/protections/dep.md)

### Supervisor Mode Access Prevention - SMEP
> Short descripttion of what a SMEP is all about

> keywords: rop, return-oriented-programming

[Link here](https://github.com/jpdejavitecs/bufferoverflow/blob/master/protections/smep.md)

### Address Space Layout Randomization (ASLR)
> Short descripttion of what an ASLR is all about

> keywords: 

[Link here](https://github.com/jpdejavitecs/ExploitDevelopment/blob/master/protections/aslr.md)

https://pax.grsecurity.net/docs/aslr.txt

### No eXecute bit (NX)
> Short descripttion of what NX is all about

> keywords: jumps

[Link here](https://github.com/jpdejavitecs/ExploitDevelopment/blob/master/protections/nx.md)


---

## Techniques

### ROP - Return Oriented Programming

[Windows Lab](https://h0mbre.github.io/Creating_Win32_ROP_Chains/#)

[Linux Lab](https://www.hackingarticles.in/hack-the-rop-primer-1-0-1-ctf-challenge/)

### Ret2libC

[Link here](https://github.com/firmianay/Life-long-Learner/blob/master/SEED-labs/return-to-libc-attack-lab.md)

### Return into system()

[Link here]()

---

## Heap Corruption

### Heap Spray

https://www.corelan.be/index.php/2011/12/31/exploit-writing-tutorial-part-11-heap-spraying-demystified/
