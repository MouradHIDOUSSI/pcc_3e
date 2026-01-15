favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:")

# looping through unique values only
for language in set(favorite_languages.values()):
    print(language.title())

