Write a Python program that accepts two arguments:

1. The name of a given file (the source file).
2. The name of a new file (the destination file).

The program should read the content of the source file, sort it, and write the sorted content to the destination file. If the destination file does not exist, it should be created; otherwise, it should be overwritten.

### Example

```console
$ ./sort unordered.txt sorted.txt
$ cat unordered.txt
2
3
1
$ cat sorted.txt
1
2
3
```
