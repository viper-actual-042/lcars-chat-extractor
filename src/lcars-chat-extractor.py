import json
import os
import sys
import unicodedata

lcars_commands_parsed = []

def parse_discord_data(json_data):
    mcount = 0
    last_message = {}
    skip_command = 0
    global lcars_commands_parsed
    for message in json_data['messages']:
        
        # if author is lcars and the content = Commander, information as requested
        if message["author"]["id"] == '553906981652529181' and mcount > 0 and message["content"] == 'Commander, information as requested...':
            '''grab the immediately preceding message's content, which will be the command used, 
               if this isn't a continuation
            '''
            lcars_command = str(last_message["content"]).lower()
            if lcars_command != 'commander, information as requested...':
                if len(lcars_commands_parsed) > 0:
                    # check to see if we've previously processed this command
                    if lcars_command in lcars_commands_parsed:
                        skip_command = 1
                        print('********* DUPLICATE COMMAND FOUND ***********')
                        print(lcars_command)
                        continue
                    else:
                        skip_command = 0  
                        lcars_commands_parsed.append(lcars_command)
                else:
                    lcars_commands_parsed.append(lcars_command)

                print('=====================================================')
                print('LCARS_COMMAND: ' + lcars_command)
                print('-----------------------------------------------------')
                print('LCARS_RESPONSE:')
                for field in message["embeds"][0]["fields"]:
                    print(unicodedata.normalize("NFKD", field["value"]))
                print('=====================================================')

            else:
                #this is a continuation of previous response
                print('==========CONTINUED FROM ABOVE================')
                for field in message["embeds"][0]["fields"]:
                    print(field)

        last_message = message
        mcount = mcount + 1
        if mcount > 5:
            return 0

    return 0

def process_file(data_file):
    print('PARSE_FILE: ' + data_file)
    f = open(data_file,)
    data = json.load(f)
    parse_discord_data(data)
    f.close()

def walk_folders(path):
    os.scandir()
    for entry in os.scandir(path):
        if entry.is_dir():
            print("DIRECTORY FOUND:" + entry.path)
            walk_folders(entry.path)
        if (entry.path.endswith(".json")
                or entry.path.endswith(".json")) and entry.is_file():
            print("JSON file found:" + entry.path)
            process_file(entry.path)    

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # use the current working directory if none is specified in command-line args
        directory = os.getcwd()
    
    print("MAIN() Starting Directory: " + directory)
    walk_folders(directory)

    # print out the list of commands we parsed in this session
    lcars_commands_parsed.sort(key=lambda x: x.lower())
    print(lcars_commands_parsed)

if __name__ == '__main__':
    main()