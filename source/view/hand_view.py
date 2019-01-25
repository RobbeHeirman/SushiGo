import source.view.entity_view as entity_view


class HandView(entity_view.EntityView):
    """
    This is the surface all cards in hand will be on screen.
    This will be an invisible box that bounds the cards a player can choose from.
    The class should be a singleton on the UI. (could enforce this, but seems to off topic).
    The Surface for a han is centered on the bottom of the screen. We could play around with the width and height
    """

    def _initialize_surface(self):
        pass

    def __init__(self, parent_surface):
        super().__init__(parent_surface)
