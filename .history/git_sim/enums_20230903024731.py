from enum import Enum


class ResetMode(Enum):
    DEFAULT = "mixed"
    SOFT = "soft"
    MIXED = "mixed"
    HARD = "hard"


class StashSubCommand(Enum):
    POP = "pop"
    APPLY = "apply"
    PUSH = "push"


class ColorByOptions(Enum):
    AUTHOR = "author"
    BRANCH = "branch"
    NOTLOCAL1 = "notlocal1"
    NOTLOCAL2 = "notlocal2"

    # Reset the remotes in the local clone to the original remotes


class StyleOptions(Enum):
    CLEAN = "clean"
    THICK = "thick"


class VideoFormat(str, Enum):
    MP4 = "mp4"
    WEBM = "webm"


class ImgFormat(str, Enum):
    JPG = "jpg"
    PNG = "png"
