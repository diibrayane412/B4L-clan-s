import discord
from discord.ext import commands

# Configuration dyal Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('Bot B4L is ready!')

@bot.command(name="clan")
async def create_clan(ctx, *, clan_name: str = None):
    # Check 1: Ghir l-Owner dyal l-Server li 3ndo l-7aq yst3mel l-command
    if ctx.author != ctx.guild.owner:
        await ctx.send("❌ Hada l-amr mkhassas ghir l-Owner dyal l-server!")
        return

    # Check 2: التأكد blli smiya dyal clan tktbat
    if not clan_name:
        await ctx.send("⚠️ A3ti smiya l clan! Mthal: `!clan Warriors`")
        return

    guild = ctx.guild

    # 1. Kriyat l-Role dyal l-Clan
    role_name = f"[B4L] {clan_name}"
    clan_role = await guild.create_role(
        name=role_name,
        color=discord.Color.gold(),
        reason=f"Clan created by owner: {clan_name}"
    )

    # 2. Ta7did l-Permissions (Privé ghir l-s7ab l-role)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        clan_role: discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True,
            connect=True,
            speak=True,
            stream=True
        ),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True)
    }

    # 3. Kriyat Category (Tap/Section) khassa b l-clan
    category = await guild.create_category(
        name=f"🏰 Clan | {clan_name}",
        overwrites=overwrites
    )

    # 4. Kriyat Text Channel Privé
    text_channel = await category.create_text_channel(
        name=f"💬-{clan_name.lower()}-chat"
    )

    # 5. Kriyat Voice Channel Privé
    voice_channel = await category.create_voice_channel(
        name=f"🔊 Clan {clan_name} Voice"
    )

    # M3loma l-Owner
    await ctx.send(f"✅ **تم إنشاء الكلان بنجاح!**\n"
                   f"• **Role:** {clan_role.mention}\n"
                   f"• **Category:** {category.name}\n"
                   f"• **Text Channel:** {text_channel.mention}\n"
                   f"• **Voice Channel:** {voice_channel.name}")

# Bddel Had l-Jumla b l-Token dyalak
bot.run('YOUR_DISCORD_BOT_TOKEN')

> ⚠️ Mūlaḥaḍa: Ma-t-nsash t-bddel 'YOUR_DISCORD_BOT_TOKEN' f ākhir saṭr b l-Token dyal l-bot dyālak li kopītī mn Discord Developer Portal!
> 
