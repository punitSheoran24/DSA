class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        found_keys = set(rooms[0])
        n = len(rooms)
        room = [False] * n
        room[0] = True
        while found_keys:
            key = found_keys.pop()

            if not room[key]:
                room[key] = True
                for n in rooms[key]:
                    found_keys.add(n)

        if False in room:
            return False
        return True
