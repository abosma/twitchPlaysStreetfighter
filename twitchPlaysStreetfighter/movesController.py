import asyncio
import time
import re
import inputController as ic

async def llHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def rlHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);
    
async def lmHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x53);
    time.sleep(0.02);
    ic.ReleaseKey(0x53);

async def rmHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x53);
    time.sleep(0.02);
    ic.ReleaseKey(0x53);

async def lhHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x44);

async def rhHadouken():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x44);

async def llShoryu():
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def rlShoryu():
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def lmShoryu():
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x53);
    time.sleep(0.02);
    ic.ReleaseKey(0x53);
    
async def rmShoryu():
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x53);
    time.sleep(0.02);
    ic.ReleaseKey(0x53);

async def lhShoryu():
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x44);

async def rhShoryu():
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x44);

async def llSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x5A);
    time.sleep(0.02);
    ic.ReleaseKey(0x5A);

async def rlSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x5A);
    time.sleep(0.02);
    ic.ReleaseKey(0x5A);
    
async def lmSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x58);
    time.sleep(0.02);
    ic.ReleaseKey(0x58);

async def rmSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x58);
    time.sleep(0.02);
    ic.ReleaseKey(0x58);

async def lhSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x43);
    time.sleep(0.02);
    ic.ReleaseKey(0x43);

async def rhSenp():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x43);
    time.sleep(0.02);
    ic.ReleaseKey(0x43);

async def lsuper():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def rsuper():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x41);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def lultra():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    ic.PressKey(0x41);
    ic.PressKey(0x53);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);
    ic.ReleaseKey(0x53);
    ic.ReleaseKey(0x44);

async def rultra():
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x28);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x28);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);
    ic.PressKey(0x41);
    ic.PressKey(0x53);
    ic.PressKey(0x44);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);
    ic.ReleaseKey(0x53);
    ic.ReleaseKey(0x44);

async def jl():
    ic.PressKey(0x26);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x26);
    ic.ReleaseKey(0x25);

async def jr():
    ic.PressKey(0x26);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x26);
    ic.ReleaseKey(0x27);

async def dl():
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);
    time.sleep(0.02);
    ic.PressKey(0x25);
    time.sleep(0.02);
    ic.ReleaseKey(0x25);

async def dr():
    ic.PressKey(0x27);
    time.sleep(0.015);
    ic.ReleaseKey(0x27);
    time.sleep(0.02);
    ic.PressKey(0x27);
    time.sleep(0.02);
    ic.ReleaseKey(0x27);

async def throw():
    ic.PressKey(0x41);
    ic.PressKey(0x5A);
    time.sleep(0.02);
    ic.ReleaseKey(0x41);
    ic.ReleaseKey(0x5A);

async def focus():
    ic.PressKey(0x53);
    ic.PressKey(0x58);
    time.sleep(1);
    ic.ReleaseKey(0x53);
    ic.ReleaseKey(0x58);

async def taunt():
    ic.PressKey(0x44);
    ic.PressKey(0x43);
    time.sleep(0.02);
    ic.ReleaseKey(0x44);
    ic.ReleaseKey(0x43);

async def lfadc():
    ic.PressKey(0x53);
    ic.PressKey(0x58);
    time.sleep(0.11);
    await dl();
    ic.ReleaseKey(0x53);
    ic.ReleaseKey(0x58);

async def rfadc():
    ic.PressKey(0x53);
    ic.PressKey(0x58);
    time.sleep(0.11);
    await dr();
    ic.ReleaseKey(0x53);
    ic.ReleaseKey(0x58);

async def lk():
    ic.PressKey(0x41)
    time.sleep(0.02);
    ic.ReleaseKey(0x41);

async def stringReader(moveString):
    moveList = ["llhdk", "rlhdk",
                "lmhdk", "rmhdk",
                "lhhdk", "rhhdk",
                "llshy", "rlshy",
                "lmshy", "rmshy",
                "lhshy", "rhshy",
                "llsen", "rlsen",
                "lmsen", "rmsen",
                "lhsen", "rhsen",
                "lsuper", "rsuper",
                "lultra", "rultra",
                "jl", "jr", "dl", "dr",
                "throw", "taunt",
                "focus", "lfadc",
                "rfadc", "lk",
                "mk", "hk", "lp",
                "mp", "hp", "slp"]
    waitTime = 0;
    match = re.search('slp[\d]{0,9}', moveString);

    for move in moveList:
        if move in moveString:
            if match:
                timeToWait = int(''.join(list(filter(str.isdigit, match.group(0)))));
                waitTime = (timeToWait / 1000);
            if move == "llhdk":
                await llHadouken();
            if move == "rlhdk":
                await rlHadouken();
            if move == "lmhdk":
                await lmHadouken();
            if move == "rmhdk":
                await rmHadouken();
            if move == "lhhdk":
                await lhHadouken();
            if move == "rhhdk":
                await rhHadouken();
            if move == "llshy":
                await llShoryu();
            if move == "rlshy":
                await rlShoryu();
            if move == "lmshy":
                await lmShoryu();
            if move == "rmshy":
                await rmShoryu();
            if move == "lhshy":
                await lhShoryu();
            if move == "rhshy":
                await rhShoryu();
            if move == "llsen":
                await llSenp();
            if move == "rlsen":
                await rlSenp();
            if move == "lmsen":
                await lmSenp();
            if move == "rmsen":
                await rmSenp();
            if move == "lhsen":
                await lhSenp();
            if move == "rhsen":
                await rhSenp();
            if move == "lsuper":
                await lsuper();
            if move == "lultra":
                await lultra();
            if move == "rsuper":
                await rsuper();
            if move == "rultra":
                await rultra();
            if move == "jl":
                await jl();
            if move == "jr":
                await jr();
            if move == "dl":
                await dl();
            if move == "dr":
                await dr();
            if move == "throw":
                await throw();
            if move == "focus":
                await focus();
            if move == "taunt":
                await taunt();
            if move == "lfadc":
                await lfadc();
            if move == "rfadc":
                await rfadc();
            if move == "help":
                return("Commandlist here: http://pastebin.com/TH3PN3wK");
            if move == "lk":
                await lk();
            time.sleep(waitTime);
    return("Done using moves");