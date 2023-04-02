input={'department' : ['Bakkt', 'Cisco'],'team' : ['Red', 'Yellow', 'Black']}

for k,v in input.items():
    if k=='department':
        departments=(v)
    else:
        teams=(v)

combinations = [{'Department': department, 'Team': team} for department in departments for team in teams]

print(combinations)