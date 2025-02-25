# Training Resources

List of vulnerable applications separated by topics:

---

### Classic Buffer Overflow
> Short descripttion of what a classic Buffer Overflow is all about
> keywords: eip, 41414141, no-protection

Lab: https://samsclass.info/127/proj/lbuf1.htm
Description:
Write-up Solution:

https://samsclass.info/127/proj/lbuf2.htm

### Egghunters
> Short descripttion of what an Egghunter is all about
> keywords: small-buffer

**Egghunter Labs:**
Lab:

Description:

Write-up Solution:

### Structured Exception Handling (SEH)
> Short descripttion of what a SEH is all about
> keywords: seh, windows, cpp, dll

**SEH Labs:**
Lab:

Description:

Write-up Solution:

### Data Execution Prevention (DEP)
> Short descripttion of what a DEP is all about
> keywords: rop, return-oriented-programming

**DEP Labs:**
Lab:

Description:

Write-up Solution:

### Address Space Layout Randomization (ASLR)
> Short descripttion of what an ASLR is all about
> keywords: 

**ASLR Labs:**
Lab:

Description:

Write-up Solution:

https://pax.grsecurity.net/docs/aslr.txt

### No eXecute bit (NX)
> Short descripttion of what NX is all about
> keywords: jumps

**NX Labs:**
Lab:

Description:

Write-up Solution:


---

## Techniques

### ROP - Return Oriented Programming

### Ret2libC

### Return into system()

---

## Heap Corruption

---

Classic Stack Buffer Overflow
https://www.youtube.com/watch?v=qSnPayW6F7U&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G

Structured Exception Handling - SEH
https://www.youtube.com/watch?v=bzOpI6-blfo

Data Execution Prevention (DEP) - bypass with ROP
https://www.youtube.com/watch?v=4_xSGvD0GNk

Egghunters - Very short Buffer
https://www.helviojunior.com.br/it/security/criacao-de-exploits/criacao-de-exploits-parte-3-estudo-de-caso-vulnserver-kstet-com-egghunter/

PRACTICE LABS

Minishare 1.4.1 --> HEAD/POST Remote Buffer Overflow
https://www.exploit-db.com/exploits/45999

WarFTP 1.65 - 'USER' Remote Buffer Overflow
https://www.exploit-db.com/exploits/3570

Simple Web Server 2.2 Buffer Overflow (SEH)
https://www.oppositionsecurity.com/simple-web-server-2-2-buffer-overflow-seh/
http://www.pmx.it/software/sws.asp

Freefloat FTP Server 1.0 - 'STOR' Remote Buffer Overflow
https://www.exploit-db.com/exploits/46763
https://learning.oreilly.com/library/view/penetration-testing-with/9781788473736/ae22d1e3-2758-4035-9230-650cfc8f2a8c.xhtml
https://medium.com/@codingkarma/free-float-ftp-pop-calc-exe-via-stack-overflow-3be11ce23570


Freefloat FTP Server 1.0 - 'MKD' Remote Buffer Overflow
https://www.exploit-db.com/exploits/17539
https://learning.oreilly.com/library/view/penetration-testing-with/9781788473736/ae22d1e3-2758-4035-9230-650cfc8f2a8c.xhtml
https://medium.com/@codingkarma/free-float-ftp-pop-calc-exe-via-stack-overflow-3be11ce23570


Sync Breeze Enterprise 10.0.28 - Remote Buffer Overflow
https://www.exploit-db.com/exploits/42928
https://learning.oreilly.com/library/view/penetration-testing-with/9781788473736/13a6eee1-3d0e-4d22-bfc1-2ca5d23dd0c9.xhtml

Easy File Sharing Web Server 7.2 - GET Buffer Overflow (SEH) 
https://www.exploit-db.com/exploits/39008
https://learning.oreilly.com/library/view/penetration-testing-with/9781788473736/72354dc1-c982-4379-abc9-374197d07f5c.xhtml

DVD X Player Standard 5.5.3.9 - Buffer Overflow
https://www.exploit-db.com/exploits/44438

DVD X Player 5.5 Pro - Local Buffer Overflow (SEH) 
https://www.exploit-db.com/exploits/46962

Brainpan
https://medium.com/@codingkarma/free-float-ftp-pop-calc-exe-via-stack-overflow-3be11ce23570

PCMan FTP Server 2.0.7
https://www.exploit-db.com/exploits/26471
https://medium.com/@mtucunduva98/buffer-overflow-pcman-ftp-server-2-0-7-e143ff3473c

Savant Web Server 3.1 - Remote Buffer Overflow (1)
https://www.exploit-db.com/exploits/781

Seattle Lab Mail (SLmail) 5.5 - POP3 'PASS' Remote Buffer Overflow (1)
https://www.exploit-db.com/exploits/638
https://medium.com/@rafaelrenovaci/buffer-overflow-slmail-5-5-fad2a67316dc

VeryPDF Image2PDF Converter - Local Buffer Overflow (SEH) 
https://www.exploit-db.com/exploits/38423
https://github.com/angelorighi/exploits/blob/master/Image2PDF-seh-poc.py


INTERESTING REFERENCES

Exploit Development Course (Extreme IMPORTANT!)
https://ocw.cs.pub.ro/courses/cns/labs/lab-08

Bypassing non-executable memory, ASLR and stack canaries on x86-64 Linux
https://www.antoniobarresi.com/security/exploitdev/2014/05/03/64bitexploitation/

Exploit Dev 101: Bypassing ASLR on Windows
https://www.abatchy.com/2017/06/exploit-dev-101-bypassing-aslr-on.html

Exploit Mitigation Techniques - Stack Canaries (Extremely GOOD!)
https://0x00sec.org/t/exploit-mitigation-techniques-stack-canaries/5085

Exploit Mitigation Techniques - Data Execution Prevention (DEP) - Extremely Good
https://0x00sec.org/t/exploit-mitigation-techniques-data-execution-prevention-dep/4634

Ultra Top Blog:
GCC protection flags
https://outflux.net/blog/archives/2014/01/27/fstack-protector-strong/

5.2 Kernel Review
https://outflux.net/blog/archives/2019/07/17/security-things-in-linux-v5-2/

The Frame Pointer Overwrite
http://www.phrack.com/issues/55/8.html#article

BYPASSING STACKGUARD AND STACKSHIELD
http://phrack.org/issues/56/5.html

OSCP Exploits Repo
https://github.com/codingo/OSCP-2/tree/master/Exploits

Write-up OSCE prep
https://github.com/freddiebarrsmith/Buffer-Overflow-Exploit-Development-Practice

FUZZY SECURITY
http://fuzzysecurity.com/tutorials.html

Corelan
https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/

Exploit Development - Linux Platforms + ret2libc and more bypasses
https://ihazomgsecurityskillz.blogspot.com/
https://vimeo.com/user5676486

IDA Pro Course
https://tuts4you.com/e107_plugins/download/download.php?list.67

he advanced return-into-lib(c) exploits: PaX case study
https://www.win.tue.nl/~aeb/linux/hh/phrack/P58-04
