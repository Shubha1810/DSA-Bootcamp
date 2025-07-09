def tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 0:
        return
    if n == 1:
        moves.append(f"Move disk 1 from rod {source} to rod {destination}")
        return

    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)

    moves.append(f"Move disk {n} from rod {source} to rod {destination}")

    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)

def solve_hanoi(n):
    if n <= 0:
        print("No disks to move.")
        return
    moves = []
    tower_of_hanoi(n, 'A', 'C', 'B', moves)
    for move in moves:
        print(move)
    print(f"Total moves: {len(moves)}")

print("Input: n = 3 disks\nOutput:")
solve_hanoi(3)

print("\nInput: n = 2 disks\nOutput:")
solve_hanoi(2)