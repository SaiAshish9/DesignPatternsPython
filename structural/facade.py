# Subsystem Classes
class AudioPlayer:
    def play_audio(self, file):
        print(f"Playing audio file: {file}")

class VideoPlayer:
    def play_video(self, file):
        print(f"Playing video file: {file}")

class ImageRenderer:
    def render_image(self, file):
        print(f"Rendering image file: {file}")

class MultimediaFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.image_renderer = ImageRenderer()

    def play_music(self, music_file):
        self.audio_player.play_audio(music_file)

    def play_movie(self, movie_file):
        self.video_player.play_video(movie_file)

    def display_image(self, image_file):
        self.image_renderer.render_image(image_file)

if __name__ == "__main__":
    multimedia_system = MultimediaFacade()
    multimedia_system.play_music("song.mp3")
    multimedia_system.play_movie("movie.mp4")
    multimedia_system.display_image("picture.jpg")
