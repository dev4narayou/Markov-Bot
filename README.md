# What is it?
This is a simple implementation of a discord bot with some basic commands + a markov-chain-based text generation command. The command parses all messages in the channel the "?markov" command is called, and responds with a randomly generated sentence based on the messages, using a generated markov model.
# Setup
1. Go to https://discord.com/developers/applications and create an application & a bot with the necessary permissions.
2. Setup a directory with the final-markov-bot-demo.py file. (only need this one)
3. From the bot panel, get the access token and store it in an .env file in the project directory.
4. In the developer portal, from the OAuth2 tab, get an invite link by clicking the bot scope & the required permissions (administrator for testing). This should allow you to invite the bot to a server.
5. Without hosting, the final-markov-bot-demo.py will need to be running for the bot to work.
6. While the py file is running, in the discord server with the bot, message ?markov or other commands listed in the file with the ?prefix to use the bot. 
# Note
final-markov-bot-demo.py is the required file
