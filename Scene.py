from __future__ import annotations
import Constants
import App

class Scene:
    id = 0
    constantHelper: Constants = Constants.Constants()
    background = constantHelper.getColor("GRAY")

    def __init__(self, app: App.App):
        app.scenes.append(self)
        app.scene = self
        self.id = Scene.id
        Scene.id += 1