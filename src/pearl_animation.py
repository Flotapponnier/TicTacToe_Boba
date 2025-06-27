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
            pearl_img = Image.open("sprites/pearl.png").resize(
                (20, 20), Image.Resampling.LANCZOS
            )

            if pearl_img.mode != "RGBA":
                pearl_img = pearl_img.convert("RGBA")

            self.pearl_image = ImageTk.PhotoImage(pearl_img)
        except Exception as e:
            print(f"Error loading pearl: {e}")
            self.pearl_image = None

    def get_safe_x_position(self):
        screen_width = self.parent.winfo_screenwidth()
        center_zone_start = screen_width * 0.3
        center_zone_end = screen_width * 0.7
        if random.choice([True, False]):
            return random.randint(20, int(center_zone_start))
        else:
            return random.randint(int(center_zone_end), screen_width - 40)

    def start_animation(self, parent_frame):
        if self.pearl_image is None:
            return

        self.stop_animation()
        self.running = True
        self.animate_pearls()

    def animate_pearls(self):
        if not self.running:
            return

        if random.randint(1, 12) == 1:
            self.add_pearl()

        pearls_to_remove = []
        for pearl in self.pearls:
            pearl["y"] += pearl["speed"]
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

            if pearl["y"] > self.parent.winfo_screenheight() + 50:
                try:
                    pearl["label"].destroy()
                except tk.TclError:
                    pass
                pearls_to_remove.append(pearl)

        for pearl in pearls_to_remove:
            if pearl in self.pearls:
                self.pearls.remove(pearl)

        if self.running:
            self.animation_job = self.parent.after(80, self.animate_pearls)

    def add_pearl(self):
        if self.pearl_image is None:
            return

        x = self.get_safe_x_position()
        y = -30
        speed = random.uniform(1.5, 3.5)

        try:
            pearl_canvas = tk.Canvas(
                self.parent,
                width=20,
                height=20,
                bg="#87CEEB",
                highlightthickness=0,
                borderwidth=0,
            )

            pearl_canvas.create_image(10, 10, image=self.pearl_image)
            pearl_canvas.place(x=x, y=y)

            pearl_data = {
                "label": pearl_canvas,
                "base_x": x,
                "y": y,
                "speed": speed,
                "time": random.uniform(0, 6.28),
                "oscillation_speed": random.uniform(0.8, 1.5),
                "oscillation_amplitude": random.uniform(15, 35),
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
