input_len = int(input())
sixteen = 16 * (input_len/9) 
nine = 9 * (input_len/16) 
four = 4 * (input_len/3)
three = 3 * (input_len/4) 
print(f'{sixteen:06.2f} : {input_len:06.2f}  |  {input_len:06.2f} : {nine:06.2f}')
print(f'{four:06.2f} : {input_len:06.2f}  |  {input_len:06.2f} : {three:06.2f}')