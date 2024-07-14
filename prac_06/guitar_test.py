"""
Start time = 6.15PM
end time = 10.50PM
"""

from guitar import Guitar


guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 765.4)


current_year = 2022
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age(current_year)}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age(current_year)}")

print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(current_year)}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(current_year)}")
