import requests

from database.Database import *

PAGE_LENGTH = 300

class UserDataDownloader:
    def get_user_name_and_save_to_db(self, user_id):
        print()  # TODO Remove

    def get_user_anime_list_and_save_to_db(self, user_name):
        last_page: bool = False
        offset: int = 0

        while not last_page:
            animes_list_page = requests.get("https://myanimelist.net/animelist/{}/load.json?offset={}&status=7".format(user_name, offset)).json()
            offset += PAGE_LENGTH  # each page has x entries
            if len(animes_list_page) < PAGE_LENGTH:  # if a page has less than x entries it means it was the last page
                last_page = True

            for anime_json_entry in animes_list_page:
                if anime_json_entry["score"] > 0:  # only add scores that were actually set (0 means none)
                    anime_db_entry = Anime(id=anime_json_entry["anime_id"], name=anime_json_entry["anime_title"])  # TODO add check if anime is already in db
                    anime_db_entry.save()

                    anime_score_db_entry = AnimeScore(anime_id=anime_json_entry["anime_id"], user_name=user_name, score=anime_json_entry["score"])
                    anime_score_db_entry.save()


def test():
    udd = UserDataDownloader()
    udd.get_user_anime_list_and_save_to_db("masterP")
