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
