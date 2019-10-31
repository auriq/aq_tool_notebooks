# Jupyter Notebooks for aq_tools

Collections of the jupyter notebooks for aq_tool examples, where users can learn basic usage of aq_tools interactively.


**Note**<br>
* This notebook is based on AQ Tools version: 2.0.1-2
* For setup, follow [setup](setup.md)
* do not delete the text files, as they might be sample data file for notebooks

## Table of Contents
### aq_tools
Options that are commonly used in all aq_tools.
- [aq-input](aq_input.ipynb) - input specification for all of aq_tools
- [aq-outupt](aq_output.ipynb) - output specification for all of aq_tools
- [aq-emod](aq-emod.ipynb): use this as a reference for various builtin funtions.

#### aq_pp
- [aq_pp -eval](aq_pp%20-eval.ipynb) - option for executing evaluation, such as arithmatic and more.
- [aq_pp -filt](aq_pp%20-filt.ipynb) - filtering / selection of record based on given condition.
- [aq_pp -map](aq_pp%20-map.ipynb) - extracting, mapping and manipulation of string.
- [aq_pp -cmb](aq_pp%20-cmb.ipynb) - data lookup option, also can be used for joining datasets
	* also includes examples of `-mapf` and `-mapc`
- more on its way...

#### [aq_cnt](aq_cnt.ipynb)
This command helps users to find out more details about data stored in any given column, such as unique values, distribution of them, as well as column statistics.

## Recommended order for notebooks
Beginning users are encouraged to follow learning path to get familiarize yourself with basic syntax, as well as simple usage examples of each commands.

The following 2 notebooks go over input, column and output specs for aq_tools in general.
1. [aq_input](aq_input.ipynb)
2. [aq_output](aq_output.ipynb)

Others go over what can be done with `aq_pp` command's options, from conditional control to string manipulation. Feel free to go over them in any order you'd like.
- [aq_pp -eval](aq_pp%20-eval.ipynb)
- [aq_pp -filt](aq_pp%20-filt.ipynb)
- [aq_pp -map](aq_pp%20-map.ipynb)

## Some DS Project using Essentia
- [Amazon Product Reviews EDA with Essentia](projects/amazon_review/Amazon%20Product%20Review%20Dataset%20Analysis.ipynb)

