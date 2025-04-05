# paint_calculator


This is a simple Python program to calculate the amount of paint needed for a wall and the cost of purchasing the paint based on the chosen color. The program consists of multiple parts:

## Parts:
1. **Wall Area Calculation:** The program prompts the user for the wall's height and width, then calculates the area in square feet.
2. **Paint Needed Calculation:** Based on a fixed coverage rate of 350 square feet per gallon, the program calculates the amount of paint required to cover the wall.
3. **Cans Needed:** The program uses `math.ceil` to determine how many cans of paint are needed, ensuring the user buys enough.
4. **Cost Calculation:** The program allows the user to choose a paint color (red, blue, green) and calculates the total cost for the required amount of paint.

## Usage

1. Run the script.
2. Provide the wall height and width when prompted.
3. Choose a paint color from the available options: red, blue, or green.
4. The program will display:
   - The wall area.
   - The amount of paint needed.
   - The number of cans required.
   - The total cost based on the selected color.

## Example Output
Enter wall height (feet): 5 
Enter wall width (feet): 32
Wall area: 160 square feet
Paint needed: 0.457143 gallons
Cans needed: 1 can(s)
Choose a color to paint the wall (red,blue,green):red
Cost of purchasing red paint: 
$ 35 
