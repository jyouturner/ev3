print('hello')
print('world')

def write_to_file(whateverToWrite):
    print('start')


write_to_file('hello')
write_to_file('world')

#
# a function to print out input message
#
def show_message(whateverToSay1, whateverToSay2):
    print(whateverToSay1)
    print(whateverToSay2)

show_message('hello', 'there')
show_message('welcome', 'here')

user_input = 2

if user_input == 1:
    print('you select the first option')
elif user_input == 2:
    print('you select the second option')
elif user_input == 3:
    print('you selected the third option')
else:
    print('bye')
