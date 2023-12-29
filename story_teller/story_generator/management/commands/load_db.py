
from django.core.management.base import BaseCommand
from story_generator.models import SentenceStarter, Character, Place, SecondCharacter, CharacterAge, Activity, Plot, StoryTime

sentence_starter = ['In the past', 'About 100 years ago', 'In the 20 BC', 'Once upon a time', 'In 1990s',
                    'In the ancient Egypt']
character = [' there lived a king.', ' there was a man named Jack.', ' there was a young boy.', ' there was a old man.',
             ' there lived a farmer.', ' there was a man who lived with her son.']
time = [' One day', ' One full-moon night', ' One night', ' In the morning', ' At midnight']
story_plot = [' he was passing by', ' he was going for a picnic to', ' he is standing', ' he is walking',
              ' talking with old guy']
place = [' the mountains', ' the garden', ' the yard', ' the fence', ' the hills', ' the forest']
second_character = [' he saw a man', ' he saw a lady', ' he saw a boy', ' he saw a woman', ' he saw a girl']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble', ' who seemed very young',
       ' who is very old looking']
activity = [' searching something.', ' digging a well on roadside.', ' trying to catch a snake.',
            ' looking from the window of the house.', ' fighting with someone.', ' counting the gold coins.',
            ' trying to hide.', ' entering the hive.', ' riding the horse.', ' want to escape.']


class Command(BaseCommand):
    def handle(self, *args, **options):

        for ss in sentence_starter:
            ss_o = SentenceStarter(content=ss)
            ss_o.save()

        for c in character:
            c_o = Character(content=c)
            c_o.save()

        for t in time:
            t_o = StoryTime(content=t)
            t_o.save()

        for sp in story_plot:
            sp_o = Plot(content=sp)
            sp_o.save()

        for p in place:
            p_o = Place(content=p)
            p_o.save()

        for a in age:
            a_o = CharacterAge(content=a)
            a_o.save()

        for ac in activity:
            ac_o = Activity(content=ac)
            ac_o.save()

        for sc in second_character:
            sc_o = SecondCharacter(content=sc)
            sc_o.save()