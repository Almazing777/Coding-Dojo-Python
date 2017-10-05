mixed_list = ['magical unicorns ',19,'hello ',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ['magical ','unicorn']

def identify_list_type(first):
    new_string = ''
    sum = 0

    for value in first:
        if isinstance(value, int) or isinstance(value, float):
            sum += value
        elif isinstance(value, str):
            new_string += value

    if new_string and sum:
        print "The list you entered is of mixed type"
        print "String:", new_string
        print "Sum:", sum

    elif new_string:
        print "The list you entered is of string type"
        print "String:",new_string

    else:
        print "The list you entered is of integer type"
        print "Sum:", sum

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)