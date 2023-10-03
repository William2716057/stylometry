import nltk
import matplotlib

#prepare data for analysis 

#dictionary where names of authors are keys and paper numbers are values 
papers = {
    'Madison': [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    'Hamilton': [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                 78, 79, 80, 81, 82, 83, 84, 85],
    'Jay': [2, 3, 4, 5],
    'Shared': [18, 19, 20],
    'Disputed': [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
    'TestCase': [64]
}
#function that takes all text associated with an author into one string
def readFilesToString(filenames):
    strings = []
    for filename in filenames:
        with open(f'stylometry-federalist/data/federalist_{filename}.txt', 'r') as f:
            strings.append(f.read())
    return '\n'.join(strings)

#build data structure by calling readFilesToString function and passing it to different list of papers each time
#then store results into other dictionary 

#create dictionary from author's collection of texts 
federalistByAuthor = {}
for author, files in papers.items():
    federalistByAuthor[author] = readFilesToString(files)

for author in papers:
    print(federalistByAuthor[author][:100])
