from source.model.player import Player
from source.view.entity_view import EntityView


class PickedCardsView(EntityView):

    _rotation: int
    _player: Player

    def __init__(self, parent_surface, pos, size, player: Player, rotation: int = 0):

        super().__init__(parent_surface, pos, size)
        self._player = player
        self._rotation = rotation

    def __initialize_surface(self):

        screen_width = self._parent_surface.get_width()

        x = screen_width / 2 - self._size[0] / 2