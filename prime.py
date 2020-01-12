divisors = []
while True:
    try:
        num = int(input("Give me a number and I will tell you if it's prime: "));

    except ValueError:
        print("You need to input a number! \n")
        continue
    if num == 1:
        print("1 is not a prime number! \n")
        
    else:
        for i in range(1, (num + 1)):
            if num % i == 0:
                divisors.append(i)
                
        if divisors == [1, num]:
            print("Prime! \n")
            
        else:
            print("Not prime.")
            print(str(num) + " has non trivial divisors: " + str(divisors[1:len(divisors)-1]) + "\n")
            
    divisors=[]
