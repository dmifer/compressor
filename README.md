# Data Compressor

**Descriprion:**

compress.py - compress choosen file

decompress.py - decompress choosen file

entropy.py - calculate entropy
  

**Demonstration** - [Loom](https://www.loom.com/share/c7548b75c57f480b870b516e6c2ad27b)


**Implemented alghoritms:**

 * Move to front - [ITMO](https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_MTF)

 * Burrows-Wheeler transform - [ITMO](https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%91%D0%B0%D1%80%D1%80%D0%BE%D1%83%D0%B7%D0%B0-%D0%A3%D0%B8%D0%BB%D0%B5%D1%80%D0%B0)

 * Huffman algoritm - [ITMO](https://neerc.ifmo.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%A5%D0%B0%D1%84%D1%84%D0%BC%D0%B0%D0%BD%D0%B0), [Stanford](http://web.stanford.edu/class/archive/cs/cs106x/cs106x.1174/assnFiles/assign6/huffman-spec.html)

**Notes:**

 * For BWT used special character for end and start of text instad of number of initial row in matrix of permulations
 
 * All files reading in bytes format
 
 * Huffman encoded tree wrutten to first row in the file


**Ways to improve:**

 * Use only source alphabet 
 
 * Split encoded text to blocks / rows

 * Use *esc* symbol for MTF  
