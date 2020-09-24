# canary import
from discordbuildinfopy import getCanaryData, printCanaryBuildInfo, writeCanaryDataToFile
# ptb import
from discordbuildinfopy import getPTBData, printPTBBuildInfo, writePTBDataToFile
# stable import
from discordbuildinfopy import getStableData, printStableBuildInfo, writeStableDataToFile
# general client import
from discordbuildinfopy import getClientData, printClientData, writeClientDataToLocalFile
# universal import
from discordbuildinfopy import *

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
