# AirBnB_clone
<p align="center">
  <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240205T180432Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=435832dbbf2ed1cf01a478c355d6934f79225c66038a0936e789adb1ef5d48ea">
</p>
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


