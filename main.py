from discord.ext import commands
import discord


class VCN(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("---ready---")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.create_role(name="vcn")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None:  # VC参加時
            if member.bot or len(after.channel.members) <= 1:  # 参加者がBot又はメンバーが1人以下の時は処理を中断
                return
            else:
                role = discord.utils.get(member.guild.roles, name="vcn")
                VCmembers = after.channel.members
                VCmembers.remove(member)
                for member in VCmembers:
                    if role in member.roles:
                        channel = await member.create_dm()
                        await channel.send(f"*{member.name}*さんがVCに参加しました")

    @commands.command()
    async def alert(self, ctx, _set):
        if set in ("on", "off"):
            role = discord.utils.get(ctx.guild.roles, name="vcn")
            if set == "on":
                await ctx.author.add_roles(role)
                await ctx.send("VC通知をオンにしました")
            elif set == "off":
                await ctx.author.remove_roles(role)
                await ctx.send("VC通知をオフにしました")
        else:
            await ctx.send("on:offのどちらかのみを入力してください")

    @commands.command()
    async def role(self, ctx):
        try:
            discord.utils.get(ctx.guild.roles, name="vcn").name
            await ctx.send("既に専用roleが存在します")
        except AttributeError:
            await ctx.guild.create_role(name="vcn")
            await ctx.send("専用roleを作成しました")


def setup(bot):
    bot.add_cog(VCN(bot))
