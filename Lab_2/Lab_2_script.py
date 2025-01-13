# Question 1: Take the following list and multiply all list items together.
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
part1_answer = 1
for i in part1:
    part1_answer = part1_answer * i
print('The result of question #1 is: ' + str(part1_answer))

# Question 2: Take the following list and add all list items together.
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
part2_answer = 0
for i in part2:
    part2_answer = part2_answer + i
print('The result of question #2 is: ' + str(part2_answer))


# Question 3: Take the following list and only add together those list items which are even.
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 

part3_answer = 0
for i in part3:
    if i % 2 == 0:
        part3_answer = part3_answer + i
print('The result of question #3 is: ' + str(part3_answer))