<div align="center">
  <p>
    <a href="https://pypi.org/project/discord-build-info-py/"><img src="https://img.shields.io/pypi/v/discord-build-info-py.svg" alt="PyPI Package Version" /></a>
    <a href="https://pypistats.org/packages/discord-build-info-py"><img src="https://img.shields.io/pypi/dm/discord-build-info-py?color=1" alt="Downloads Per Month" /></a>
    <a href="https://pypi.org/project/discord-build-info-py/"><img src="https://img.shields.io/pypi/format/discord-build-info-py.svg" alt="PyPI Format" /></a>
    <a href="LICENSE.md"><img src="https://img.shields.io/github/license/KaNguy/discord-build-info-py?color=007ace" alt="License" /></a>
  </p>
</div>

# Discord Build Info Module

`Discord Build Info PY` is a Python 3 module capable of getting the build information of the Discord (Talk, Video & Chat) app.
Discord has 3 mainstream clients: Stable, Canary, PTB (Public Test Build) which all have build information. 

## Why use this?
This module is great for developers who want to quickly retrieve build information from the Discord clients. Instead of going through the hassle of setting up a file that makes a request and gets the Discord client build information, this module already covers that for you.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.   
Or follow instructions from the module at https://pypi.org/project/discord-build-info-py/

```bash
pip install discord-build-info-py
```

## Before you use
Be aware that the functions that allow you to write data to a file must be used carefully.
These functions can overwrite data so it is recommended to use a dedicated JSON file per client info that you obtain.

# Documentation

## Getting started
**Import all functions from the library** —— Allows you to directly call the functions without having to call the library constant.
```python
from discord_build_info_py import *
```

## Retrieving build info per client
We must first call the function, `getClientData(release_channel_args)`. 

**Returns** `build_num, build_hash, build_id`, in direct order, it is the build number, hash, and ID that is returned.

There are three supported release channels which are `canary`, `ptb`, `stable` which can be provided as the `release_channel_args` upon calling the function.

### Information retrieval options: 
1. Declare three variables and assign it to the method with your provided release channel, you can call these individually. 
   1. Example using the **Canary** client: `build_num, build_hash, build_id = getClientData("canary")` 
      1. Calling an a variable from it: `build_num` —— Calls the build number and that is it.
2. Declare one variable and assign it to the method with your provide release channel, because it will become an array since there are multiple values assigned to one variable, there can only be one variable to be called upon, so indexes must be specified. 
   1. Example using the **Canary** client: `build_info = getClientData("canary)`
      1. Calling it one of the elements: `build_info[0]` —— Calls the build number as it is the first in the index.
 

### Examples of retrieval:

#### Simple approach
```python
from discord_build_info_py import *

# Assigning three variables to the function 
build_num, build_hash, build_id = getClientData("canary")
print(build_num, build_hash, build_id) 
```
Outputs: **build number**, **build hash**, and **build id** which change every few hours and do not remain the same always.  


#### Array-like approach
```python
from discord_build_info_py import *
# Assign one variable to the function
build_info = getClientData("canary")
print(build_info[0], build_info[1], build_info[2])
```
Outputs: **build number**, **build hash**, and **build id** which change every few hours and do not remain the same always. 

## Contributing
No information at the moment.

## License
[Apache 2.0 License](LICENSE.md)
