# AirBnB_clone
![AirBnB](https://github.com/Adeniyii/AirBnB_clone/blob/main/assets/hbnb_logo.png)
---
# Reading Concepts
## [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages) 
- A python file can be a module but when this file is in a folder, we call this folder a package
- Packages are a way of structuring python's module namespace using "dotted "module names, e.g. the module `a.b` designates a module *b* found in package *a*
- Using dotted module names saves author from having to worry about each other's module name.
- The __`init.py`__ are required to make python treat the directories as containing packages.
- use of `import * from a package`may lead to unwanted side effects , its dangerous  and considered a bad practice . In that case , `__init__.py` should not be empty but must contain a list of modules to load.
- When packages are structured into subpackages, you can use absolute imports to refer to submodules of siblings packages.(Absolute)
- You can also relative imports, with the `from module import name` form of import statement. use leading dots to indicate the current and parent packages involved in the relative import.
__note:__  relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.

## cmd - support for line-oriented command intepreters
- The Cmd class provides a simple framework for writing line oriented command intepreters.
