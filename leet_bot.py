import discord
import scrape_leetcode

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=['997873023589818569'])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=['997873023589818569'])
async def leet(ctx):
    channel = bot.get_channel(997873023589818572)
    problem = scrape_leetcode.get_latest_problem_title()
    thread = await channel.create_thread(name=problem[1], message=None, auto_archive_duration=60, type=discord.ChannelType.public_thread, reason=None)
    await thread.send(problem[0])
    await ctx.respond("Created Thread!")

token_file = open("pw.txt", "r")
token = token_file.read()
token_file.close()
bot.run(token)