import tcod
import copy
import traceback
import color
from engine import Engine
from entity import Entity
from procgen import generate_dungeon
import entity_factories
from dungeon_name import generate_dungeon_name

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    max_monsters_per_room = 3
    max_items_per_room = 2
    
    tileset = tcod.tileset.load_tilesheet("Md_curses_16x16.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    player = copy.deepcopy(entity_factories.player)
    
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
        engine=engine,)
    
    engine.update_fov()
    
    dungeon_name = generate_dungeon_name()
    engine.message_log.add_message(
        "Hello, delver.", color.welcome_text
    )
    engine.message_log.add_message(
        f"Thou shalt now enter the place known as the {dungeon_name}.", color.welcome_text
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,          # Setting up the console
        tileset=tileset,
        title="MythicRogue",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            # Basic loop
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error to stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(traceback.format_exc(), color.error)


if __name__ == "__main__":
    main()
