from typing import Optional, TYPE_CHECKING

from __future__ import annotations

import tcod.event

from actions import Action, EscapeAction, BumpAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()  # Update the FOV before the players next action.
        
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        state = tcod.event.get_keyboard_state()
        player = self.engine.player
        
        if state[tcod.event.Scancode.LSHIFT]:
            if key == tcod.event.KeySym.UP:
                action = BumpAction(player, dx=-1, dy=-1)
            elif key == tcod.event.KeySym.DOWN:
                action = BumpAction(player, dx=1, dy=1)
            elif key == tcod.event.KeySym.LEFT:
                action = BumpAction(player, dx=-1, dy=1)
            elif key == tcod.event.KeySym.RIGHT:
                action = BumpAction(player, dx=1, dy=-1)

        elif key == tcod.event.KeySym.UP:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.KeySym.DOWN:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.KeySym.LEFT:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.KeySym.RIGHT:
            action = BumpAction(player, dx=1, dy=0)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction(player)

        # No valid key was pressed
        return action