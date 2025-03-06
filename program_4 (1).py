# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math
def distance(first_coordinates, second_coordinates):
    coordinate_distance = ((second_coordinates[0] - first_coordinates[0])**2, (second_coordinates[1] - first_coordinates[1])**2, (second_coordinates[2] - first_coordinates[2])**2)
    final_distance1 = math.sqrt(coordinate_distance[0])
    final_distance2 = math.sqrt(coordinate_distance[1])
    final_distance3 = math.sqrt(coordinate_distance[2])
    final_distance_list = [final_distance1,final_distance2,final_distance3]
    final_distance_tuple = tuple(final_distance_list)
    print(final_distance_tuple)

def main():
    try:
        first_coordinates = list(map(int, input('please enter three coordinates separated by spaces:').split()))
        second_coordinates = list(map(int, input('please enter second set of three coordinates separated by spaces:').split()))
        distance(first_coordinates, second_coordinates)
    except string_input_error:
        print('please enter a number not words')

main()
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
#ethan collins 3/6/2025 distance