from django.db import models

# Create your models here.
class Anime:
    def __init__(self, name, description, episodes, category):
        self.name = name
        self.description = description
        self.episodes = episodes
        self.category = category


# HARD CODED ANIME INFO #
naruto = Anime(
    'Naruto',
    'Adapted from a comic by Masashi Kishimoto, this animated hit follows the adventures of Naruto Uzumaki, a boy who is determined to become a Hokage, the ninja in his village who is acknowledged as the leader and the strongest of them all.',
    220,
    'Adventure, Fantasy, Martial Arts'
)

naruto_Shippuden = Anime(
    'Naruto Shippuden',
    'adapted from Part II of Masashi Kishimoto\'s manga series, with exactly 500 episodes. It is set two and a half years after Part I in the Naruto universe, following the ninja teenager Naruto Uzumaki and his allies. The series is directed by Hayato Date, and produced by Pierrot and TV Tokyo.',
    500,
    'Adventure, Fantasy, Martial Arts'
)

shows = [naruto, naruto_Shippuden]