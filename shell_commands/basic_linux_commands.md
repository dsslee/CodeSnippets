# Linux commands fro working with files an directories

1. Display the present working directory
```bash
$ pwd                 # current directory
```

2. List all the content of a directory
```bash
$ ls 
$ ls -la              # includes hidden files and directories
```

3. Change directory 
```bash
$ cd /		            # move to root directory
$ cd ~		            # move to home directory
$ cd ..               # move one level up from current directory
$ cd folder2          # move to folder2
```

4. Create new file
```bash
$ touch file.txt
```

5. Display file contents
```bash
$ cat file            # view single file
$ cat file1 file2     # view multiple files
$ cat -n file         # view contents of lines of a file
$ tail file           # prints last few lines of a file
```

5. Remove file
```bash
$ rm file.txt         # removes a file
$ rm -i file.txt      # removes a file after confirming to delete
$ rm -f file.txt	    # forecefully remove a file
```

6. Create new directory
```bash
$ mkdir new_folder
$ mkdir -p new_folder/nested_folder/another
```

7. Remove directory
```bash
$ rmdir new_folder      # deletes directory provide its empty
$ rmdir -r new_folder 	# recursively deletes directory along with its content
$ rmdir -rf new_folder  # forcefully and recursively deletes directory along with its content
```

8. Copy and move file/directory
```bash
$ cp file               # view single file
$ mv file ../folder/.   # move single file
$ mv file newname       # change filename
```

9. changes permission
```bash
$ chmodp file           # view single file
```

10. Find files
```bash
$ find /home/username/ -name "*.err"    # searches for *.err files in the /home/username/ directory and all sub-directories
$ locate
```

11. Compressing and extracting 
```bash
$ zip folder.zip                    # compressing to zip 
$ unzip folder.zip                  # extracting zip

$ tar cvf [tarfile.tar] [folder]    # compressing to tar 
$ tar -cvf                          # extracting tar

$ tar -zcvf                         # compressing tar.gz 
$ tar -zxvf                         # extracting tar.gz
```

12 . Other useful commands
```
$ history n                         # n list of  commands
```

