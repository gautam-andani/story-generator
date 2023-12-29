import random
from openai import OpenAI
from django.conf import settings
from django.shortcuts import render
from openai import APIConnectionError

from story_generator.models import SentenceStarter, Character, Place, SecondCharacter, CharacterAge, Activity, Plot, StoryTime


def story_type_input(request):
    return render(request, 'story_input.html')

def index(request):
    random_starter_ids = SentenceStarter.objects.all().values_list('id', flat=True)
    sentence_starter = (SentenceStarter.objects.get(pk=random.choice(list(random_starter_ids)))).content

    random_character_ids = Character.objects.all().values_list('id', flat=True)
    character = (Character.objects.get(pk=random.choice(list(random_character_ids)))).content

    random_place_ids = Place.objects.all().values_list('id', flat=True)
    place = (Place.objects.get(pk=random.choice(list(random_place_ids)))).content

    random_sc_ids = SecondCharacter.objects.all().values_list('id', flat=True)
    second_character = (SecondCharacter.objects.get(pk=random.choice(list(random_sc_ids)))).content

    random_ca_ids = CharacterAge.objects.all().values_list('id', flat=True)
    character_age = (CharacterAge.objects.get(pk=random.choice(list(random_ca_ids)))).content

    random_activity_ids = Activity.objects.all().values_list('id', flat=True)
    activity = (Activity.objects.get(pk=random.choice(list(random_activity_ids)))).content

    random_plot_ids = Plot.objects.all().values_list('id', flat=True)
    plot = (Plot.objects.get(pk=random.choice(list(random_plot_ids)))).content

    random_story_time_ids = StoryTime.objects.all().values_list('id', flat=True)
    story_time = (StoryTime.objects.get(pk=random.choice(list(random_story_time_ids)))).content
    
    if request.method=='POST':
        sentence_starter = request.POST.get('sentence_starter')
        character = request.POST.get('character')
        place = request.POST.get('place')
        second_character = request.POST.get('second_character')
        character_age = request.POST.get('character_age')
        activity = request.POST.get('activity')
        plot = request.POST.get('plot')
        story_time = request.POST.get('story_time')

    story = sentence_starter + character + story_time + plot + place + second_character + character_age + activity

    try:
        client = OpenAI(api_key="") # Your API key here
        message = f"write a creative, interesting, funny and thriller story with words {story} in about 200 words.(avoid spelling mistakes from user prompt)"
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[  
            {"role": "user", "content": message}
        ]
        )

        image_response = client.images.generate(
        model="dall-e-3",
        prompt=f"image of characters in story on prompt {story}",
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = image_response.data[0].url
        story_data = response.choices[0].message.content

    except (ConnectionError, APIConnectionError):
        image_url = None

    context = {
        'story': story_data,
        'image_url': image_url
    }
    return render(request, context=context, template_name='story.html')
