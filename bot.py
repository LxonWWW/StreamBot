import discord
from discord.ext import tasks, commands
from discord import Member
import datetime

global streamer_role_id;
global streamer_channel_id;

#configuration
streamer_role_id = YOUR_STREAMER_ROLE_ID;
streamer_channel_id = YOUR_STREAM_ANNOUNCEMENT_CHANNEL;

bot = commands.Bot(command_prefix='§')

async def on_ready():
    print('> Bot is ready')

    #Set bots activity
    bot_activity = discord.Game('Twitch');
    await bot.change_presence(status=discord.Status.online, activity=bot_activity)

async def on_member_update(member_before, member_after):
    global streamer_role_id;
    global streamer_channel_id;

    #print(member_after.activities);

    has_streamer_role = 0;

    for role in member_after.roles:
        if(role.id == streamer_role_id):
            has_streamer_role = 1;

    stream_channel = bot.get_channel(streamer_channel_id);

    has_streamed_before = 0;

    if(has_streamer_role == 1):
        for activity_last in member_before.activities:
            if(activity_last.type == discord.ActivityType.streaming):
                has_streamed_before = 1;

    if(has_streamer_role == 1):
        for activity in member_after.activities:
            if(activity.type == discord.ActivityType.streaming and has_streamed_before == 0):
                await stream_channel.send('Hi @everyone, ' + str(member_after) + ' streamt jetzt ** ' + str(activity.name) + ' ** live auf Twitch!\n*Klick hier:* ' + str(activity.url));
                print(datetime.datetime.now().strftime('[%d.%m.%Y %H:%M:%S]') + ' Stream announced: ' + str(member_after) + ' streaming ' + str(activity.name) + ' on ' + str(activity.url));

bot.add_listener(on_member_update);
bot.add_listener(on_ready);

bot.run('ENTER YOU TOKE HERE')
