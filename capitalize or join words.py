def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particualr character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """
    # your code here
    if sentence.startswith('*'):
       s = sentence.replace('*','')
       
       s2 = s.split()
    
       s3 = []
       for i in s2:
           s3 +=  i[0].upper()+ i[1:-1]+ i[-1].upper()+" "
           print(s3)
       s4="".join(s3)
       s5=s4[1:-1]
       sentence_revised =s5
    
    else:
    
      s = sentence.split()
      print(s)
      sentence_revised = ",".join(s)
    return sentence_revised
string="*i love python"
print (capitalize_or_join_words(string))
