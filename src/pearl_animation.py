import tkinter as tk
import random
import math
from PIL import Image, ImageTk


class PearlAnimation:
    def __init__(self, parent_window):
        self.parent = parent_window
        self.pearls = []
        self.pearl_image = None
        self.running = False
        self.animation_job = None
        self.load_pearl_image()

    def load_pearl_image(self):
        try:
            base_size = 20
            pearl_img = Image.open("sprites/pearl.png").resize(
                (base_size, base_size), Image.Resampling.LANCZOS
            )

            if pearl_img.mode != "RGBA":
                pearl_img = pearl_img.convert("RGBA")

            self.pearl_image = ImageTk.PhotoImage(pearl_img)
        except Exception as e:
            print(f"Error loading pearl: {e}")
            self.pearl_image = None

    def get_safe_x_position(self):
        """Calcule une position X sûre en fonction de la taille actuelle de la fenêtre"""
        try:
            screen_width = self.parent.winfo_width()
            if screen_width <= 1:
                screen_width = self.parent.winfo_screenwidth()
        except:
            screen_width = 1200

        center_zone_start = screen_width * 0.25
        center_zone_end = screen_width * 0.75

        if random.choice([True, False]):
            return random.randint(20, max(int(center_zone_start), 50))
        else:
            return random.randint(
                min(int(center_zone_end), screen_width - 60),
                max(screen_width - 40, int(center_zone_end) + 10),
            )

    def get_window_height(self):
        """Obtient la hauteur actuelle de la fenêtre"""
        try:
            height = self.parent.winfo_height()
            return height if height > 1 else self.parent.winfo_screenheight()
        except:
            return 800

    def start_animation(self, parent_frame):
        if self.pearl_image is None:
            return

        self.stop_animation()
        self.running = True
        self.animate_pearls()

    def animate_pearls(self):
        if not self.running:
            return

        # Fréquence d'apparition adaptée à la taille de la fenêtre
        window_width = getattr(self.parent, "winfo_width", lambda: 1200)()
        if window_width <= 1:
            window_width = 1200

        spawn_rate = max(
            8, min(15, int(window_width / 80))
        )  # Plus grande fenêtre = plus de perles

        if random.randint(1, spawn_rate) == 1:
            self.add_pearl()

        pearls_to_remove = []
        current_height = self.get_window_height()

        for pearl in self.pearls:
            # Vitesse adaptée à la taille de l'écran
            speed_modifier = min(1.5, max(0.8, current_height / 800))
            pearl["y"] += pearl["speed"] * speed_modifier
            pearl["time"] += 0.1

            oscillation = (
                math.sin(pearl["time"] * pearl["oscillation_speed"])
                * pearl["oscillation_amplitude"]
            )
            new_x = pearl["base_x"] + oscillation

            pearl["rotation"] += pearl["rotation_speed"]
            if pearl["rotation"] >= 360:
                pearl["rotation"] = 0

            try:
                pearl["label"].place(x=int(new_x), y=int(pearl["y"]))
            except tk.TclError:
                pearls_to_remove.append(pearl)
                continue

            # Supprimer les perles qui sortent de l'écran
            if pearl["y"] > current_height + 50:
                try:
                    pearl["label"].destroy()
                except tk.TclError:
                    pass
                pearls_to_remove.append(pearl)

        for pearl in pearls_to_remove:
            if pearl in self.pearls:
                self.pearls.remove(pearl)

        if self.running:
            # Intervalle d'animation adapté à la performance
            interval = 60 if len(self.pearls) > 20 else 80
            self.animation_job = self.parent.after(interval, self.animate_pearls)

    def add_pearl(self):
        if self.pearl_image is None:
            return

        x = self.get_safe_x_position()
        y = -30

        # Vitesse adaptée à la taille de la fenêtre
        window_height = self.get_window_height()
        base_speed = max(1.5, min(4.0, window_height / 250))
        speed = random.uniform(base_speed * 0.8, base_speed * 1.2)

        try:
            # Taille de perle adaptée
            pearl_size = max(15, min(25, int(20 * (window_height / 800))))

            pearl_canvas = tk.Canvas(
                self.parent,
                width=pearl_size,
                height=pearl_size,
                bg="#87CEEB",
                highlightthickness=0,
                borderwidth=0,
            )

            pearl_canvas.create_image(
                pearl_size // 2, pearl_size // 2, image=self.pearl_image
            )
            pearl_canvas.place(x=x, y=y)

            try:
                window_width = self.parent.winfo_width()
                if window_width <= 1:
                    window_width = 1200
            except:
                window_width = 1200

            max_amplitude = min(50, window_width / 30)

            pearl_data = {
                "label": pearl_canvas,
                "base_x": x,
                "y": y,
                "speed": speed,
                "time": random.uniform(0, 6.28),
                "oscillation_speed": random.uniform(0.8, 1.5),
                "oscillation_amplitude": random.uniform(15, max_amplitude),
                "rotation": random.uniform(0, 360),
                "rotation_speed": random.uniform(1, 4),
            }
            self.pearls.append(pearl_data)
        except tk.TclError:
            pass

    def stop_animation(self):
        self.running = False

        if self.animation_job is not None:
            self.parent.after_cancel(self.animation_job)
            self.animation_job = None

        for pearl in self.pearls:
            try:
                pearl["label"].destroy()
            except (tk.TclError, KeyError):
                pass
        self.pearls.clear()
