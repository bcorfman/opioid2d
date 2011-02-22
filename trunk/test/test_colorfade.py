
from Opioid2D import *

class TestSprite(Sprite):
    image = "sprite.png"
    layer = "sprite"

class TestScene(Scene):
    layers = ["sprite"]

    def enter(self):
        s = TestSprite()
        s.set(
            position = (400,300),
            )
        s.do(
            Delay(1.0) + \
            ColorFade((1,0,0), secs=1.0) + \
            ColorFade((0,1,0), secs=1.0) + \
            ColorFade((0,0,1), secs=1.0) + \
            ColorFade((1,1,1), secs=1.0)
            )

Display.init((800,600), title="ColorFade Test")
Director.run(TestScene)
