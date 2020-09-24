# canary import
from discord_build_info_py import getCanaryData, printCanaryBuildInfo, writeCanaryDataToFile
# ptb import
from discord_build_info_py import getPTBData, printPTBBuildInfo, writePTBDataToFile
# stable import
from discord_build_info_py import getStableData, printStableBuildInfo, writeStableDataToFile
# general client import
from discord_build_info_py import getClientData, printClientData, writeClientDataToLocalFile
# universal import
from discord_build_info_py import *

# Canary Tests
# printCanaryBuildInfo()

# PTB tests
# printPTBBuildInfo()

# Stable tests
# printStableBuildInfo()

# Param tests
# printClientData('canary')
# print(clientBuildDataJSON('canary'))

# JSON tests
print(reparse(canaryDataJSON()))
