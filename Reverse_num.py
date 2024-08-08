def reverse_number(n):
    reverse_num = 0
    while n > 0:
        last_digit = n % 10
        reverse_num = reverse_num * 10 + last_digit
        n = n // 10
    return reverse_num


print(reverse_number(12345))



#def reverse_number(n):
    #reversed_num = 0
    #while n > 0:
        # Get last digit and remove it from n in a single line
        #last_digit, n = n % 10, n // 10
        
        # Append last_digit to reversed_num
        #reversed_num = reversed_num * 10 + last_digit

    #return reversed_num
