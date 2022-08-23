#--- Day 8: Matchsticks ---
#--- part one ---

string_literals = 0
string_values = 0

with open('test_case_day_8.txt', 'r') as file:
    data = [i.strip() for i in file]

#for i in data:
#    string_literals += len(i)
#    
#    string_values += len(eval(i))
#
#print(string_literals - string_values)
    
# --- Part Two ---

for i in data:
    string_values += len(i)

for i in data:
      string_literals += len(i) + 2 + len(list(filter(lambda x: x in '\\"',i)))

print(string_literals - string_values)
