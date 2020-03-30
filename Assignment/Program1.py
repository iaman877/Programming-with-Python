# Write Python program to sort words in a sentence in decreasing order of their length.
#  Display the sorted words along with their length

def sortedfunction(String): 
	a = String.split(" ")                    # Splitting the String into words
	a.sort(reverse=True)                      # Sorting the words 
	return a               

String = "Programmng with python"
print(sortedfunction(String), end = ' ')       # Print the sortedSentence
print(len(String))
String = "Aman Bhardwaj"
print(sortedfunction(String), end = ' ')       # Print the sortedSentence
print(len(String))
