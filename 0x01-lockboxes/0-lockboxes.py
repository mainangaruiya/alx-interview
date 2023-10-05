def canUnlockAll(boxes):
    num_boxes = len(boxes)
    keys = set()
    opened_boxes = set()
    current_box = 0

    while current_box < num_boxes:
        opened_boxes.add(current_box)
        keys.update(boxes[current_box])

        # Find the next unopened box that can be opened
        next_box = None
        for key in keys:
            if key < num_boxes and key not in opened_boxes:
                next_box = key
                break

        if next_box is None:
            break  # No more boxes can be opened

        current_box = next_box

    # Check if all boxes have been opened except the first one (index 0)
    return len(opened_boxes) == num_boxes - 1

# Example usage:
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False

