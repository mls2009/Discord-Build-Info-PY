# Discord Build Info Module

`Discord Build Info PY` is a Python 3 module capable of getting the build information of the Discord (Talk, Video & Chat) app.
Discord has 3 mainstream clients: Stable, Canary, PTB (Public Test Build) which all have build information. 

## Why use this?
This module is great for developers who want to quickly retrieve build information from the Discord clients. Instead of going through the hassle of setting up a file that makes a request and gets the Discord client build information, this module already covers that for you.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package. Or follow instructions from the module at https://pypi.org/project/discord-build-info-py/

```bash
pip install discord-build-info-py
```

## Before you use
Be aware that the functions that allow you to write data to a file must be used carefully.
These functions can overwrite data so it is recommended to use a dedicated JSON file per client info that you obtain.

## Usage Example

```python
import discord_build_info_py as dbpy

# Prints the stable client's build number, hash, and id.
dbpy.printStableBuildInfo()

# Get stable data 
stableNum, stableHash, stableID = dbpy.getStableData();
# Do something with the data 
```

## Contributing
No information at the moment.

## License
[Apache 2.0 License](LICENSE.md)
