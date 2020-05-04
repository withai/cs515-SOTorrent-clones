# cs515-SOTorrent-clones

## parser.py
The ideal first run of this script looks like this:
`python3 parser.py -f <name-of-file-to-parse> -d`
Subsequent calls to parser.py can omit the -d argument as it is used to create the directories in which the code snippets are stored.

The above command will parse and create snippets in individual directories. The "Arguments" section defines the arguments for parser.py.

**Warning** There is no protection from running the parser.py script on the same file twice. If this is done, duplicates of code snippets will be created and are difficult to detect. Care should be taken to avoid doing this.

### Arguments
### -f (Required)
The "file" argument is required, it is the file to be parsed by parser.py.

### -c (Optional)
This is the "count" argument and will display the count of code snippets in each subdirectory *after* the file in the command is parsed.

### -d (Optional)
This is the "directoy creation" argument and will create the appropriate directories for each kind of code snippet in the current working directory of the parser.py file.

### -v (Optional)
This is the "verbose" argument and will output the name of the code snippet file being added in the terminal. It is helpful for viewing the progress of the file parsing operation.


## analysis.py

This python script produces a graph of the number of code blocks present in the top 10 programming languages from the SOTorrent dataset.

Execution instructions:
`python3 analysis.py`

![](https://github.com/withai/cs515-SOTorrent-clones/blob/master/top-10-languages.png)
