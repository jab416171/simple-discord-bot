## Setup
1. First you must have a bot instance to run this script on. Follow Discord's tutorial [here](https://discord.onl/2019/03/21/how-to-set-up-a-bot-application/) on how to set one up. Be sure to invite it to a server to use it.

2. Run `pip3 install -r requirements.txt` in the repository's root directory to get the necessary libraries.

    * Note that python-Levenshtein requires your system to have a C++ compiler (Visual Studio C++ compiler for Windows or g++ for Linux). This library may be replaced in the future to eliminate this requirement.

3. Copy entrypoint.py.example to entrypoint.py and put in your bot token.

4. You can simply run the Dockerfile and your bot will start up, with voice support

5. In the discord console, click on OAuth2 then URL Generator, and under scope select "Bot" and if you want to add slash commands, "applications.commands", and whatever permissions you believe your bot will need.