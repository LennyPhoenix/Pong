import random

from .basic import Basic


class Ball(Basic):
    def __init__(self, application):
        super().__init__(
            application,
            application.window.width//2-10,
            application.window.height//2-10,
            20, 20,
            (255, 255, 255)
        )
        self.vx = random.choice([-200, 200])
        self.vy = random.randint(-150, 150)

    def update(self, dt):
        if (
            self.aabb[0] < 0 or
            self.aabb[2] > self.application.window.width
        ):
            self.vx *= -1

        if (
            self.aabb[1] < 0 or
            self.aabb[3] > self.application.window.height
        ):
            self.vy *= -1

        super().update(dt)
