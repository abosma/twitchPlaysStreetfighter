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
    waitTime = 0;
    builtString = "";
    for chr in moveString:
        builtString = builtString + chr;
        match = re.search('^slp[0-9]{2}$', builtString);
        if match:
            timeToWait = int(''.join(list(filter(str.isdigit, match.group(0)))));
            waitTime = (timeToWait / 1000);
            builtString = "";
        if builtString == "llhdk":
            await llHadouken();
            builtString = "";
        if builtString == "rlhdk":
            await rlHadouken();
            builtString = "";
        if builtString == "lmhdk":
            await lmHadouken();
            builtString = "";
        if builtString == "rmhdk":
            await rmHadouken();
            builtString = "";
        if builtString == "lhhdk":
            await lhHadouken();
            builtString = "";
        if builtString == "rhhdk":
            await rhHadouken();
            builtString = "";
        if builtString == "llshy":
            await llShoryu();
            builtString = "";
        if builtString == "rlshy":
            await rlShoryu();
            builtString = "";
        if builtString == "lmshy":
            await lmShoryu();
            builtString = "";
        if builtString == "rmshy":
            await rmShoryu();
            builtString = "";
        if builtString == "lhshy":
            await lhShoryu();
            builtString = "";
        if builtString == "rhshy":
            await rhShoryu();
            builtString = "";
        if builtString == "llsen":
            await llSenp();
            builtString = "";
        if builtString == "rlsen":
            await rlSenp();
            builtString = "";
        if builtString == "lmsen":
            await lmSenp();
            builtString = "";
        if builtString == "rmsen":
            await rmSenp();
            builtString = "";
        if builtString == "lhsen":
            await lhSenp();
            builtString = "";
        if builtString == "rhsen":
            await rhSenp();
            builtString = "";
        if builtString == "lsuper":
            await lsuper();
            builtString = "";
        if builtString == "lultra":
            await lultra();
            builtString = "";
        if builtString == "rsuper":
            await rsuper();
            builtString = "";
        if builtString == "rultra":
            await rultra();
            builtString = "";
        if builtString == "jl":
            await jl();
            builtString = "";
        if builtString == "jr":
            await jr();
            builtString = "";
        if builtString == "dl":
            await dl();
            builtString = "";
        if builtString == "dr":
            await dr();
            builtString = "";
        if builtString == "throw":
            await throw();
            builtString = "";
        if builtString == "focus":
            await focus();
            builtString = "";
        if builtString == "taunt":
            await taunt();
            builtString = "";
        if builtString == "lfadc":
            await lfadc();
            builtString = "";
        if builtString == "rfadc":
            await rfadc();
            builtString = "";
        if builtString == "help":
            return("Commandlist here: http://pastebin.com/TH3PN3wK");
        if builtString == "lk":
            await lk();
            builtString = "";
        time.sleep(waitTime);
    return("Done using moves");