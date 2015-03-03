# Licenser
Inserts license text into source files.

*License is inserted as-is. It is recommended that license text is wrapped in comment block or equivalent.*

## Usage
Full help available via ```python licenser.py --help```

Has 2 positional and 2 optional arguments.
Positional arguments:

* path - path to target directory
* license - file with license text

Optional
* --extensions extensions of target files (if left empty, licenser will attempt to insert into every file)
* --ignorefiles name of file which should be ignored


## Samples
Insert license into every file in current directory (includes licenser.py!):

```python licenser.py . license.txt```


Insert into every .cs file:

```python licenser.py MyProject\ license.txt --extensions .cs```


Insert license into every .cpp and .h file, but ignore main.cpp

```python licenser.py targetdir\ license.txt --extensions .cpp .h --ignorefiles main.cpp```
