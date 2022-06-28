# StreamBot.py

StreamBot.py is a very simple discord bot, that notifies members in a specified channel when someone with a specific role is streaming on Twitch or YouTube.

**The streamers on your server must have their streaming platform accounts linked to their Discord accounts!**

## Setting up StreamBot.py

1. Install Python [(Click here)](https://wiki.python.org/moin/BeginnersGuide/Download).

2. Install Discord.py [(Click here)](https://discordpy.readthedocs.io/en/latest/intro.html).

3. Download [bot.py](https://github.com/LxonWWW/StreamBot/blob/master/bot.py).

4. Create a discord application [here](https://discord.com/developers/applications).

5. On the application dashboard create a bot.

6. Open "bot.py" with a suitable editor or IDE, I'm personally using [Atom](https://atom.io/).

7. Then go to the last line of the file and replace 'ENTER YOU TOKE HERE' with the bot's token from Discord's application dashboard.

8. Enable developer mode in Discord's settings.

9. Create a streaming role and copy the id of your streaming role by right clicking.

10. Insert the streaming role id at line 10. Replace 'YOUR_STREAMER_ROLE_ID' with your streaming role id.

11. Copy the id of your streaming announcements channel by right clicking.

12. Insert the streaming announcement channel id at line 11. Replace 'YOUR_STREAM_ANNOUNCEMENT_CHANNEL_ID' with your streaming announcements channel id.

13. Now save the file an you're good to go.

## Starting your StreamBot

The bot can be started with the following command, please replace the leading slashes with the path to your "bot.py" file.
`python3 path/to/your/directory/bot.py`
