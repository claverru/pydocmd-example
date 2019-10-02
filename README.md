# PYDOCMD EXAMPLE

We show how to automatically create docs from Python's docstrings.  

Also we add a little script to create a file with project's structure.

## Usage

### Create Image

- Open terminal as administrator.  
- ```cd /path/to/project```  
- ```docker build -t docs .```  

### Run Container

- ```docker run -it -p 80:80 -v "/path/to/delen-analitycs":/usr/src docs bash```  

### Create Structure

- ```python create_structure.py```

### Visualize docs

- ```pydocmd serve -a 0.0.0.0:80```  
- <http://127.0.0.1:80> in browser 