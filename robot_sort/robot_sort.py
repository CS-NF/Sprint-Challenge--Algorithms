class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"


# *** Understand ***
# Use bubble sort
# The robot can move either left or right
# It can only hold on item and if it picks up an item it has to swap it for the one it's holding
# It can compare items

# *** Plan ***
# call self.swap_item to initially swap the first item with "None"
# cretae a while loop to dretirmin while function is true
# cretae an if statment to see if the robot is able to even move right
# if the robot CAN move right use swap method to swap the item 
# stop the if statment condition 
# create a while loop if the robot can move right is True 
# since we know the robot can now move right tell it to start moving right
# once the robot get's in front of the item compar the item by [0:1] to see if the item the robot is in front of is greater or smaller then the one it's holding
# if it is swap the item
# create a while loop to see if the robot can move left if it can tell the robot to go to the "None" placehold we droped at the begging of the list
# tell robot to move left
# Once the robot is at the begging of of list tell it to drop off the number it's holding and pick up none
# now everything to the left of the robot should be sorted
# robot then repeat the process 

    def sort(self):
        self.swap_item() # this swaps the first item the robot is on initially to start the bubble sort
        while True:
            print("something")
            if not self.can_move_right(): # if statment checks to see if robot can not move right
                self.swap_item() # if the robot can not move right it will swap the item
                break # if the robot can move right
            while self.can_move_right(): # if the robot can move right
                self.move_right() # the robot will begin to move right by one index at a time
                if self.compare_item() == 1: # compare the index in front and if the index the robot is holding onto is greater then the index in front
                    self.swap_item() # swap that index
            while self.can_move_left() and self.compare_item() is not None: # checking to see if robot can move left and stoping at "None"
                self.move_left() # robot will iterate through the list moving left until it reaches the end of the list at "None
            self.swap_item()  # dropping smallest value and swapping with "None"
            self.move_right() # move right so that everything to the left of the robot is sorted
            self.swap_item() # will drop "None" for the next unsorted value
    

# *** Rules ***

# You may use any pre-defined robot methods.
# You may NOT modify any pre-defined robot methods.
# You may use logical operators. (if, and, or, not, etc.)
# You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
# You may use iterators. (while, for, break, continue)
# You may NOT store any variables. (=)
# You may NOT access any instance variables directly. (self._anything)
# You may NOT use any Python libraries or class methods. (sorted(), etc.)
# You may define robot helper methods, as long as they follow all the rules.


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)