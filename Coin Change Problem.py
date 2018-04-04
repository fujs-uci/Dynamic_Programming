# 4, [1,2,3]
#[[1,1,1,1],[1,1,2],[2,2],[1,3]]

## Test case 1
goal = 10
test = [2,3,5,6]
test2 = [2,3,5,6]


toops = []
answer = []
for x in test:
        for y in test2:
                res_value = x + y
                test = sorted([x,y,res_value])
                teste = [test[0],test[1],test[2]]
                if teste in toops:
                        continue
                if res_value > goal:
                        continue
                if res_value == goal:
                        answer.append(teste)
                        break
                toops.append([x,y,res_value])
        copy_toops = toops
        for i,j,k in copy_toops:
                res_value = x + k
                og = [x,k, res_value]
                r_og = [x for x in sorted([x,k, res_value])]
                if og in toops: continue
                if r_og in toops: continue
                if res_value > goal:continue
                if res_value == goal:
                        answer.append(og)
                        break
                toops.append([x,k,res_value])

top_level = [t[1] for t in answer]
bottom_level = sorted([t for t in toops if (t[-1] in top_level) or (t[-1] in test) ], key = lambda x : x[-1])
bottom_level2 = bottom_level
##for i in bottom_level2:
##        buffer = bottom_level
##        looking = i[-1]
##        adding = i[-1]
##        while (len(buffer) != 0):
##                new_constr = []
##                hammer = buffer[0]
##                for j in hammer[1:-1]:
##                        if looking == j:
                                
print(bottom_level)
print(answer)

#[[2, 2, 4], [2, 3, 5], [2, 4, 6], [3, 3, 6], [2, 5, 7], [3, 4, 7], [2, 6, 8], [3, 5, 8]]
# ex... [2,2,4] search for 4 in ^, replace all 4 with [2,2]
# thus.... [3,4,7] -> [3,2,2,7]
# thus.... [2,4,6] -> [2,2,2,6]
# ex... [2,6,8] -> [2,2,4,8] and [2,2,2,2,8]
#answer, replace the middle item  with the middle level

                                
                



