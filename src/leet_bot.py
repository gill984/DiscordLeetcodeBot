import discord
import scrape_leetcode

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=['215246893758808064', '997873023589818569'])
async def leet(ctx):
    channel = ctx.channel
    threads = channel.threads

    problem = scrape_leetcode.get_latest_problem_title()
    if (problem is None):
        await ctx.respond("Couldn't create thread, sorry!")
        return
    
    for thread in threads:
        if thread.name == problem[1] and not thread.archived:
            await ctx.respond("A thread for this problem was already created here: " + thread.jump_url)
            return
    
    new_thread = await channel.create_thread(name=problem[1], message=None, auto_archive_duration=60, type=discord.ChannelType.public_thread, reason=None)
    await new_thread.send(problem[0])
    await ctx.respond("Created Thread!")

token_file = open("pw.txt", "r")
token = token_file.read()
token_file.close()
bot.run(token)