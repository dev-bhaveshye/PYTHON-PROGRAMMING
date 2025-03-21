name = input("enter name ")
date = input ("enter date ")
print( f"congratulations {name}\n you are selected\n{date} ")

letter = '''dear <| name |>,
you are selected 1
<|date|> ''' 
print(letter.replace("<| name |>" , "bhavesh").replace("<|date|>bhavesh", "17 nov bhavesh" ))