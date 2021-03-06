# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cp: makes copy of a file and puts it in another directory

mv: moves original file to another directory

find: finds files in a given directory

grep: finds particular strings in a given file

kill: terminates a process

ls: lists files and directories

pwd: prints working directory

man: displays documentation for command

rm: removes files or directories ; use option -r to delete non-empty directory

sort: sorts a given file

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`: lists files and directories in current directory

`ls -a`: same as above including hidden dot files (a)

`ls -l`: displays files and directories in long format (l) ; gives information on size, ownership, modification date

`ls -lh`: same as above except that it displays the units for the file sizes (B, K, etc.) ; meant to be human readable (h)

`ls -lah`: in addition to the above, also displays information on hidden files

`ls -t`: lists all files and directories sorted by time modified (t) with most recently modified first and then going down  
columns

`ls -Glp`: lists files and directories in long form (l) with colorized output (G) and putting a slash after filenames that are directories (p) ; in my case the directory names were now in blue and everything else remained black

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -r`: displays files in reverse alphabetical order

`ls -hlS`: displays files in human readable long form with largest files first

`ls -1`: displays one file per line

`ls -m`: displays files as comma separated list

`ls -lT`: display complete time information about each file including hour, minute, second, month, day, and year

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command reads from standard input and converts each line (element separated by whitespace) into arguments to another command.

ex) `find . -name "*.c" -print0 | xargs -0 rm -rf`: removes all files ending in ".c" in the current directory including the ones that have spaces in their names ; the -print0 option of find puts a null character at the end of each filename and the -0 option of xargs makes it treat null characters as delimiters rather than spaces

ex) `echo dir1 dir2 | xargs ls`: lists the files in the directory named dir1 and in the directory named dir2

 

