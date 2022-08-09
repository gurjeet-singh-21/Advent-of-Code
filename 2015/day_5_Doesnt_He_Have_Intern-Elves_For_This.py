##################################
#--- Day 5: Doesn't He Have Intern-Elves For This? ---
#--- part one ---

#For example:
#
#    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#    jchzalrnumimnmhp is naughty because it has no double letter.
#    haegwjzuvuyypxyu is naughty because it contains the string xy.
#    dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
#How many strings are nice?
##################################
with open('test_case_day_5.txt', 'r') as file:
    items = [i[:-1] for i in file]

    list_ = ['ab','cd','pq','xy']
    total = 0

    for data in items:
        cond_1 = cond_2 = cond_3 = True
        count_1 = count_2 = 0
        #condition 1
        for i in data:
            if i in 'aeiou':
                count_1 += 1
        if count_1 < 3:
            cond_1 = False

        #condition 2
        for i in data:
            if i*2 in data:
                count_2 += 1
        if count_2<1:
            cond_2 = False

        #condtion 3
        for i in list_:
            if i in data:
                cond_3 = False

        if cond_1 and cond_2 and cond_3:
            total += 1
    print(total)

