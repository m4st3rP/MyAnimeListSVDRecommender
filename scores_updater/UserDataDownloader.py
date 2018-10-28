import requests

from database.Database import *


class UserDataDownloader:
    def get_user_name_and_save_to_db(self, user_id):
        print()  # TODO Remove

    def get_user_anime_list_and_save_to_db(self, user_name):
        last_page = False
        offset = 0

        while not last_page:
            r = requests.get("https://myanimelist.net/animelist/{}/load.json?offset={}&status=7".format(user_name, offset))
            rj = r.json()
            offset += 300
            if len(rj) < 300:
                last_page = True

            for anime_json_entry in rj:
                if anime_json_entry["score"] > 0:
                    anime_db_entry = Anime(id=anime_json_entry["anime_id"], name=anime_json_entry["anime_title"])
                    anime_db_entry.save()

                    anime_score_db_entry = AnimeScore(anime_id=anime_json_entry["anime_id"], user_name=user_name, score=anime_json_entry["score"])
                    anime_score_db_entry.save()


def test():
    udd = UserDataDownloader()
    udd.get_user_anime_list_and_save_to_db("masterP")
