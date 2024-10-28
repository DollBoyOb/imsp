# IMSP

**IMSP** -  Turing-complete esoteric programming language inspired by spacing between gray slabs at the park. IMSP is an acronym, which stands for  **I**nterval **M**ejdu **S**erymi **P**litami (Spacing Between Gray Slabs)

## Tutorial ##
IMSP have 9-cells memory and 6 commands with their modes.

### `0` - Input and Output ###
The `0` command outputs and inputs in different modes. `0` command have 4 modes:

* **`1`** - **Reversed ASCII mode**. Given arguments are reversed and translated to ASCII character. Example: `0 1 2 7` that outputs the letter `H`. 
* **`2`** - **Binary mode** All arguments subtracts by first argument and translates to decimal. Example `0 2 3 4 3 3 4 3 3 3`, first argument is `3`, and other arguments subtracts by `3`. Or simply `433433 - 333333 = 100100` and `100100` is `72`, that in ASCII its `H`
* **`3`** - **Memory-output mode**. Outputs the 
value from cell of memory.
* **`4`** - **Memory-input mode**. Writes a value to a cell of memory by user

### `1` - Save in memory ###
The `1` command are working with memory, saving something inside of it, and its have 4 modes:

**Syntax** - `1 <cell pos> <mode> <other arguments>`

* **`0`** - **Reversed ASCII mode**. Given arguments are reversed and translated to ASCII character. Same as mode `1` in `0` command
* **`1`** - **Number mode.** Saving in memory `int` number. Example `1 1 1 1` - saving number `1` in second cell of memory
* **`2`** - **Copy mode.** Copies cell to other cell
* **`3`** - **Index mode.** Saving in memory cell the index of a string from other cell. Example `1 0 3 1 2`, same as `mem[0] = mem[1][mem[2]]`  

### `2` - Math operations ###
This command computing math and saves result in cell of memory. Operations are designated in a specific order: **+**, **-**, *, **/**,**%**

**Syntax** - `2 <cell pos> <operation> <cell pos> <cell pos>`
 
If we want to add first cell and second cell, and save the result in third cell, the code will be this: `2 0 0 1 2` 

Its also works with strings!

### `3` - If ###
Command working with conditions, and operators are designated in a specific order: **==, <, >, !=**
 
**Syntax** - 
`3 <cell pos> <operator> <cell pos>`

If condition are false, the next are skips, in this example the condition are true, so output of this script is `A`
```
3 1 3 2 (if mem[1] != mem[2])
0 1 5 6
```

### `4` - Jump ###
This command just jumping on line of code

**Syntax** - `4 <number>`

### `5` - Halt ###
This command halts the programm


## Examples ##
### Hello World ###
```
0 1 2 7 
0 1 1 0 1
0 1 8 0 1
0 1 8 0 1
0 1 1 1 1
0 1 2 3
0 1 7 8
0 1 1 1 1
0 1 4 1 1
0 1 8 0 1
0 1 0 0 1
```

### Fibonacci sequence ###
```
1 3 1 0
1 4 1 1
0 3 3
0 1 0 1
0 3 4
0 1 0 1
1 2 1 10
1 1 1 1
2 3 0 4 5
0 3 5
1 6 2 3
1 3 2 4
2 6 0 4 4
2 0 0 1 0
0 1 0 1
3 0 3 2
4 6
3 0 0 2
5
```
### Truth Machine ###
```
0 4 0
1 1 1 1
3 0 0 2
0 3 0
3 0 0 1
0 3 0
3 0 0 1
4 4
```
