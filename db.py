import logging

from waifuc.source import DanbooruSource

logging.basicConfig(level=logging.DEBUG)

for item in DanbooruSource(
        ['animated_gif'],
)[:30]:
    pass
