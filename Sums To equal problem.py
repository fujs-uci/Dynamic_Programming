#==========================
# Equals problem
#       given a list of numbers, addition
#       add to another list of numbers, equalto
#       so that all the numbers in equal to are equal,
#       return amount of operations it took
#==========================

def equal( arr):
        addition = [1,3,5]
        temp_arr = sorted(arr)
        total = 0

        while max(temp_arr) != min(temp_arr):
                total+=1
                check_dif_max = []
                check_dif_rest = []
                for value in addition:

                        check_max = temp_arr[-1] - value
                        check_dif_max.append([abs(check_max-item) for item in temp_arr[:-1]])
                        check_dif_rest
                        
                best_step = check_dif_max.index(min(check_dif_max))
                temp_arr = sorted(temp_arr[:-1] + [(temp_arr[-1] - addition[best_step])])
                print(temp_arr)
                input("...")
                
                        
        return total

bt1 = [53, 361, 188, 665, 786, 898, 447, 562, 272, 123, 229, 629, 670, 848, 994, 54, 822, 46, 208, 17, 449, 302, 466, 832, 931, 778, 156, 39, 31, 777, 749, 436, 138, 289, 453, 276, 539, 901, 839, 811, 24, 420, 440, 46, 269, 786, 101, 443, 832, 661, 460, 281, 964, 278, 465, 247, 408, 622, 638, 440, 751, 739, 876, 889, 380, 330, 517, 919, 583, 356, 83, 959, 129, 875, 5, 750, 662, 106, 193, 494, 120, 653, 128, 84, 283, 593, 683, 44, 567, 321, 484, 318, 412, 712, 559, 792, 394, 77, 711, 977, 785, 146, 936, 914, 22, 942, 664, 36, 400, 857]
bt2 = [512, 125, 928, 381, 890, 90, 512, 789, 469, 473, 908, 990, 195, 763, 102, 643, 458, 366, 684, 857, 126, 534, 974, 875, 459, 892, 686, 373, 127, 297, 576, 991, 774, 856, 372, 664, 946, 237, 806, 767, 62, 714, 758, 258, 477, 860, 253, 287, 579, 289, 496]
test1 = [2,2,3,7]
test2 = [10, 7, 12]
print(equal(bt2))
