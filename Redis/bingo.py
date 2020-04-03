import os
import redis

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
GLOBE = "stone_list"

class _Numbers:

    def __init__(self):
      numbers = [x for x in range(1, 100)]
      redis_db.sadd(GLOBE, *numbers)

class _Cards:

    def __init__(self, CARDS):

        for x in range(0, CARDS):
            card        = f"{x:02d}"
            name        = f"user{card}"
            player_name = f"user{card}"
            card_name   = f"cartela:{card}"
            score_name  = f"score:{card}"

            redis_db.hset(name, "name", player_name)
            redis_db.hset(name, "bcartela", card_name)
            redis_db.hset(name, "bscore", score_name)

            card = redis_db.srandmember(GLOBE, number=15)
            redis_db.rpush(card_name, *card)

            redis_db.set(score_name, 0)

class _Bingo: 

    def __init__(self):
        _Numbers()
        _Cards(50)
        
    def play(self, PLAYERS):
        round = 0
        winner = False
                
        while not winner:
            round += 1
            number = int(redis_db.spop(GLOBE))
            players_found = []

            for player in range(0, PLAYERS):
                card = f"{player:02d}"
                name = f"user{card}"
                player_info = redis_db.hgetall(name)

                if redis_db.lrem(player_info[b"bcartela"], 1, number) != 0:
                    players_found.append(name)
                    redis_db.incr(player_info[b"bscore"])
                    winner = int(redis_db.get(player_info[b"bscore"])) == 15

            print("")
            print("Rodada: {0}".format(round))
            print("Número sorteado: {0}".format(number))

            if (winner):
                print("**********************************************")
                print("BINGO!  O vencedor é {0}".format(name))
                print("**********************************************")            
            else:
                print("Jogadores que pontuaram na rodada: {0}".format(",".join(players_found)))   

        os.system("PAUSE")


def initialize():
    redis_db.flushall()
    b = _Bingo()
    b.play(50)
    

if __name__ == '__main__':
    initialize()