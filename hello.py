                   #print("Enter your name:")
#x = input()
#print("Hello, " + x)

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)         # Prints complete list
print (list[0])     # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist)
str="ashok"
print(str*2)
for c in list:
    print (c)
    import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
a=[10,20,'dklj']
print(a)
for x in a:
    print (x)
    if x==10:
        continue
    print("continue")
L1=['apple',1,2,3]
[L1[i]  for i in (1,2,3)]
print(L1)

Dict={"Name":"ashok",
      "age":27,
      "phone":7795801335
      }

print(Dict)
def test():
    print("Hi")
    age=input("enter your age")
    print(age)
    age=int(age)
    if (age>=18):
        print("eligible to vote")
        
test()
l=range(1,20)
for x in l:
   print(x)
   
text = "hello cruel world. This is a sample text"
d = dict.fromkeys(text, 0)
for c in text: 
    d[c] += 1
    print(c)
    

def first_repeated_word(str1):
  temp = []
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.append(word)
  return 'None'
print(first_repeated_word("ab ca bc ab"))
print(first_repeated_word("ab ca bc ab ca ab bc"))
print(first_repeated_word("ab ca bc ca ab bc"))
print(first_repeated_word("iloveappleandapplemacbook"))

str="ashok"
print(''.join(reversed(str)))
   
        