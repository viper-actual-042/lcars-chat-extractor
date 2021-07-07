# lcars-chat-extractor
# author: viper042

#### Purpose
- To iterate through a directory structure of exported LCARS Discord messages, identify and parse json files,
  and extract command - response pairs

#### Current State
- Given a path in command-line args, recursively iterates and identifies json data files
- Loads the JSON files into python objects
- Identifies LCARS system commands and responses
- Ignores duplicate commands
- Prints out to stdout

#### Future Revisions
- Export JSON objects
- Write to data schema for future querying
- Handle unicode non-breaking spaces `\xa0`
- Create docker-compose setup

#### Pre-requisites
- Python 3.5+

#### Setup
1. Create a python virtualenv, ensure version is 3.5+
    - `virtualenv -p $(which python3) venv`
2. Activate the python venv
    - `source venv/bin/activate`
3. rename some files to get the unicode characters out
    - `rename 's/Official LCARS 2.0 - ──── access terminals ──── - 💻-lcars-terminal-/lcars-terminal-/' *.json`
    - `rename 's/ \(after 2021-07-05\)//' *.json`
4. Run the extractor
    - example usage: `python ./src/lcars-chat-extractor.py <path-to-data-files>`
    - `python ./src/lcars-chat-extractor.py ./raw-data/`
5. Deactivate the python venv
    - `deactivate`