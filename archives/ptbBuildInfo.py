import requests
import re
import json


def getPTBData():
    """
    Gets the PTB client data.
    :return:
    """
    discord_ptb_request = requests.get(f"https://ptb.discord.com/app")

    jsFileRegex = re.compile(r'([a-zA-z0-9]+)\.js', re.I)

    assetFileSearch = jsFileRegex.findall(discord_ptb_request.text)[-1]

    assetFileRequests = requests.get(f'https://ptb.discord.com/assets/{assetFileSearch}.js')

    try:
        jsFileRegex = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+')
        ptb_build_strings = jsFileRegex.findall(assetFileRequests.text)[0].replace(' ', '').split(',')
    # Error handling
    except (RuntimeError, TypeError, NameError):
        print('Something went wrong, check the code above as that could be the likely cause.')

    build_num = ptb_build_strings[0].split(':')[-1]

    build_hash = ptb_build_strings[1].split(':')[-1]

    build_id = build_hash[:7]

    return build_num, build_hash, build_id


def printPTBBuildInfo():
    """
    Prints the PTB data obtained.
    It is not really a needed feature but you can get an idea of what the data looks like in general.
    :return:
    """
    printPTBBuildInfo.build_num, printPTBBuildInfo.build_hash, printPTBBuildInfo.build_id = getPTBData()

    # This just prints the final data that was obtained from the request
    print(
        f'PTB Build Number: {printPTBBuildInfo.build_num}\nPTB Build Hash: {printPTBBuildInfo.build_hash}\n'
        f'PTB Build ID: {printPTBBuildInfo.build_id}')


def writePTBDataToFile(file_path):
    """
    Writes the PTB data obtained to the provided JSON file path.
    NOTICE: This is a somewhat unstable feature and one JSON file should be used for storing the data.
    :param file_path:
    :return:
    """
    writePTBDataToFile.build_num, writePTBDataToFile.build_hash, writePTBDataToFile.build_id = getPTBData()
    # This just writes the data to a JSON file
    ptb_build_data = {'ptb_build_info': []}
    ptb_build_data['ptb_build_info'].append({
        'ptb_build_number': writePTBDataToFile.build_num,
        'ptb_build_hash': writePTBDataToFile.build_hash,
        'ptb_build_id': writePTBDataToFile.build_id
    })
    # Opens file and dumps the JSON data declared earlier
    with open(file_path, 'w') as outfile:
        # Pretty-printing and sending the data to a JSON file
        json.dump(ptb_build_data, outfile, indent=2)


def ptbDataJSON():
    """
    Returns PTB data as a JSON object.
    Please parse the data to avoid further issues when handling the data.
    :return:
    """
    ptbDataJSON.build_num, ptbDataJSON.build_hash, ptbDataJSON.build_id = getPTBData()
    ptb_build_data = {'ptb_build_info': []}
    ptb_build_data['ptb_build_info'].append({
        'ptb_build_number': ptbDataJSON.build_num,
        'ptb_build_hash': ptbDataJSON.build_hash,
        'ptb_build_id': ptbDataJSON.build_id
    })
    parsed_ptb_data = json.dumps(ptb_build_data)
    return parsed_ptb_data
