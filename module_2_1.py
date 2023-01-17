def get_matrix(n_rows, n_col):
    matrix = []
    for i in range(n_rows):
        matrix.append([])
        for j in range(n_col):
            matrix[i].append(i+j)
    
    return matrix


def function(first_name, last_name):
    greeting = f"Hello, {first_name} {last_name}"
    
    return greeting

if __name__ =='__main__':

    matrix = get_matrix(5,5)
    print(matrix)
    sentence = "HELLO THERE!"
    lowercase_sentence = sentence.lower()
    sentence = "Some pie please!"
    print(lowercase_sentence)

    
    first_name = 'Jon'
    last_name = 'Sistiaga'
    print(function(first_name, last_name))

    print('5.0'.isnumeric())