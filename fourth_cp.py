from decimal import Decimal
from math import sqrt

# 1. Create a list, tuple, float, integer, decimal, and dictionary.
friends = ['Jon', 'Mikel', 'Asier']
kitchen_tools = ('fork', 'knife')
school_grade = 7.7
another_school_grade = 7
school_grade_decimal = Decimal(7.7)
sports_teams = {
    'basketball': 'baskonia',
    'football': 'Real Sociedad'
}

# 2. Round your float up
rounded_school_grade = round(school_grade)

# 3. Get the square root of your float
sqrt_school_grade = sqrt(school_grade)

# 4. Select the first element from your dictionary.
first_item = sports_teams['basketball']

# 5. Select the second element from your tuple.
second_kitchen_tool = kitchen_tools[1]

# 6. Add an element to the end of your list.
friends.append('Jaime')

# 7. Replace the first element in your list.
friends[0] = 'Manex'

# 8. Sort your list alphabetically.
friends.sort()

# 9. Use reassignment to add an element to your tuple.
kitchen_tools += ('spoon',)

print('')