import asyncio
import time
import re
import twitchPlaysStreetfighterp2.inputController as ic

async def llHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def rlHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);
    
async def lmHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x65);

async def rmHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x65);

async def lhHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x66);

async def rhHadouken():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x66);

async def llShoryu():
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def rlShoryu():
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def lmShoryu():
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x65);
    
async def rmShoryu():
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x65);

async def lhShoryu():
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x66);

async def rhShoryu():
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x66);

async def llSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x61);
    time.sleep(0.02);
    ic.ReleaseKey(0x61);

async def rlSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x61);
    time.sleep(0.02);
    ic.ReleaseKey(0x61);
    
async def lmSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x62);
    time.sleep(0.02);
    ic.ReleaseKey(0x62);

async def rmSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x62);
    time.sleep(0.02);
    ic.ReleaseKey(0x62);

async def lhSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x63);
    time.sleep(0.02);
    ic.ReleaseKey(0x63);

async def rhSenp():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x63);
    time.sleep(0.02);
    ic.ReleaseKey(0x63);

async def lsuper():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def rsuper():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def lultra():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    ic.PressKey(0x64);
    ic.PressKey(0x65);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);
    ic.ReleaseKey(0x65);
    ic.ReleaseKey(0x66);

async def rultra():
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x4B);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    ic.PressKey(0x64);
    ic.PressKey(0x65);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);
    ic.ReleaseKey(0x65);
    ic.ReleaseKey(0x66);

async def jl():
    ic.PressKey(0x49);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x49);
    ic.ReleaseKey(0x4A);

async def jr():
    ic.PressKey(0x49);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x49);
    ic.ReleaseKey(0x4C);

async def dl():
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);
    time.sleep(0.02);
    ic.PressKey(0x4A);
    time.sleep(0.02);
    ic.ReleaseKey(0x4A);

async def dr():
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);
    time.sleep(0.02);
    ic.PressKey(0x4C);
    time.sleep(0.02);
    ic.ReleaseKey(0x4C);

async def throw():
    ic.PressKey(0x61);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x61);
    ic.ReleaseKey(0x64);

async def focus():
    ic.PressKey(0x62);
    ic.PressKey(0x65);
    time.sleep(1);
    ic.ReleaseKey(0x62);
    ic.ReleaseKey(0x65);

async def taunt():
    ic.PressKey(0x63);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x63);
    ic.ReleaseKey(0x66);

async def lfadc():
    ic.PressKey(0x62);
    ic.PressKey(0x65);
    time.sleep(0.11);
    await dl();
    ic.ReleaseKey(0x62);
    ic.ReleaseKey(0x65);

async def rfadc():
    ic.PressKey(0x62);
    ic.PressKey(0x65);
    time.sleep(0.11);
    await dr();
    ic.ReleaseKey(0x62);
    ic.ReleaseKey(0x65);

async def lk():
    ic.PressKey(0x61);
    time.sleep(0.02);
    ic.ReleaseKey(0x61);

async def mk():
    ic.PressKey(0x62);
    time.sleep(0.02);
    ic.ReleaseKey(0x62);

async def hk():
    ic.PressKey(0x63);
    time.sleep(0.02);
    ic.ReleaseKey(0x63);

async def lp():
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x64);

async def mp():
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x65);

async def hp():
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x66);

async def crlk():
    ic.PressKey(0x4B);
    ic.PressKey(0x61);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x61);

async def crmk():
    ic.PressKey(0x4B);
    ic.PressKey(0x62);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x62);

async def crhk():
    ic.PressKey(0x4B);
    ic.PressKey(0x63);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x63);

async def crlp():
    ic.PressKey(0x4B);
    ic.PressKey(0x64);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x64);

async def crmp():
    ic.PressKey(0x4B);
    ic.PressKey(0x65);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x65);

async def crhp():
    ic.PressKey(0x4B);
    ic.PressKey(0x66);
    time.sleep(0.02);
    ic.ReleaseKey(0x4B);
    ic.ReleaseKey(0x66);

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
        if builtString == "mk":
            await mk();
            builtString = "";
        if builtString == "hk":
            await hk();
            builtString = "";
        if builtString == "lp":
            await lp();
            builtString = "";
        if builtString == "mp":
            await mp();
            builtString = "";
        if builtString == "hp":
            await hp();
            builtString = "";
        if builtString == "crlk":
            await crlk();
            builtString = "";
        if builtString == "crmk":
            await crmk();
            builtString = "";
        if builtString == "crhk":
            await crhk();
            builtString = "";
        if builtString == "crlp":
            await crlp();
            builtString = "";
        if builtString == "crmp":
            await crmp();
            builtString = "";
        if builtString == "crhp":
            await crhp();
            builtString = "";
    return("Done using moves");