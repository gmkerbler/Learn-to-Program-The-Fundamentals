##message = 'Happy 29th!'
##new_message = ''
##for char in message:
##    new_message = new_message + str((int(char) + 1) % 10)
##
##print('1st answer', new_message)


message = 'Happy 29th!'
new_message = ''
for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

select_which = False
if new_message == 'Happy 30th!':
    select_which = True
    
print('2nd answer:', new_message, '\nselect:', select_which)

message = 'Happy 29th!'
new_message = ''
for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    new_message = new_message + char

select_which = False
if new_message == 'Happy 30th!':
    select_which = True
    
print('3rd answer:', new_message, '\nselect:', select_which)

message = 'Happy 29th!'
new_message = ''
for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)

select_which = False
if new_message == 'Happy 30th!':
    select_which = True

print('4th answer:', new_message,'\nselect:', select_which) 
