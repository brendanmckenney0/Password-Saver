import pickle
import sys

#The password list - We start with it populated for testing purposes
entries = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]
#The password file name to store the data to
password_file_name = "samplePasswordFile.pickle"
#The encryption key for the caesar cypher
encryption_key = 16

# We need to add additional menu options to accomodate extra credit functions
menu_text = """
What would you like to do:
1. Open password file
2. Lookup a password
3. Add a password
4. Save password file
5. Print the encrypted password list (for testing)
6. Quit program
7. Delete Password
Please enter a number (1-6)"""

def password_encrypt (unencrypted_message, key):
    """Returns an encrypted message using a caesar cypher

    :param unencrypted_message (string)
    :param key (int) The offset to be used for the caesar cypher
    :return (string) The encrypted message
    """
    result_string = ''
    min_limit = 32
    max_limit = 126
    for character in unencrypted_message:
        value = ord(character) - min_limit + key
        value = value % (max_limit - min_limit + 1)
        value = value + min_limit
        result_string = result_string + chr(value)
    return result_string



def load_password_file(file_name):
    """Loads a password file.  The file must be in the same directory as the .py file

    :param file_name (string) The file to load.  Must be a pickle file in the correct format
    """
    entries, encryption_key = pickle.load(file_name, 'rb')

def save_password_file(file_name):
    """Saves a password file.  The file will be created if it doesn't exist.

    :param file_name (string) The file to save.
    """
    pickle.dump( (entries, encryption_key), open( file_name, "wb" ) )


def add_entry(website, password):
    """Adds an entry with a website and password

    Logic for function:

    Step 1: Use the password_encrypt() function to encrypt the password.
            The encryptionKey variable is defined already as 16, don't change this
    Step 2: create a list of size 2, first item the website name and the second
            item the password.
    Step 3: append the list from Step 2 to the password list


    :param website (string) The website for the entry
    :param password (string) The unencrypted password for the entry
    """
    # First define final result of password_encrypt function
    finalencrypt = password_encrypt(password, encryption_key)
    #Input website and encrypted password into lists, unencrypted passwords do not exist in plain text until unencrypted
    entry = [website, finalencrypt]
    #append the newly assigned entry variable to the entries lists
    entries.append(entry)

def lookup_password(website):
    """Lookup the password for a given website

    Logic for function:
    1. Create a loop that goes through each item in the password list
     You can consult the reading on lists in Week 5 for ways to loop through a list

    2. Check if the name is found.  To index a list of lists you use 2 square backet sets
      So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
      So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
      If you created a loop using the syntax described in step 1, then i is your 'iterator' in the list so you
      will want to use i in your first set of brackets.

    3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
    caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt

     Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
     for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
     you can test easily along the way.

    :param website (string) The website for the entry to lookup
    :return: Returns an unencrypted password.  Returns None if no entry is found
    """
    # Creating a loop that reads through the entries list
    for entry in entries:
        #found is initially set to false because we need to give it a default value
        found = False
        #if given website is found in entries, set found to True
        if entry[0] = website:
            found = True
            break
        #since passwords only exist in the list in encrypted format, we need to decrypt the password to display it
        if found:
            password = password_encrypt(entry[1], -encryption_key)
        else:
            password = None
        # based on the logic of the ceasar cipher, we know it works by shifting the characters used in the unencrypted password by a certain number of positions in the alphabet
         # By using the same logic to decrypt the password, we know to use the negative number of the amount of positions the characters in the original password were shifted

        return password




def delete_password(website):
"""Deletes password from list

Logic for function:

Step 1: Use the given website to read through list of entries to find corresponding password
Step 2: If website exists in entries, delete it along with corresponding password


:param website (string) The website that corresponds with the password user wishes to delete
:return: Confirmation of deletion"""

    # we are going to use a similar for loop here as the lookup_password function uses because we need to read through the entries list
    for entry in entries:
        # setting default of found variable to make this function automatically assume we have not found what we're looking for
        found = False
        # if we find website in entries
        if entry[0] = website:
            found = True
            # contrary to lookup_password function, we need more action after we have determined the given website exists
            while found = True:
                del entries([website, password])
        # if we have not found the given website and combo password in entries, set found to False and set and set an error message
        else:
            found = False

        return


        
while True:
    print(menu_text)
    choice = input()

    if(choice == '1'): # Load the password list from a file
        load_password_file(password_file_name)

    if(choice == '2'): # Lookup at password
        print("Which website do you want to lookup the password for?")
        for key_value in entries:
            print(key_value[0])
        website = input()

        password = lookup_password(website)
        if password:
            print('The password is: ', password)
        else:
            print('Password not found')

    if(choice == '3'): # Add a new entry
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencrypted_password = input()
        add_entry(website, password)

    if(choice == '4'): #Save the passwords to a file
            save_password_file(password_file_name)

    if(choice == '5'): #print out the password list
        for key_value in entries:
            print(', '.join(key_value))

    if(choice == '6'):  #quit our program
        sys.exit()

    # need to call delete_password function here
    if(choice == '7'):  # delete passwords
        delete_password(website)
        if found == True:
            Print("Your password for this website has been deleted")
        else:
            Print("Sorry, that password couldnt be found. Please make sure this is an existing password or that the website name is spelled correctly.")
