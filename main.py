import discord
from discord import app_commands
from discord.ext import commands

# 1. Replace with your actual numeric Discord User ID
MY_USER_ID =1277467996805271572

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
  # Sync slash commands globally across all installation contexts
  await bot.tree.sync()
  print(f"Logged in as {bot.user} - Personal User App Ready!")


# Helper function to enforce owner-only access
def is_owner(interaction: discord.Interaction) -> bool:
  return interaction.user.id == MY_USER_ID


# --- COMMAND 1: REPEAT (MAX 10 MESSAGES) ---
@bot.tree.command(
    name="repeat",
    description="Repeat a message up to 10 times (Owner Only)",
)
@app_commands.describe(
    times="How many times to repeat (Max 10)", message="The text to send"
)
async def repeat(
    interaction: discord.Interaction, times: int, message: str
):
  if not is_owner(interaction):
    await interaction.response.send_message(
        "❌ Access denied. Only the app owner can use this.", ephemeral=True
    )
    return

  # Force maximum limit to 10
  actual_times = min(max(1, times), 10)

  # Private confirmation so only you see the trigger message
  await interaction.response.send_message(
      f"Sending {actual_times} messages...", ephemeral=True
  )

  for _ in range(actual_times):
    await interaction.channel.send(message)


# --- COMMAND 2: PING USER ---
@bot.tree.command(
    name="pinguser", description="Mention a specific user (Owner Only)"
)
@app_commands.describe(
    user="The user to ping", message="Optional message to include"
)
async def ping_user(
    interaction: discord.Interaction,
    user: discord.User,
    message: str = "Pinging you!",
):
  if not is_owner(interaction):
    await interaction.response.send_message(
        "❌ Access denied.", ephemeral=True
    )
    return

  # Respond in channel with user mention
  await interaction.response.send_message(
      f"{user.mention} {message}",
      allowed_mentions=discord.AllowedMentions(users=True),
  )


# --- COMMAND 3: PING ROLE ---
@bot.tree.command(
    name="pingrole", description="Mention a specific role (Owner Only)"
)
@app_commands.describe(
    role="The role to ping", message="Optional message to include"
)
async def ping_role(
    interaction: discord.Interaction,
    role: discord.Role,
    message: str = "Attention!",
):
  if not is_owner(interaction):
    await interaction.response.send_message(
        "❌ Access denied.", ephemeral=True
    )
    return

  await interaction.response.send_message(
      f"{role.mention} {message}",
      allowed_mentions=discord.AllowedMentions(roles=True),
  )


# --- COMMAND 4: PING EVERYONE ---
@bot.tree.command(
    name="pingeveryone",
    description="Mention @everyone in the channel (Owner Only)",
)
@app_commands.describe(message="Optional message to include")
async def ping_everyone(
    interaction: discord.Interaction, message: str = "Attention everyone!"
):
  if not is_owner(interaction):
    await interaction.response.send_message(
        "❌ Access denied.", ephemeral=True
    )
    return

  # Explicitly allow pinging everyone/here
  await interaction.response.send_message(
      f"@everyone {message}",
      allowed_mentions=discord.AllowedMentions(everyone=True),
  )


# Run bot with your Bot Token (from Discord Developer Portal)bot.run(os.environ.get()
bot.run(os.environ.get(MTU1OTU4OTEzNDQ0MjcwMDg2MA.G2aB3h.EVhJjZx7Mt5KLL7N2hoSDgxTvjxhTQf_7xLlr4"))
