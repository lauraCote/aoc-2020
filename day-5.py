import re
import functools

ROWS = 128
SEATS_PER_ROW = 8

def get_seats():
    with open('data/day-5.txt') as file:
        return [(line.rstrip()) for line in file]

def next(range, direction):
    middle = (range[1] - range[0]) // 2
    if direction == 'F' or direction == 'L':
        return (range[0], range[1] - middle - 1)
    if direction == 'B' or direction == 'R':
        return (1 + range[0] + middle, range[1])

def get_seat_id(seat):
    data = re.match(r'([FB]{1,7})([LR]{3})', seat).groups()
    row_range = (0, ROWS - 1)
    row = functools.reduce(next, data[0], row_range)[0]
    
    column_range = (0, SEATS_PER_ROW - 1)
    column = functools.reduce(next, data[1], column_range)[0]

    return row * SEATS_PER_ROW + column

def get_highest_seat(seats):
    return max(map(lambda seat: get_seat_id(seat), seats))

def get_my_seat(seats):
    seat_ids = set(get_seat_id(seat) for seat in seats)
    for seat in range(SEATS_PER_ROW + 1, (SEATS_PER_ROW * (ROWS - 1)) - SEATS_PER_ROW + 1):
        if seat not in seat_ids and (seat + 1) in seat_ids and (seat - 1) in seat_ids:
            return seat

if __name__ == "__main__":
    seats = get_seats()
    print(get_highest_seat(seats))
    print(get_my_seat(seats))