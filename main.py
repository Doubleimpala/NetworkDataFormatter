import json

# Initialize empty lists to store the questions and answers
questions = []
answers = []

# Initialize an empty list to store the pairs
pairs = []
n=0
# Open the input file
with open('input.txt', 'r') as f:
  
    # Read each line of the file
    for line in f:
        
       
        # Split the line into a list of fields using the tab character as the delimiter
        fields = line.split('\t')
        
        # Ignore the line if it doesn't have at least two fields
        if len(fields) < 2:
            continue
        
        # Extract the first two fields (the question and the answer)
        question = fields[0]
        answer = fields[1]
        
        # Check if the question is already in the list of questions
        if question in questions:
            # Find the index of the question in the list
            index = questions.index(question)
            
            # Append the answer to the existing answer at the same index
            answers[index] += ' ' + answer
        else:
            # Add the question and answer to the appropriate lists
            questions.append(question)
            answers.append(answer)

# Iterate over the questions and answers
for i in range(len(questions)):
    n= n+1
    # Create a dictionary for the current question and answer
    pair = {
        "tag": "jhdjhfwq" + str(n),
        "patterns": [questions[i]],
        "responses": [answers[i]],
        "context_set": ""
    }
    
    # Add the dictionary to the list of pairs
    pairs.append(pair)

# Open the output file
with open('output.json', 'w') as f:
    # Write the list of pairs to the output file as JSON
    json.dump(pairs, f, indent = 2)
