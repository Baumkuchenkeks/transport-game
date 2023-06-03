from __future__ import annotations
import Constants
import App

class Scene:
    id = 0
    constantHelper: Constants = Constants.Constants()
    background = constantHelper.getColor("GRAY")

    def __init__(self, app: App.App):
        """creates a new Scene
        Scene appents itself to the apps scenes.
        Gets an incrementing id.
        """
        app.scenes.append(self)
        app.scene = self
        self.id = Scene.id
        Scene.id += 1