from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("sound.wav")
play(song)

