import requests
import re
import json


def getCanaryData():
    """
    Gets Canary client data and returns it.
    :return:
    """
    # No longer using canary.discordapp.com/app since discord is dropping the domain
    discord_canary_request = requests.get(f"https://canary.discord.com/app")

    # Regex search filter that gets the JS files, possible to this in node.js but not sufficient
    jsFileRegex = re.compile(r'([a-zA-z0-9]+)\.js', re.I)

    # Gets the asset files which are scrambled after every build update, we are always getting the last file name
    assetFileSearch = jsFileRegex.findall(discord_canary_request.text)[-1]

    assetFileRequests = requests.get(f'https://canary.discord.com/assets/{assetFileSearch}.js')

    try:
        jsBuildRegex = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+')
        canary_build_strings = jsBuildRegex.findall(assetFileRequests.text)[0].replace(' ', '').split(',')
    # Error handling
    except (RuntimeError, TypeError, NameError):
        print('Something went wrong, check the code above as that could be the likely cause.')

    build_num = canary_build_strings[0].split(':')[-1]

    build_hash = canary_build_strings[1].split(':')[-1]

    build_id = build_hash[:7]

    return build_num, build_hash, build_id


def printCanaryBuildInfo():
    """
    Prints Canary client data to give some visualization.
    :return:
    """
    printCanaryBuildInfo.build_num, printCanaryBuildInfo.build_hash, printCanaryBuildInfo.build_id = getCanaryData()

    # This just prints the final data that was obtained from the request
    print(
        f'Canary Build Number: {printCanaryBuildInfo.build_num}\nCanary Build Hash: {printCanaryBuildInfo.build_hash}\n'
        f'Canary Build ID: {printCanaryBuildInfo.build_id}')


def writeCanaryDataToFile(file_path):
    """
    Writes obtained Canary client data to the given JSON file path.
    NOTICE: This is a somewhat unstable feature and one JSON file should be used for storing the data.
    :param file_path:
    :return:
    """
    writeCanaryDataToFile.build_num, writeCanaryDataToFile.build_hash, writeCanaryDataToFile.build_id = getCanaryData()
    # This just writes the data to a JSON file
    canary_build_data = {'canary_build_info': []}
    canary_build_data['canary_build_info'].append({
        'canary_build_number': writeCanaryDataToFile.build_num,
        'canary_build_hash': writeCanaryDataToFile.build_hash,
        'canary_build_id': writeCanaryDataToFile.build_id
    })
    # Opens file and dumps the JSON data declared earlier
    with open(file_path, 'w') as outfile:
        # Pretty-printing and sending the data to a JSON file
        json.dump(canary_build_data, outfile, indent=2)


def canaryDataJSON():
    """
    Returns Canary client data as a JSON object.
    Parse the data to avoid errors or other issues.
    :return:
    """
    canaryDataJSON.build_num, canaryDataJSON.build_hash, canaryDataJSON.build_id = getCanaryData()
    canary_build_data = {'canary_build_info': []}
    canary_build_data['canary_build_info'].append({
        'canary_build_number': canaryDataJSON.build_num,
        'canary_build_hash': canaryDataJSON.build_hash,
        'canary_build_id': canaryDataJSON.build_id
    })
    parsed_canary_data = json.dumps(canary_build_data)
    return parsed_canary_data
