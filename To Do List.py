firstprio = None
secondprio = None
thirdprio = None
fourthprio = None
fifthprio = None

firstprio = input("What is your #1 priority for your list?   " )

secondprio = input( "What is your #2 priority for your list?  "  )

thirdprio = input("What is your #3 priority for your list?:  " )


fourthprio = input("What is your #4 priority for your list? (If you don't have one, enter 'None'):   " )
if fourthprio != 'None':
  fifthprio = input("What is your #5 priority for your list? (If you don't have one, enter 'None'):   " )
else:
    pass



#complete list
if fourthprio and fifthprio != 'None':
    final_list = (f"Your To-Do List is:\n1. {firstprio}\n2. {secondprio}\n3. {thirdprio} \n4. {fourthprio} \n5. {fifthprio} \n")
if fifthprio  == 'None':
    final_list = (f"Your To-Do List is:\n1. {firstprio}\n2. {secondprio}\n3. {thirdprio} \n4. {fourthprio}\n")
if fourthprio == 'None':
    final_list = (f"Your To-Do List is:\n1. {firstprio}\n2. {secondprio}\n3. {thirdprio}\n") 

print(final_list)
    
                