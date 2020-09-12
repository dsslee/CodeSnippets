# Linux commands fro working with files an directories

1. Display the prsent working directory
```bash
$ pwd
```

2. List all the content of a directory
```bash
$ ls 
$ ls -la      # includes hidden files and directories
```

3. Move aroudn the directory tree
```bash
$ cd /		# move to root directory
$ cd ..      # move one level up from current directory
$ cd folder2  # move to folder2
```

4. Create new file
```bash
$ touch file.txt
```

5. Remove file
```bash
$ rm file.txt       # removes a file
$ rm -f file.txt	# forecefully remove a file
```

6. Create new direcotry
```bash
$ mkdir new_folder
$ mkdir -p new_folder/nested_folder/another
```

7. Remove directory
```bash
$ rmdir new_folder      # deletes directory provide its empty
$ rmdir -r new_folder	# recursively deletes directory along with its content
$ rmdir -rf new_folder  # forcefully and recursively deletes directory along with its content
```



