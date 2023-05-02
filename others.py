import discord
import string

def upper(x):
    x = string.capwords(x, sep=None)
    return x

def lower(x):
    x = x.casefold()
    return x

def longembed():
    embed = discord.Embed(
        title = "Master Orb Finder",
        description = "String too long, try again.",
        colour = discord.Colour.dark_orange()
    )
    embed.add_field(name="Follow the command: $jewel [English/Japanese/Romaji Name]",value=" ",inline=False)
    return embed

def invalidembed():
    embed = discord.Embed(
        title = "Master Orb Finder",
        description = "This value is not valid, try again.",
        colour = discord.Colour.dark_orange()
    )
    embed.add_field(name="Follow the command: $jewel [English/Japanese/Romaji Name]",value=" ",inline=False)
    return embed

def emptyembed(buscar):
    embed = discord.Embed(
        title = "Master Orb Finder",
        description = 'There are no jewels that contain "'+buscar+'".',
        colour = discord.Colour.dark_orange()
    )
    embed.add_field(name="Follow the command: $jewel [English/Japanese/Romaji Name]",value=" ",inline=False)
    return embed


def listedembed(list):
    embed = discord.Embed(
        title = "Master Orb Finder",
        description = "",
        colour = discord.Colour.dark_grey()
    )
    #message = "Maybe you're looking for:\n"
    message = ""
    count=0
    for index, row in list.iterrows():
        message += "["+row['Element']+"] "+row['English']+"\n"+row["Japanese"]+" ("+row["Romanized"]+")\n\n"
        count = count+1
        if(count > 9):
            message += "(.....)"
            count = 0
            break
    embed.add_field(name="Maybe you're looking for:", value=message, inline=True)
    embed.add_field(name="Follow the command: $jewel [English/Japanese/Romaji Name]",value="",inline=False)
    return embed

def correctembed(find):
    vct = find['Vocation'].item()
    wpn = find['Weapon'].item()
    el = find['Element'].item()
    jp = find['Japanese'].item()
    rm = find['Romanized'].item()
    eng = find['English'].item()
    desc = find['Description'].item()
    monsters = (find['Monster Drop / Location'].item()).split(", ")
    elColour = None
    if el == "Fire":
        elColour = discord.Colour.red()
    elif el == "Water":
        elColour = discord.Colour.blue()
    elif el == "Wind":
        elColour = discord.Colour.green()
    elif el == "Light":
        elColour = discord.Colour.yellow()
    elif el == "Dark":
        elColour = discord.Colour.dark_purple()

    embed = discord.Embed(
        title = eng,
        description = "Also known as: \n"+jp+" ("+rm+")",
        colour = elColour
    )
    embed.set_footer(text="Information extracted from Ethene Wiki, bot made by Ark")
    embed.add_field(name="Description", value=desc, inline=False)
    message = ''
    embed.add_field(name="Element", value=el+" Orb", inline=True)
    
    if(vct != "null" and vct != "any"):
        vctname = upper(vct[:-6])
        vctshrt = vct[-5:].upper()
        embed.add_field(name="Vocation", value=vctname+" "+vctshrt, inline=True)
        #message+= vct+ " exclusive.\n"
    if(vct == "any"):
        vctname = upper(vct)
        #print(vctname)
        embed.add_field(name="Vocation", value=vctname, inline=True)
    if(wpn != "Null"):
        embed.add_field(name="Weapon", value=wpn, inline=True)
        #message+= wpn+ " exclusive.\n"
    #message+= "["+el+" Orb]:\n"+eng+" ("+rm+")\n"+jp
    #message+= "\nDescription: "+desc
    
    if("Map" in monsters[0]):
        embed.add_field(name="Found in", value="* "+(monsters[0])[5:], inline=False)
        #message+= "Found in:"
        #message+= "* "+(monsters[0])[5:]
    else:
        #message+= "\nDropped by:"
        message =''
        for j in monsters:
            message+= "\n* "+j
        embed.add_field(name="Dropped by", value=message, inline=False)
    #return message;
    embed.add_field(name="Complete List of Orbs: https://ethene.wiki/wiki/Master_Orb"+"#"+el,value=" ",inline=False)
    return embed;