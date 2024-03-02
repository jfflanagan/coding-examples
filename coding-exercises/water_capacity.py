def calc_height(walls):
    left_wall = 0
    right_wall = len(walls) - 1

    capacity = min(walls[left_wall], walls[right_wall]) * right_wall

    while left_wall < right_wall:
        if walls[left_wall] < walls[right_wall]:
            left_wall += 1
        else:
            right_wall -= 1

        capacity = max(capacity, min(walls[left_wall], walls[right_wall]) * (right_wall - left_wall))

    return capacity
          


if __name__ == "__main__":
    #print(calc_height([1,8,6,2,5,4,8,3,7]))
    #print(calc_height([4,3,2,1,4]))
    print(calc_height([1,2,1,3,4,2,1,3]))