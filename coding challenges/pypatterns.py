# printing stars in odd number format



def right_triangle(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print('*', end='')
        print('\r')
        


# right_triangle(5)

def left_triangel(n):
    # set the number of spaces
    s = 2*n-2
    for i in range(0,n):
        
        # inner loop to handle spaces
        for j in range(0, s):
            print(end=' ')
            
        # decrease space by 2 after each row loop will give a left-facing triangle
        # decrease by 1 will give a proper traingle.
        s-=1
        
        # inner loop to handle cols
        for k in range(0,i+1):
            print('* ', end='')
        print('\r')
            
# left_triangel(5)


