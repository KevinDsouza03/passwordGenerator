import function_headers as fh

cont = -1

while cont != 3:
    cont = int(input("Enter 0 to set a password.\nEnter 1 to retrieve a password.\nEnter 2 to delete a password.\nEnter 3 to exit program.\n"))
    if cont == 0:
        fh.generate_store_workflow()
    elif cont == 1:
        fh.retrieve_pass_workflow()
    elif cont == 2:
        fh.deleting_pass_workflow()
    elif cont == 3:
        print("Exiting program.")
    else:
        print("Invalid input. Please enter a valid option.")
