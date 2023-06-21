import pandas as pd

print("""
      Welcome to a grade marking program using python and the pandas module! If you want to use it here are the steps:
      #1 : drop your excel file in the file of the program
      #2 : input the name of your excel file
      #3 : input the name of which column you want to calculate (has to be a column that contains integers not letters!)
      """)


file_name = input("Type in the name of your excel file: ")
file = (file_name + '.xlsx')
grades = pd.read_excel(file)

while True:
      choice1 = input("""
                If you want to get a specific class average then type in 1, however if you want to get all the class averages type in 2 or 'quit' to exit
                """)      

      if choice1  == "1":
            choice1_2 = input("Type in the subject you want to get the class average of(caps sensitive): ")
            subject = choice1_2
            class_average = grades[subject].mean()
            print(class_average)
            continue
      
      elif choice1 == "2":
            choice_col1 = input("Type in the first class(first column you want to include)(caps sensitive): ")
            choice_col2 = input("Type in the last class(last column you want to include)(caps sensitive): ")
            student_average = grades[[choice_col1, choice_col2]].mean(axis=1)
            print(student_average)
            continue
      
      elif choice1 == "quit":
            quit()
            
      else:
            print("Please only type in yes or no")
            choice1 = input("""
                If you want to get a specific class average then type in 1, however if you want to get all the class averages type in 2
                """)
      