# 1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print('original:', x)
x[1][0] = 15
print('altered:', x)
print('original:', students)
students[0]['last_name'] = 'Bryant'
print('altered:', students)
print('original:', sports_directory)
sports_directory['soccer'][0] = 'Andres'
print('altered:', sports_directory)
print('original:', z)
z[0]['y'] = 30
print('altered:', z)

# 2
students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(li):
    fn = 'first_name -'
    ln = 'last_name -'
    '''print(type(li))
    print(li[0])
    print(li[0]['first_name'])'''
    i = 0
    while i < len(li):
        first = li[i]['first_name']
        last = li[i]['last_name']
        print(fn, str(first) + ',', ln, str(last))
        i += 1

iterateDictionary(students)

