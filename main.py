#!/usr/bin/env python3
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
import tcod
WIDTH, HEIGHT = 80, 60

def main() -> None:

    screen_width=80
    screen_height=50
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)



    tileset= tcod.tileset.load_tilesheet(
    "Tileset.png", 32, 8,  tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    #creating main console:
    console = tcod.Console(screen_width,screen_height, order="F")
    # Create a window based on this console and tileset.
    with tcod.context.new(
       columns=console.width, rows=console.height, tileset=tileset, title="Woodlands", vsync=True,
    ) as context:
        while True:
            console.clear()
            console.print(x=player_x, y=player_y, string="@")
            context.present(console)#show the console

            for event in tcod.event.wait():
                context.convert_event(event)# Sets tile coordinates for mouse events.
                print (event)
                #checking if an action is happening?
                action = event_handler.dispatch(event)
                #if there is no actions, the skip the rest I guess?
                if action is None:
                    continue
              
                if isinstance(action, MovementAction):
                    # if there is an instance of a movement action 
                    #changing the player X,Y if there is a movemnet action
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    #obvs another escape action..
                    raise SystemExit()




if __name__ == "__main__":
    main()
