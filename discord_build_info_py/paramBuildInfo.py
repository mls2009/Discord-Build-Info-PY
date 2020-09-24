import requests
import re
import json

release_channels = ['stable', 'canary', 'ptb']


def getClientData(release_channel_args):
    """
    Returns the data based on what release channel is provided.
    :param release_channel_args:
    :return:
    """
    release_channel = ''
    if release_channel_args in release_channels:
        if release_channel_args == 'stable':
            pass
        else:
            release_channel = release_channel_args + '.'

    client_request = requests.get(f"https://{release_channel}discord.com/app")
    # Regex search filter that gets the JS files, possible to this in node.js but not sufficient
    jsFileRegex = re.compile(r'([a-zA-z0-9]+)\.js', re.I)

    # Gets the asset files which are scrambled after every build update, we are always getting the last file name
    assetFileSearch = jsFileRegex.findall(client_request.text)[-1]

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


def printClientData(release_channel_args):
    """
    Prints data based on what release channel is provided.
    :param release_channel_args:
    :return:
    """
    # Calls it from the other method
    printClientData.build_num, printClientData.build_hash, printClientData.build_id = \
        getClientData(release_channel_args)

    release_channel_f = release_channel_args.title()
    if release_channel_f.lower() == 'ptb':
        release_channel_f = release_channel_f.upper()

    # Prints the final data that was obtained from the request for neat formatting
    print(
        f'{release_channel_f} Build Number: {printClientData.build_num}\n'
        f'{release_channel_f} Build Hash: {printClientData.build_hash}\n'
        f'{release_channel_f} Build ID: {printClientData.build_id}')


def writeClientDataToLocalFile(release_channel_args, file_path):
    """
    Writes any data obtained to a JSON file if provided, release channel must also be provided.
    NOTICE: This is a somewhat unstable feature and one JSON file should be used for storing the data.
    :param release_channel_args:
    :param file_path:
    :return:
    """
    writeClientDataToLocalFile.build_num, writeClientDataToLocalFile.build_hash, writeClientDataToLocalFile.build_id = \
        getClientData(release_channel_args)

    release_channel_j = release_channel_args.lower()
    # Declares an object for JSON
    client_build_data = {f'{release_channel_j}_build_info': []}
    client_build_data[f'{release_channel_j}_build_info'].append({
        f'{release_channel_j}_build_number': writeClientDataToLocalFile.build_num,
        f'{release_channel_j}_build_hash': writeClientDataToLocalFile.build_hash,
        f'{release_channel_j}_build_id': writeClientDataToLocalFile.build_id
    })
    # Opens file and dumps the JSON data declared earlier
    with open(file_path, 'w') as outfile:
        # Pretty-printing and sending the data to a JSON file
        json.dump(client_build_data, outfile, indent=2)


def clientBuildDataJSON(release_channel_args):
    """
    Returns the client build data as a JSON object.
    Please parse the object into JSON before calling the attributes of it.
    :param release_channel_args:
    :return:
    """
    # Initializing the values for that contain the build data
    clientBuildDataJSON.build_num, clientBuildDataJSON.build_hash, clientBuildDataJSON.build_id = \
        getClientData(release_channel_args)

    release_channel_j = release_channel_args.lower()
    # Declares an object for JSON based on the params
    client_build_data = {f'{release_channel_j}_build_info': []}
    client_build_data[f'{release_channel_j}_build_info'].append({
        f'{release_channel_j}_build_number': clientBuildDataJSON.build_num,
        f'{release_channel_j}_build_hash': clientBuildDataJSON.build_hash,
        f'{release_channel_j}_build_id': clientBuildDataJSON.build_id
    })
    parsed_client_data = json.dumps(client_build_data)
    return parsed_client_data
