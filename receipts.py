import csv 
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print the current
# day of the week and the current time.



def main():
    try: 
        subtotal = 0.0
        
        products_dict = read_dictionary("products.csv", 0)
        

        with open ("request.csv") as request:

            reader = csv.reader(request)

            next (reader)

            print("\nThanks for Shopping at FoodRUs")
            print()

            for line in reader:
                product_key = line[0]
                quantity = float(line[1])

                
                item_list = products_dict[product_key]
                global name
                name = item_list[1]
                global price
                price = float(item_list[2])
                multiple_price = price * quantity    
                
                subtotal += (multiple_price)
                sales_tax = subtotal * 0.06
                total = sales_tax + subtotal
                



                print(f'{name}: {quantity} @ ${price}') 
            print()
            print(f"Number of Items: ")
            print(f"Subtotal: {subtotal:.2f} ")
            print(f"Sales Tax: {sales_tax:.2f} ")
            print(f"Total: {total:.2f} ")
            print("Thanks for shopping with us!")
            print(f"{current_date_and_time:%A %b %m %I:%M %p}")
            print()

    except FileNotFoundError as not_found_err:

        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file doesn't exist.")
        print("Run the program again and enter the" \
                " name of a file that exists")
    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read that file.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")    
    except KeyError as key_err:
        print()
        print(type(key_err).__name__, key_err, sep=": " )
        print("You tried to access a key that wasn't in the dictionary" \
               "try again.")
    


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    with open (filename, "rt") as file: 
        products_dict = {}


        reader = csv.reader(file)

        next (reader)

        for row_list in reader:
            if len(row_list) != 0:    

                key = row_list[key_column_index]
                products_dict[key] = row_list

        
        return products_dict
    


if __name__ == "__main__":
    main()

