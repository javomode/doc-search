# <Project Name>

<Command-line tool that indexes and searches document collections. Users can then quickly locate documents containing specific keywords or phrases without manually opening files.>

## Usage

### Index Documents

To index all .txt files within a directory and its subdirectories:

`docsearch index <directory>`

Example:

`docsearch index sample_docs`

This command recursively scans the specified directory for text files, extracts their contents, and stores them in index.json.

### Search Documents

To search indexed documents for a keyword or phrase:

`docsearch search "<query>"`

Example:

`docsearch search "benefits"`

Output:

sample_docs/employee_handbook.txt
sample_docs/vacation_policy.txt
Search with Snippets

To display matching text snippets along with search results:

`docsearch search -s "<query>"`

or

`docsearch search --snippet "<query>"`

Example:

`docsearch search -s "benefits"`

Output:

sample_docs/employee_handbook.txt
...employees are eligible for benefits after 90 days...

sample_docs/vacation_policy.txt
...benefits include paid sick leave and vacation...
View Statistics

To display index statistics:

docsearch stats

Example:

docsearch stats

Output:

Documents indexed: 42

## Typical Workflow

Index a directory:

`docsearch index sample_docs`

Search the indexed documents:

`docsearch search "benefits"`

Search with context snippets:

`docsearch search -s "benefits"`
