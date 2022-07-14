#!/usr/bin/env python3
from engine import Engine
from input_handlers import EventHandler
from entity import Entity
from game_map import GameMap
import tcod
WIDTH, HEIGHT = 80, 60

def main() -> None:

    screen_width=80
    screen_height=50

    map_width = 80
    map_height = 45

    tileset= tcod.tileset.load_tilesheet(
    "Tileset.png", 32, 8,  tcod.tileset.CHARMAP_TCOD
    
    )
    GameMap.do_step()

    event_handler = EventHandler()
    #creating main console
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    #the player
    orc = Entity(int(screen_width / 2 - 15), int(screen_height / 6), "O", (255, 255, 0))
    
    # a rando
    entities = {player, orc}

    game_map = GameMap(map_width, map_height)
# full list of entities. will probably get moved later
    engine = Engine(entities=entities, event_handler=event_handler,game_map=game_map, player=player)

    console = tcod.Console(screen_width, screen_height, order="F")
# Create a window based on this console and tileset.
    with tcod.context.new(
       columns=console.width, rows=console.height, tileset=tileset, title="Woodlands", vsync=True,
    ) as context:
        while True:
            engine.render(console=console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)





if __name__ == "__main__":
    main()
