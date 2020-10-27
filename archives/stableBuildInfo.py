import requests
import re
import json


def getStableData():
    """
    Gets stable build information and returns the data.
    :return:
    """
    discord_stable_request = requests.get(f"https://discord.com/app")

    jsFileRegex = re.compile(r'([a-zA-z0-9]+)\.js', re.I)

    assetFileSearch = jsFileRegex.findall(discord_stable_request.text)[-1]

    assetFileRequests = requests.get(f'https://discord.com/assets/{assetFileSearch}.js')

    try:
        jsFileRegex = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+')
        stable_build_strings = jsFileRegex.findall(assetFileRequests.text)[0].replace(' ', '').split(',')
    # Error handling
    except (RuntimeError, TypeError, NameError):
        print('Something went wrong, check the code above as that could be the likely cause.')

    build_num = stable_build_strings[0].split(':')[-1]

    build_hash = stable_build_strings[1].split(':')[-1]

    build_id = build_hash[:7]

    return build_num, build_hash, build_id


def printStableBuildInfo():
    """
    Gets all stable build info and prints it to make things fancy.
    :return:
    """
    printStableBuildInfo.build_num, printStableBuildInfo.build_hash, printStableBuildInfo.build_id = getStableData()

    # This just prints the final data that was obtained from the request
    # Pretty simple
    print(
        f'Stable Build Number: {printStableBuildInfo.build_num}\nStable Build Hash: {printStableBuildInfo.build_hash}\n'
        f'Stable Build ID: {printStableBuildInfo.build_id}')


def writeStableDataToFile(file_path):
    """
    Writes all stable data obtained to a JSON file that is provided.
    NOTICE: This is a somewhat unstable feature and one JSON file should be used for storing the data.
    :param file_path:
    :return:
    """
    writeStableDataToFile.build_num, writeStableDataToFile.build_hash, writeStableDataToFile.build_id = getStableData()
    # This just writes the data to a JSON file
    stable_build_data = {'stable_build_info': []}
    stable_build_data['stable_build_info'].append({
        'stable_build_number': writeStableDataToFile.build_num,
        'stable_build_hash': writeStableDataToFile.build_hash,
        'stable_build_id': writeStableDataToFile.build_id
    })
    # Opens file and dumps the JSON data declared earlier for stable of course
    # However this requires a separate file
    with open(file_path, 'w') as outfile:
        # Pretty-printing and sending the data to a JSON file
        json.dump(stable_build_data, outfile, indent=2)


def stableDataJSON():
    """
    Returns stable data obtained as a JSON object.
    Please parse the data in order to make sure you can use it.
    :return:
    """
    stableDataJSON.build_num, stableDataJSON.build_hash, stableDataJSON.build_id = getStableData()
    stable_build_data = {'stable_build_info': []}
    stable_build_data['stable_build_info'].append({
        'stable_build_number': stableDataJSON.build_num,
        'stable_build_hash': stableDataJSON.build_hash,
        'stable_build_id': stableDataJSON.build_id
    })
    parsed_stable_data = json.dumps(stable_build_data)
    return parsed_stable_data
