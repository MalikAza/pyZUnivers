![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/MalikAza/pyZUnivers/main/pyproject.toml&style=for-the-badge&logo=python) ![GitHub last commit](https://img.shields.io/github/last-commit/MalikAza/pyZUnivers/main?style=for-the-badge)

# pyZUnivers
ZUnivers API python wrapper

[Documentation](https://malikaza.github.io/pyZUnivers/)
## Installation
**Disclaimers:**
- It is recommended to install the module (with your project using it) in a [virtual environment](https://docs.python.org/3/library/venv.html).
- `pyZUnivers` module is not available on PyPi yet, so you can use the `installation` python script to add required dependencies and add the module to your python `site-packages` folder, making it globally available on your machine.
```bash
python installation.py
```
or
```bash
python3 installation.py
```

## Example
```python
import discord
from discord.ext import commands
import pyZUnivers as ZU

class Zunivers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="zuchecker", help="Permets de faire un récap' de qui à besoin de faire quoi.")
    async def zuchecker(self, ctx: commands.Context):
        server = self.bot.get_guild(<your_guild_id>)
        zu_role = server.get_role(<specific_role_id_in_your_guild>)
        journa, bonus, nowel = list(), list(), list()
        msg = await ctx.send("Je vérifie qui doit faire quelque chose...")
        try:
            for i in zu_role.members:
                konar_profile = ZU.User.get_checker(i.name)
                if not konar_profile["journa"]: journa.append(i.name)
                if not konar_profile["bonus"]: bonus.append(i.name)
                if not konar_profile["advent"] and konar_profile["advent"] is not None: nowel.append(i.name)

            embed = discord.Embed(color=discord.Colour(value=0x19BC14), description=f"<#{ZU.utils.JOURNA_BONUS_TICKET_CHANNEL_ID}>")
            embed.set_author(name="ZUnivers - Checker")
            if len(journa) != 0: embed.add_field(name="📅 Journa", value="".join([f"- {x}\n" for x in journa]))
            if len(bonus) != 0: embed.add_field(name="🎁 Bonus", value="".join([f"- {x}\n" for x in bonus]))
            if len(nowel) != 0: embed.add_field(name="🎄 Advent", value="".join([f"- {x}\n" for x in nowel]))
            if len(journa) == 0 and len(bonus) == 0 and len(nowel) == 0: embed.description = "Personne a besoin de faire quoi que ce soit."

            await msg.edit(embed=embed, content="")
        except ZU.ZUniversAPIError as e:
            await msg.edit("`Erreur dans la command 'zu checker'."
                        f" {e.message}`\n`Endpoint: {e.url}`")

async def setup(bot):
    await bot.add_cog(Zunivers(bot))
```