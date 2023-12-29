from django.db import models

class Base(models.Model):
    content = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.content


class SentenceStarter(Base):
    pass


class Character(Base):
    pass


class StoryTime(Base):
    pass


class Plot(Base):
    pass


class Place(Base):
    pass


class SecondCharacter(Base):
    pass


class CharacterAge(Base):
    pass


class Activity(Base):
    pass