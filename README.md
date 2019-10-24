# Jupyter Notebooks for aq_tools

Collections of the jupyter notebooks for aq_tool examples, where users can learn basic usage of aq_tools interactively.

## Table of Contents
### aq_tools
Options that are commonly used in all aq_tools.
- [aq_input](aq_pp%20-eval.ipynb)
- [aq_outupt](aq_output.ipynb)
[//]: # (- [aq_emod](aq_emod.ipynb) this is a comment) 

### aq_pp
- [aq_pp -eval](aq_pp -eval.ipynb) - option for executing evaluation, such as arithmatic and more.
- [aq_pp -filt](aq_pp\ -filt.ipynb) - filtering / selection of record based on given condition.
- [aq_pp -map](aq_pp\ -map.ipynb) - extracting, mapping and manipulation of string.
	* also includes examples of `-mapf` and `-mapc`
- more on its way...

### [aq_cnt](aq_cnt.ipynb)
This command helps users to find out more details about data stored in any given column, such as unique values, distribution of them, as well as column statistics.

## Recommended order for notebooks
Beginning users are encouraged to follow following path (no pun) to get familiarize yourself with basic syntax, as well as simple usage examples of each commands.

The following 2 notebooks go over input, column and output specs for aq_tools in general.
1. [aq_input](aq_input.ipynb)
2. [aq_output](aq_output.ipynb)

Others go over what can be done with `aq_pp` command's options, from conditional control to string manipulation. Feel free to go over them in any order you'd like.
- [aq_pp -eval](aq_pp\ -eval.ipynb)
- [aq_pp -filt](aq_pp\ -filt.ipynb)
- [aq_pp -map](aq_pp\ -map.ipynb)


For setup, follow [setup](setup.md)
### Todo
#### in & output Specs
- input spec
	DONE* Basic
	* advanced
DONE- OUTPUT SPEC

#### aq_pp
- basic options
- advanced options 

#### aq_eod
- transfer from aq_pp -eval
- prettify

DONE #### aq_cnt.ipynb
- comprehensive `aq_cnt` example
	* things that can only be done through `-g` option


#### mini project
Small project for users to follow through, and utilize knowledge gained from past notebooks for real life like data cleaning senario.
**Amazon Review Dataset with anomaly and invliad data?**
