import gpt_2_simple as gpt2
import discord
from discord.ext import commands

sess = gpt2.start_tf_sess()
print('Downloading trained GPT-2 model...')
gpt2.load_gpt2(sess)
print('Download complete')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def generate(ctx, message):
    print("Generating text")
    generated_text = gpt2.generate(sess, prefix=message, length=400, return_as_list=True)[0]
    print("Text generation complete")

    # Organizing generated text
    word_list = generated_text.split()
    formatted_text = ""
    for word in word_list:
        formatted_text += word + " "
    formatted_text = formatted_text[:-1]

    await ctx.reply(formatted_text + '...')      


bot.run('YOUR PREFIX HERE')
