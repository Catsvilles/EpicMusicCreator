from pysynth_b import *
song = (
    ('c', 16),
    ('d', 16),
    ('e', 4),
    ('g', 4),
    ('e', 4),
    ('e', 8),
    ('d', 16),
    ('e', 16),
    ('d', 16),
    ('c', 2),
    ('r', 4),
    ('e', 8),
    ('g', 8),
    ('a', 3),
    ('c5', 8),
    ('b', 4),
    ('g', 4),
    ('e', 2),
    ('d', 4),
    ('c', 8),
    ('d', 8),
    ('e', 4),
    ('g', 4),
    ('e', 16),
    ('d', 6),
    ('c', 6),
    ('d', 16),
    ('c', 2),
    ('r', 4)
)

make_wav(song, fn="InDreams.wav", bpm=120)
