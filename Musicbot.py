print("Initialising...")
import discord
from discord.ext import commands
import youtube_dl
print("Logging into the discord server")

#client = discord.Client()

bot = commands.Bot(command_prefix='/')

VChannel = None
VState = None



@bot.event
async def on_ready():
    print('the music bot is ready')

@bot.command(pass_context = True)
async def join(ctx):
    for vc in ctx.guild.voice_channels:
        for member in vc.members:
            if member == ctx.message.author:
                vs = await vc.connect();
                global VChannel
                VChannel = vc
                global VState
                VState = vs
                print(VChannel)


@bot.command(pass_context=True)
async def leave(ctx):
    if VChannel is not None:
        await VChannel.disconnect()
    else:
        for vc in ctx.guild.voice_channels:
            for member in vc.members:
                if member == client.user:
                    await vc.disconnect();


@bot.command(pass_context=True)
async def play(ctx, *url):
    if not VState or not VChannel:
        print("ERROR: Not connected to a voice channel")
        return

    #opts = {}
    song_info = youtube_dl.YoutubeDL({}).extract_info("ytsearch:" + ' '.join(url), download=False)
    VState.play(discord.FFmpegPCMAudio(song_info['entries'][0]['formats'][0]['url']))

    await ctx.channel.send("Playing: **{}**".format(song_info['entries'][0]['title']))







bot.run('NTAwNjY1MTQ0NjI4NDc3OTU0.DqOKCw.z9vo0mYbnAw1BE69MI8Xd_Hsnd4')
