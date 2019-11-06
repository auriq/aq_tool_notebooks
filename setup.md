# Jupyter Notebooks for aq_tools

Make sure following requirements for environments and packages are met.

## Depencendies
### environment
- python3 (python3.6 comes with AMI), virtualenv `python3 -m venv aq_tool_notebooks`
	* dependencies can be found in requirements.txt
- ec2 instance with Essentia AMI
### python packages
- jupyter notebook
- bash_kernel

## To setup
after lanching the instance with the AMI,
1. clone this repo from [auriq github](https://github.com/auriq/aq_tool_notebooks)
2. `cd` into the repo, then create a virtual environment with
	1. `python3 -m venv aq_tool_notebooks`
	2. activate with `source aq_tool_notebooks/bin/activate`
3. install jupyter notebook following instruction of _installing jupyter with pip_ on the [link](https://jupyter.readthedocs.io/en/latest/install.html)
4. follow instrutions on the [jupyter notebook doc](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#notebook-public-server), 
	1. securing with Password. (Skip ssl, maybe use route 53)
	2. Running Notebook server
		1. set up ip, open_browser and port=9999 on jupyter_notebook_config
5. disable Quit button on the notebook on jupyter confing file
5. check and make sure security groups are open appropriately
6. install [bash_kernel](https://pypi.org/project/bash_kernel/) in the virtual env


## Tutorials on how to set up jupyter notebook remotely on ec2
**make sure to read the all 3 steps below**
- [Setting up jupyter notebook on EC2](https://chrisalbon.com/aws/basics/run_project_jupyter_on_amazon_ec2/)
- [Running a jupyter notebook from a remote server](https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/)
- [if you get ssl error when accessing from local](https://stackoverflow.com/questions/36387654/jupyter-on-ec2-ssl-error)

Once everything is set up, **choose bash kernel** when creating a new notebook

## Note
- aq_tools_notebooks/ dir within the project directory (aq_tools_notebooks) is a python virtual env folder. Don't mess with it
