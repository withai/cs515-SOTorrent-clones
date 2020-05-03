# cs515-SOTorrent-clones

## parser.py
The ideal first run of this script looks like this:
`python3 parser.py -f <name-of-file-to-parse> -d`
Subsequent calls to parser.py can omit the -d argument as it is used to create the directories in which the code snippets are stored.

The above command will parse and create snippets in individual directories. The next section defines the arguments for parser.py.

### Arguments
### -f
The "file" argument is required, it is the to be parsed by parser.py.

### -c
This is the "count" argument and will display the count of code snippets in each subdirectory **after** the file in the command is parsed.

### -d
This is the "directoy creation" argument and will create the appropriate directories for each kind of code snippet in the current working directory of the parser.py file.

### -v
This is the "verbose" argument and will output the name of the code snippet file being added in the terminal. It is helpful for viewing the progress of the file parsing operation.

## Warning
There is no protection from running the parser.py script on the same file twice. If this is done, duplicates of code snippets will be created and are difficult tto detect. Care should be taken to avoid doing this.
