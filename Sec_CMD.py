import discord
from discord.ext import commands
from asyncio import *
import random
from discord import colour
import json
from discord import embeds
from discord.ext import tasks
from discord.ext.commands.errors import DisabledCommand



colors = [0x01b8a1, 0xaa0e6c, 0x390174, 0xf6fa02, 0x5df306, 0x2206f3, 0xfffdfd, 0xff0a0e, 0x850000, 0xe76868, 0x4eca75, 0xb38203, 0xc44400, 0x000000, 0x0517dd, 0x6c6f92, 0x144900, 0xffffff, 0x020246, 0xe209b7, 0x0976e2, 0x3de209, 0xe29209, 0x08a247]


class CONFIG:
    TOKEN = "Paste Token"
    PREFIX = "$"


client = commands.Bot(command_prefix=CONFIG.PREFIX)
client.remove_command("help")


@client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="PREFIX = ."),status=discord.Status.idle)
      print("Oltra Bot Run Shod ! :)")

#  run shodan Bot



@client.command(aliases=["LOCK", "Lock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel):
    the_channel = client.get_channel(channel.id)
    await the_channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(title="Channel Lock Shod! 🔒", color=0x8b0003)
    await channel.send(embed=embed)

#   Lock channel

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="Shoma Gabeliyat estefade az dastor ($lock) ra nadarid ⛔❌",
        )
        await ctx.reply(embed=embed)


# Dastresi be $lock


@client.command(aliases=["unLOCK", "unLock", "UNLOCK", "Unlock", "UNlock", "UNLock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel):
    the_channel = client.get_channel(channel.id)
    await the_channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = discord.Embed(title="Channel UnLock Shod! 🔓", color=0x108602)
    await channel.send(embed=embed)

#   Unlock kardan



@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            color=0xb60000
        )
        embed.set_author(
            name="Shoma Gabeliyat estefade az dastor ($unlock) ra nadarid ⛔❌",
        )
        await ctx.reply(embed=embed)


# Dastresi be $unlock



@client.event
async def on_guild_join(g):
    success = False
    i = 0
    while not success:
        try:
            embed = discord.Embed(title="Salam man ye Bot Security Hastam va vazife man Hefazat az Server, Member ha va Channel hast. ", color=0x108602, description="**Baraye didan Command ha mitavanid az ( `.help` ) Estefade Konid!**")
            embed.set_footer(text="Server Poshtebani 𝑶𝒍𝒕𝒓𝒂 𝑺𝒆𝒄𝒖𝒓𝒊𝒕𝒚 : https://discord.gg/S7s6emz4JG")
            await g.channels[i].send(embed=embed)
        except (discord.Forbidden, AttributeError):
            i += 1
        except IndexError:
            pass
        else:
            success = True

   
    
    payload = {
        'server_count': len(client.guilds)
    }


# vaghti join server shod payam dahad!



@client.command(aliases=["user", "User"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.choice(colors), timestamp=ctx.message.created_at,
                          title=f"User Info  {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Darkhast Tavasot: {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p "))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p "))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Top Role:", value=member.top_role.mention)

    await ctx.reply(embed=embed)


# user info


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(cdv, member: discord.Member):
    mutedRole = discord.utils.get(cdv.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f" shoma unmute shodid! **( {member.name} )**", color=0x036103)
    await cdv.send(embed=embed)
    embed = discord.Embed(title=f" shoma unmute shodid az server: **( {cdv.guild.name} )**", color=0x036103)
    await member.send(embed=embed)

#unmute server


@client.command()
@commands.has_permissions(administrator=True)
async def mute(cdv, member: discord.Member, *, reason=None):
    guild = cdv.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False, connect=False)
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(title=f" Shoma mute shodid (** {member.name} **) Be dalil : ( ||**{reason}**|| ) 💀", color=0x8d0303)
    await cdv.send(embed=embed)
    embed = discord.Embed(title=f" Shoma az Server : ( **{guild.name}** ) mute shodid , Be dalil : ( **{reason}** ) 💀", color=0x8d0303)
    await member.send(embed=embed)

#mute server


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server : ( ||**{ctx.guild.name}**|| ) Be Dalil ( **{reason}** ) Kick Shodid! ", color=0x5f04a3)
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar ( {member.name} ) az Server Be dalil : ( ||{reason}|| ) Kick shod!", color=0x5f04a3)
    await ctx.send(embed=embed)


#kick server


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server  : ( **||{ctx.guild.name}||** ) Ban Shodid , Be dalil : ( **{reason}** ) 💀", color=0xf10004)
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar  : ( **{member.name}** ) az Server Ban Shod , Be dalil : ( **||{reason}||** ) 💀", color=0xf10004)
    await ctx.send(embed=embed)



#ban server



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
     embed = discord.Embed(
       title="Command Not Found!",
       colour=random.choice(colors),
       description="دستوری با این موزون یافت :confused:"
      )
     embed.set_footer(text="برای دیدن کامند های بیشتر از help. استفاده کنید")
     await ctx.reply(embed=embed)


# command not found


@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx,member: discord.Member,*,result=None):
    authorm = ctx.message.author
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description=f"Warn Be ( **{member}** ) Be Dalil ( **{result}** ) Dadeshod! :no_entry_sign:"
      )
    await ctx.reply(embed=embed)
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description = f"Shoma Tavasot ( **{authorm}** ) Be Dalil ( **{result}** ) Warn Gereftid! :no_entry_sign:"
      )
    await member.send(embed=embed)

#warn dadan




@client.command(aliases=["clean", "delet", "del"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count="1"):
     count = int(count)
     await ctx.channel.purge(limit=count+1)
     await ctx.send(">>> "+str(count)+"> Payam Pak shod :white_check_mark:")

# pak kardn payam ha = $clear







client.run(CONFIG.TOKEN)
