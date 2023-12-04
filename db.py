import logging

from waifuc.action import ModeConvertAction, AlignMinSizeAction
from waifuc.source import DanbooruSource

logging.basicConfig(level=logging.DEBUG)

for item in DanbooruSource(
        ['animated_gif'],
)[:30].attach(
    ModeConvertAction(),
    AlignMinSizeAction(640),
):
    pass
