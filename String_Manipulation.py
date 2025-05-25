print("Hello World!\nHello World!")

a = "Hello"
b = "World"
# String concatenation and repetitions
print("a" + " " + "b")
print(a * 3)

# String slicing
s = "python"
print(s[0:2])
print(s[::2]) # Every second character
print(s[::-1]) # reversed 

# Loop through a string
s = "HI"
for ch in s:
    print(ch)

# String methods
s = "  Python Is Awesome!  "
print(s.lower()) # lower letter
print(s.strip()) # remove the space
print(s.replace("Awesome", "Great"))
print(s.split())

# Check palindrome
s = "madam"
if s == s[::-1]:
    print("Pallindrome!")
else:
    print("Not a palindrome!")


