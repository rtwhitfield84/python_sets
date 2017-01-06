# Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.


songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Elliott Smith', 'Better Be Quiet Now'),
    ('Radiohead', 'Myxomatosis'),
    ('Dumb Fuck City', 'Heavy Emotion'),
    ('Nickelback', 'Photograph'),
    ('Nickelback', 'Animals')
}

greatest_hits = {song for song in songs if song[0] != 'Nickelback'}

print(greatest_hits)