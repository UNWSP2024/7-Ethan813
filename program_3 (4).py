# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For, example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    while True:
        year = (input('please enter a year or done to finish '))
        if year == 'done':
            break
        state = input('please enter a state ')
        population = int(input('please enter the population of your selected state and year '))
        all_entered_values.append([year, state, population])
    # Now have the user enter a year. 
    selected_year = input('please enter a year to search ')
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    print(all_entered_values)
    sum_population_for_year(all_entered_values, selected_year)
    return
def sum_population_for_year(all_entered_values, selected_year):
        year = all_entered_values[0]
        if all_entered_values[0][0] == selected_year:
            total_population = all_entered_values[0][2]
            total_population += all_entered_values[1][2]
            total_population += all_entered_values[2][2]
            print(total_population)
    # Loop through and sum the populations for the appropriate year.
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
#ethan collins 3/6/2025 population