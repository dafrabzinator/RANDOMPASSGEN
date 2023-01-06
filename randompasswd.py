import random
import math

alphabets = "abcdefghijklmnopqrstuvwxyz"
numerical_values = "0123456789"
special_characters = "@#$%*"

pass_len = int(input('Enter your password Length:   '))

#length of password by 50-30-20 formula

alpha_len = pass_len//2
num_len = math.ceil(pass_len*30/100)
special_len = pass_len-(alpha_len + num_len)

password = []

def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        Character = array[index]
        if is_alpha:
            Case = random.randint(0, 1)
            if Case == 1:
                Character = Character.upper()
        password.append(Character)

#alpha password
generate_pass(alpha_len, alphabets, True)
#NUMERIC password
generate_pass(num_len, numerical_values)
#special character password
generate_pass(special_len, special_characters)
#shuffle the generated password
random.shuffle(password)
#convert list to string
gen_password = "" 
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)