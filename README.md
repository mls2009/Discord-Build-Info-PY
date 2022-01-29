<div align="center">
  <p>
    <a href="https://github.com/KiyonoKara/Discord-Build-Info-PY/releases"><img src="https://img.shields.io/github/v/release/KiyonoKara/discord-build-info-py?display_name=tag&sort=semver" alt="Version" /></a>
    <a href="LICENSE.md"><img src="https://img.shields.io/github/license/KiyonoKara/discord-build-info-py?color=007ace" alt="License" /></a>
  </p>
</div>

# Discord Build Info Module

`Discord Build Info PY` is a Python 3 module made for obtaining the build information of the Discord (Talk, Video & Chat) app.
Discord has 3 mainstream clients: Stable, Canary, PTB (Public Test Build) which all have build information. 
  

[**Important Notice**](#project-status)
  

## Usage
This module quickly retrieves Discord's information for its release channels and provides the data in one single call. It is useful for obtaining the version data and nothing else. This module does not scrape Discord nor its API at all and only returns the data that is needed.

## Installation

To install the package, you may use:  
```bash
pip install git+https://github.com/<MAINTAINER>/Discord-Build-Info-PY.git#egg=discord-build-info-py
```

## Warnings
- Built-in functions which allow you to write data to files must be used carefully since it can potentially overwrite data—use a separate JSON file for the data.
- This library purely serves to obtain Discord platform's build number, hash, and ID. 

## Legal
`Discord-Build-Info-PY` is not affiliated or endorsed by Discord nor its assets.
Discord is a registered trademark of Discord Inc. and does not own this repository. Discord and Discord Inc's official app & website is found at https://discord.com.

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
      1. Calling a variable from it: `build_num` —— Calls the build number and that is it.
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
Outputs: **build number**, **build hash**, and **build id** which change every few hours and do not remain the same.  


#### Array-like approach
```python
from discord_build_info_py import *
# Assign one variable to the function
build_info = getClientData("canary")
print(build_info[0], build_info[1], build_info[2])
```
Outputs: **build number**, **build hash**, and **build id** which change every few hours and do not remain the same. 

## Contributing
Contributions are closed.  

## Project Status
Complete. Discontinued.  
This project and library will remain on GitHub. However, it will no longer be subject to further updates and versions since it is discontinued. __This project is no longer maintained on PyPI.__

## License
[Apache 2.0 License](LICENSE.md)
