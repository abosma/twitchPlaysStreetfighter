import socket, string, time
import asyncio
import movesController as mc


class IRCController():
    def __init__(self):
        self.HOST = "irc.twitch.tv"
        self.PORT = 6667
        self.NICK = "aetbosma"
        self.PASS = 'oauth:m6dceh4p3e46lfhdeavz1x2rxknh95'
        self.s = socket.socket();
        self.paused = False;

    def send_message(self, message):
        self.s.send(bytes("PRIVMSG #" + self.NICK + " :" + message + "\r\n", "UTF-8"))
   
    async def bot(self):
        self.s.connect((self.HOST, self.PORT));
        self.s.send(bytes("PASS " + self.PASS + "\r\n", "UTF-8"))
        self.s.send(bytes("NICK " + self.NICK + "\r\n", "UTF-8"))
        self.s.send(bytes("JOIN #" + self.NICK + " \r\n", "UTF-8"))
        while True:
            line = str(self.s.recv(1024))
            if "End of /NAMES list" in line:
                break

        while True:
            for line in str(self.s.recv(1024)).split('\\r\\n'):
                parts = line.split(':')
                if len(parts) < 3:
                    continue

                if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                    message = parts[2][:len(parts[2])]

                usernamesplit = parts[1].split("!")
                username = usernamesplit[0]

                print(username + ": " + message)
                
                try:
                    if not self.paused and username != "aetbosma":
                        self.send_message(await mc.stringReader(parts[2]));
                    elif not self.paused and username == "aetbosma":
                        if message == "pause":
                            self.paused = True;
                        else:
                            self.send_message(await mc.stringReader(parts[2]));
                    elif self.paused and username != "aetbosma":
                        self.send_message("Bot is currently paused");
                    elif self.paused and username == "aetbosma":
                        if message == "unpause":
                            self.paused = False;
                        else:
                            self.send_message(await mc.stringReader(parts[2]));
                except Exception as e:
                    pass

    def startBot(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.bot())