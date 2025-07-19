def read_data(a):
    mydictionary = {}
    kitta_no = 101  # Start kitta number from 100
    with open(a, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            mydictionary[kitta_no] = line.split(',')
            kitta_no += 1  # Increment kitta number for each line
    return mydictionary
