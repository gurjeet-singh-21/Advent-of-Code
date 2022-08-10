#######################################
#--- Day 5: Doesn't He Have Intern-Elves For This? ---
#--- Part Two ---
#
#For example:
#
#    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
#
#How many strings are nice under these new rules?
#######################################

with open('test_case_day_5.txt', 'r') as file:
    items = [i[:-1] for i in file]

    total = 0

    for key in items:
        cond_1 = cond_2 = True
        
        #condition 1
        for i in range(1, len(key)):
            if key[i-1:i+1] in key[(i+1):]:
                break
        else:
            cond_1 = False
            
        # condition 2
        for i in range(len(key)-2):
            if key[i] == key[i+2]:
                break
        else:
            cond_2 = False

        if cond_1 and cond_2:
            total += 1
    print(total)

