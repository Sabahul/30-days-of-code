'''the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string
 String traversal will take place from left to right, not from right to left'''

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        for j in range(len(sub_string)):
            if string[i+j]==sub_string[j] and j==(len(sub_string)-1):
                count=count+1  
            if string[i+j]!=sub_string[j]:
                break  
        if i==len(string)-len(sub_string):
            break            
    return count
