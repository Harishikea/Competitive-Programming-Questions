#CCC '08 J1 - Body Mass Index
#https://dmoj.ca/problem/ccc08j1

weight = float(input())
height = float(input())
bmi = weight/(height*height)

if bmi > 25: 
  print("Overweight")
if bmi < 18.5: 
  print("Underweight")
if bmi>18.5 and bmi<25.0: 
  print("Normal weight")

