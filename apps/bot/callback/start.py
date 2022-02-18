import moviepy.editor as mp
from apps.subscriber.models import Member


def start(update, context):
    user = Member.objects.get_or_create(user_id=update.message.from_user.id)


clip = mp.VideoFileClip("any.mp4")
clip.audio.write_audiofile("audio.mp3")
clip.subclip(1, 5).write_gif("output.gif")
