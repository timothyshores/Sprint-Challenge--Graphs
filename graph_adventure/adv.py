from room import Room
from player import Player
from world import World
from room_graphs import rg1, rg2, rg3, rg4, rg5

world = World()             # load world
roomGraph = rg5             # set rg5 as roomGraph from room_graphs.py
world.loadGraph(roomGraph)  # loadGraph method from world.py
world.printRooms()          # printRooms method from world.py
player = Player("Name", world.startingRoom)  # initialize player

paths_traversed = []    # paths traversed
paths_reverse = []      # paths traversed in reverse
rooms_visited = {}      # dictionary stores previously visited rooms

# dictionary with reverse direction key value pair
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# set rooms_visited key at currentRoom.id to the value currentRoom.getExits
rooms_visited[player.currentRoom.id] = player.currentRoom.getExits()

#  while all rooms have NOT been visited
while len(rooms_visited) < len(roomGraph) - 1:
    # if player has not visited the currentRoom
    if player.currentRoom.id not in rooms_visited:
        # set value of the currentRoom key to currentRoom.getExits() in rooms_visited dictionary
        rooms_visited[player.currentRoom.id] = player.currentRoom.getExits()
        # last direction traveled
        previous_direction = paths_reverse[-1]
        # remove previous_direction value at the currentRoom key from rooms_visited dictionary
        rooms_visited[player.currentRoom.id].remove(previous_direction)
    # while value of rooms_visited at the currentRoom key is empty
    while len(rooms_visited[player.currentRoom.id]) == 0:
        # remove the last element in paths_reverse and set to a varaible reverse
        reverse = paths_reverse.pop()
        # add reverse to the end of the paths_traversed list
        paths_traversed.append(reverse)
        # move the player in the reverse direction
        player.travel(reverse)
    # pop off last room exit and set to exit_direction
    exit_direction = rooms_visited[player.currentRoom.id].pop()
    # append exit_direction to paths_traversed
    paths_traversed.append(exit_direction)
    # append the reverse or opposite direction to  paths_reverse
    paths_reverse.append(reverse_direction[exit_direction])
    # travel towads exit_direction
    player.travel(exit_direction)

# TRAVERSAL TEST

 # create new set called visited_rooms
visited_rooms = set()
# set player.currentRoom to world.startingRoom
player.currentRoom = world.startingRoom
# add player's current room to visited_rooms set
visited_rooms.add(player.currentRoom)
# loop through paths_traversed
for move in paths_traversed:
    # move player through every element in paths_traversed
    player.travel(move)
    # add current room to visited_rooms set
    visited_rooms.add(player.currentRoom)

# if all rooms were visited print TESTS PASSED
if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(paths_traversed)} moves, {len(visited_rooms)} rooms visited")
# else print TESTS FAILED
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
