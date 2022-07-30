################################################
#--- Day 2: I Was Told There Would Be No Math ---
#--- part one ---
#For example:
#
#    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
#
#All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
################################################

total = 0
with open('test_case_day_2.txt', 'r') as file:
    for data in file:
        dimensions = data.split('x')
        dimensions[-1] = dimensions[-1].split('\n')
        dimensions[0] = int(dimensions[0])
        dimensions[1] = int(dimensions[1])
        dimensions[2] = int(dimensions[2][0])
#        #print(dimensions)
#        
#        area_side_1 = dimensions[0] * dimensions[1]
#        area_side_2 = dimensions[0] * dimensions[2]
#        area_side_3 = dimensions[2] * dimensions[1]
#
#        min_area_needed = min(area_side_3, area_side_1, area_side_2)
#
#        box_surface_area = 2 * (area_side_1 + area_side_2 + area_side_3)
#
#        total += min_area_needed + box_surface_area
#
#    print(total)

############################################
#--- Part Two ---
#
#For example:
#
#    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
#
#How many total feet of ribbon should they order?
###########################################
        bow_ribbon = 1
        wrap_ribbon = 0
        for dim in dimensions:
            bow_ribbon *= dim

        dimensions.remove(max(dimensions))
        for dim in dimensions:
            wrap_ribbon += (dim + dim)

        total += bow_ribbon + wrap_ribbon
    print(total)

        








