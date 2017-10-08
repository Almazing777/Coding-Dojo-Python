context = {
    "info":[
        {"My name is": "Almas"},
        {"My age is": 28},
        {"My country of birth is": "Uzbekistan"},
        {"My favorite language is": "Python"}
    ]
}

for key, data in context.items():
    for value in data:
        print value