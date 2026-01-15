favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

for value in favorite_languages.values():
    print(value.title())

print(favorite_languages.values())
print(favorite_languages.keys())
print(type(favorite_languages.keys()))
print(type(favorite_languages.values()))