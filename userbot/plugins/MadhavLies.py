"""
Pulls Up A Random Lie of Madhav Seth's Realmeme Series...
Syntax: .madhav
    orginal author : @TechyNewbie"""

from random import choice

@client.on(events(pattern="madhav"))
async def lier(event):
    if event.fwd_from:
        return
    lies = [
        "**“We Will Release A Flash Tool in Q2 2019” - Madhav Seth**",
        "**“No ADs in UI” - Madhav Seth**",
        "**“If realme makes its Own OS, then all our devices will be running on it” - Madhav Seth**",
        "**“We will try to add as many Clone Apps as possible” - Madhav Seth**",
        "**“We are the most Customer Centered brand” - Madhav Seth**",
        "**“We sell phones, not ADs” - Madhav Seth**",
        "**“We will never place ADs in OS” - Madhav Seth**",
        "**“realme is the only brand which provides regular updates” - Madhav Seth**",
        "**“We will add Internal Audio Recording in all devices by November (2019)” - Madhav Seth**",
        "**“We work on feedback taken from users” - Madhav Seth**",
        "**“Redmi's 48MP Camera (RN7pro) is just a number game” - Madhav Seth\n\n“We are launching the world's first 64MP Camera Phone”**"
    ]
    lie = choice(lies)
    await event.edit(lie)


HELPER.update({"MadhavLies": "\
**Available commands in MadhavLies module:**\
\n`.madhav`\
"})
