#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    opened_boxes = set()
    keys = set()
    opened_boxes.add(0)
    keys.update(boxes[0])

    while True:
        new_keys = set()
        for box_index, box_keys in enumerate(boxes):
            if box_index not in opened_boxes and box_index in keys:
                opened_boxes.add(box_index)
                new_keys.update(box_keys)

        if not new_keys:
            break

        keys.update(new_keys)

    return len(opened_boxes) == len(boxes)
