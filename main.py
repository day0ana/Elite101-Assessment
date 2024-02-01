# Program: Movie Seat Finder
# What it does: Take a movie theater’s seat map, and the number of seats the user is looking for, and will return a list of all the available seat options. 

# imports
import theaterSeats as t;

# Level 1: find ALL available seat
def find_available_seats(theater_seats):
    available_seats = [] # tracks available seats

    for row in theater_seats[1:]: # iterates thru each row of theater_seats but the first one as it has the letters 
        row_num = row[0] # row number
        for index, seat_open_noopen in enumerate(row[1:]): # go thru each seat in row
            if seat_open_noopen == 'o': # checks if seat available 
                row_letter = theater_seats[0][index+1] # get letter
                available_seats.append(f"{row_num}{row_letter}") # add available seats list w/ seat NUM y LET
    return available_seats # output available seats list
    ## remember to indent correctly

## TEST level 1
# test1 = find_available_seats(t.theater_seats2)
# print(test1)

# Level 2: list two empty (pair) seats
def find_single_pair(theater_seats):
    pairs_available = [] # tracks available pair seats
    
    for row in theater_seats[1:]: # iterate thru each row of theater_seats
        for index in range(len(row) - 1): #iterate thru each seat in row (-1 bc we start @ index 1)
            if row[index] == 'o' and row[index + 1] == 'o': # checks if PAIR of available seats
                pairs = f"{row[0]}{theater_seats[0][index]}{theater_seats[0][index + 1]}" # add PAIRS available seats
                pairs_available.append(pairs)
                return pairs_available # note: issue here -> feeling implemented incorrectly 
                # ask for clarification on level 2
## TEST level 2
# test2 = find_single_pair(t.theater_seats2)
# print(test2)

# Level 3: list of two empty (pairs) seats
def find_pairs_available(theater_seats):
    pairs_available = [] # tracks pairS available

    for row in theater_seats[1:]: # iterate thru each row of theater_seats
        for index in range(len(row) - 1): #iterate thru each seat in row (-1 bc we start @ index 1)
            if row[index] == 'o' and row[index + 1] == 'o': # checks if PAIR of available seats
                pairs = f"{row[0]}{theater_seats[0][index]}{theater_seats[0][index + 1]}" # add PAIRS available seats
                pairs_available.append(pairs) 
    return pairs_available # return list

## TEST level 3
# test3 = find_pairs_available(t.theater_seats2)
# print(test3)


## CHECKING 
#to print out the seats so you can see them in the console
#This prints out the empty theater - Uncomment to see
#for row in t.theater_seats:
#  print(row)

#this prints out the test theater - Uncomment to see
#for row in t.theater_seats2:
#  print(row)