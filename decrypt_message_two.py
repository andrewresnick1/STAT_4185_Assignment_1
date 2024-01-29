encrypted_file = open("C:\\Users\\Andrew\\STAT_4185_Assignment_1\\encrypted_message_two.txt")

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
encrypted_message = list(encrypted_message)
x=0
y=len(encrypted_message)-1

while y>=x: #per instructions on wksht
    if x%2==0: #check if divisible (are we swapping or not)
        encrypted_message[x], encrypted_message[y] = encrypted_message[y], encrypted_message[x] #swap
    #increment
    x+=1
    y-=1
    
output = "".join(encrypted_message)
#I'm not quite sure why, but I reversed the string while unscrambling it. Next line, I reverse it
output = output[::-1]
print(output)