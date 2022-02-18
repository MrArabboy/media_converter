import moviepy.editor as mp
from apps.subscriber.models import Member
from apps.bot.buttons.inline import language_buttons


def check_user_exist(update):
    member = update.message.from_user
    user, created = Member.objects.get_or_create(user_id=member.id)
    if created:
        user.update(
            first_name=member.first_name,
            last_name=member.last_name,
            username=f"@{member.username}",
        )
        user.save()
    return user


def start(update, context):
    user = check_user_exist(update)
    if not user.language:
        update.message.reply_html(
            text=f"Assalomu alaykum {user.first_name}!Tilni tanlang:",
            reply_markup=language_buttons(),
        )
    else:
        update.message.reply_html(text=f"Assalomu alaykum {user.first_name}!")


def media(update, context):
    print(update)
    clip = mp.VideoFileClip("any.mp4")
    clip.audio.write_audiofile("audio.mp3")
    clip.subclip(1, 5).write_gif("output.gif")
