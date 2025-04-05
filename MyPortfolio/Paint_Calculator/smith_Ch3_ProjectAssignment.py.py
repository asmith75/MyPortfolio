#part I
wall_height = int(input('Enter wall height (feet): '))
wall_width = int(input('Enter wall width (feet): '))
wall_area = wall_height * wall_width
print(f'Wall area: {wall_area} square feet')

#part II
paint_coverage = 350 #1gallon/1sqft
paint_needed = wall_area / paint_coverage
print(f'Paint needed: %.6f gallons' %paint_needed)

#part III
import math
cans_needed = math.ceil(paint_needed)
print(f'Cans needed: {cans_needed} can(s)')

#part 4
paint_cost = {'red':35,
              'blue':25,
              'green': 23}
color = input('Choose a color to paint the wall (red,blue,green):')
cost_per_can = paint_cost[color]
total_cost = cost_per_can * cans_needed
print(f"Cost of purchasing {color} paint: \n$ {total_cost} ")
