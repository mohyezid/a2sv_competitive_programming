def generate_Pattern(rows=int(input("Enter an odd number of row to generate the Pattern: "))):
    
        if rows%2==0:
            print("You Entered even number.Enter an odd num! ")
            
        
        else:
            for i in range(1, rows**2+1):
                if i % 2 == 0:
                    print(" " * 2, end="")
                else:
                    print("#" * 2, end="")

                if i % rows == 0:
                    print()
            
          


if __name__ == "__main__":
    generate_Pattern()
