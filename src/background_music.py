import pygame
import os
import threading
import time


class BackgroundMusicManager:
    def __init__(self, volume=0.3):
        self.volume = volume
        self.is_playing = False
        self.music_file = None
        self.music_thread = None
        self.should_stop = False

        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            print("Audio system initialized successfully")
        except Exception as e:
            print(f"Error initializing audio: {e}")
            self.audio_available = False
        else:
            self.audio_available = True

    def load_music(self, music_file_path):
        if not self.audio_available:
            return False

        if not os.path.exists(music_file_path):
            print(f"Music file not found: {music_file_path}")
            return False

        try:
            self.music_file = music_file_path
            pygame.mixer.music.load(music_file_path)
            pygame.mixer.music.set_volume(self.volume)
            print(f"Music loaded: {os.path.basename(music_file_path)}")
            return True
        except Exception as e:
            print(f"Error loading music: {e}")
            return False

    def play_music(self, loop=True):
        if not self.audio_available or not self.music_file:
            return

        try:
            loops = -1 if loop else 0
            pygame.mixer.music.play(loops)
            self.is_playing = True
            print("Background music started")
        except Exception as e:
            print(f"Error playing music: {e}")

    def stop_music(self):
        if not self.audio_available:
            return

        try:
            pygame.mixer.music.stop()
            self.is_playing = False
            print("Background music stopped")
        except Exception as e:
            print(f"Error stopping music: {e}")

    def pause_music(self):
        if not self.audio_available:
            return

        try:
            pygame.mixer.music.pause()
            print("Background music paused")
        except Exception as e:
            print(f"Error pausing music: {e}")

    def unpause_music(self):
        if not self.audio_available:
            return

        try:
            pygame.mixer.music.unpause()
            print("Background music resumed")
        except Exception as e:
            print(f"Error resuming music: {e}")

    def set_volume(self, volume):
        if not self.audio_available:
            return

        self.volume = max(0.0, min(1.0, volume))
        try:
            pygame.mixer.music.set_volume(self.volume)
            print(f"Volume set to {self.volume}")
        except Exception as e:
            print(f"Error setting volume: {e}")

    def is_music_playing(self):
        if not self.audio_available:
            return False

        try:
            return pygame.mixer.music.get_busy()
        except:
            return False

    def cleanup(self):
        if self.audio_available:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                print("Audio system cleaned up")
            except Exception as e:
                print(f"Error during audio cleanup: {e}")


class MusicIntegration:
    @staticmethod
    def setup_music_in_app(app):
        app.music_manager = BackgroundMusicManager(volume=0.2)

        music_path = os.path.join("music", "retro_background.mp3")
        if app.music_manager.load_music(music_path):
            app.music_manager.play_music(loop=True)

    @staticmethod
    def add_music_controls_to_ui(parent_frame, music_manager):
        import tkinter as tk

        controls_frame = tk.Frame(parent_frame, bg="#87CEEB")
        controls_frame.pack(side="bottom", pady=10)

        def toggle_music():
            if music_manager.is_music_playing():
                music_manager.pause_music()
                toggle_btn.config(text="🎵 Play Music")
            else:
                music_manager.unpause_music()
                toggle_btn.config(text="🔇 Pause Music")

        def volume_up():
            current_vol = music_manager.volume
            music_manager.set_volume(current_vol + 0.1)

        def volume_down():
            current_vol = music_manager.volume
            music_manager.set_volume(current_vol - 0.1)

        toggle_btn = tk.Button(
            controls_frame,
            text="🔇 Pause Music",
            command=toggle_music,
            bg="#FFD700",
            font=("Arial", 10),
        )
        toggle_btn.pack(side="left", padx=5)

        vol_down_btn = tk.Button(
            controls_frame,
            text="🔉",
            command=volume_down,
            bg="#FFB6C1",
            font=("Arial", 10),
        )
        vol_down_btn.pack(side="left", padx=2)

        vol_up_btn = tk.Button(
            controls_frame,
            text="🔊",
            command=volume_up,
            bg="#FFB6C1",
            font=("Arial", 10),
        )
        vol_up_btn.pack(side="left", padx=2)
