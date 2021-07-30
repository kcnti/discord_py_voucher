import discord
import requests
import json
import datetime
from discord.ext import commands


bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.commands()
async def topup(ctx, voucher):
    
    phone_num = ""

    ################

    voucher_hash = voucher.split('=')[-1]
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "mobile": phone_num,
        "voucher_hash": voucher_hash 
    }
    url = "https://gift.truemoney.com/campaign/vouchers" + voucher_hash + "/redeem"

    #################

    try:
        r = requests.post(url, data=json.dumps(data), headers=header)
        _json = r.json()
        if r.status_code == 200:
            get_bal = int(float(_json['data']['my_ticket']['amount_baht']))
            embed = discord.Embed(description=f"\nได้รับ {get_bal} บาท")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='By Kanti#8338', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="มีบางอย่างผิดปกติกับ api หรือลิ้งค์ของขวัญ")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='By Kanti#8338', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    except:
        embed = discord.Embed(description="มีบางอย่างผิดปกติกับ api หรือลิ้งค์ของขวัญ")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='By Kanti#8338', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


bot.run("token")

