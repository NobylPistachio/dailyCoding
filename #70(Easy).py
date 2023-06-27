# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

#-----------------------------------------------------------------------------
    #psuedocode
# need to break a number up by it's digits      
    #turn number into a list                        DONE
    #if list sums to 10 then number is perfect      
# user gives you a number, you give back the n-th number of the perfect list (might need a way to save the list of perfect numbers)


def list_setup(limit:int) -> list:
    perfect_numbers:list = []
    #while I done have 5 numbers in this list I don't want it to stop
    num:int=0
    while len(perfect_numbers) <= (limit):
        
        #check if number is a perfect number
        num_to_list = [int(number) for number in list(str(num))]
        sum_10:int = 0
        for elem in num_to_list:
            sum_10 += elem
        if sum_10 == 10:
            perfect_numbers.append(num)

        if len(perfect_numbers) > limit:
            break
        
        num+=1
    
    return perfect_numbers
    #return a list, if list is greater than 10 or we should have a cache for that recent number
    
def main():
    user = int(input("Give a positive integer: "))
    perfect_numbers:list = list_setup(user)
    print(f'the list of {len(perfect_numbers)} perfect_numbers are: {perfect_numbers}')
    print(f'You have selected the {user}th perfect number: {perfect_numbers[user]}')

if __name__ == "__main__":
    main()