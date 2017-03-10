import twitchPlaysStreetfighter.twitchPlaysStreetfighter as tpps
import twitchPlaysStreetfighterp2.twitchPlaysStreetfighterp2 as tpps2
import threading

a = threading.Thread(target=tpps.start)
b = threading.Thread(target=tpps2.start)

if __name__ == "__main__":
    a.daemon = True;
    b.daemon = True;
    a.start()
    b.start()