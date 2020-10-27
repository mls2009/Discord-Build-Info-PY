# universal import
from discord_build_info_py import *

# Client tests
printClientData('canary')
print(clientBuildDataJSON('canary'))

# JSON tests
print(clientBuildDataJSON('canary'))

"""
These are deprecated
"""
# canary import
# from discord_build_info_py import getCanaryData, printCanaryBuildInfo, writeCanaryDataToFile
# ptb import
# from discord_build_info_py import getPTBData, printPTBBuildInfo, writePTBDataToFile
# stable import
# from discord_build_info_py import getStableData, printStableBuildInfo, writeStableDataToFile

# Canary Tests
# printCanaryBuildInfo()

# PTB tests
# printPTBBuildInfo()

# Stable tests
# printStableBuildInfo()
