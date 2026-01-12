# Copilot Instructions for Python Crash Course, 3rd Edition

## Project Overview

This is the official repository for **Python Crash Course, 3rd Edition** by Eric Matthes—an introductory programming textbook published by No Starch Press. It contains progressive, hands-on code examples organized by chapter, spanning foundational Python concepts through data visualization and web APIs.

**Not a production codebase.** This is educational material where each chapter's files demonstrate specific Python concepts. Code prioritizes clarity and teaching value over optimization.

## Directory Structure & Purpose

- **chapter_01 to chapter_20**: Progressive lessons, each adding complexity
  - Chapters 1-11: Core Python (basics, functions, classes, testing)
  - Chapters 12-14: Pygame-based "Alien Invasion" game project
  - Chapters 15-16: Data visualization with Matplotlib
  - Chapters 17-20: Working with APIs, data analysis, and web applications

- **partial_programs/**: Incomplete code snippets used in textbook walkthroughs
- **solution_files/**: Complete solutions for end-of-chapter exercises (mirrors chapter structure)
- **cheat_sheets/**: Quick reference guides for Python concepts
- **online_resources_site/**: Web server example project

## Key Patterns & Conventions

### 1. **Minimal Dependencies**
- Most chapters use only the Python standard library
- Chapters 12-14 require `pygame` for the game project
- Chapters 15-16 require `matplotlib` for plotting
- Chapters 17+ require `requests` for API calls and `plotly` for interactive visualizations

### 2. **Docstring Style**
Follows PEP 257 with descriptive docstrings on all classes and methods:
```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
```

### 3. **Class-Based Organization (Chapters 9+)**
Projects use class hierarchies with inheritance:
- `Car` base class with `ElectricCar` subclass (chapter 9)
- `AlienInvasion` main controller class managing game resources (chapters 12-14)
- Separate `Settings` class for configuration (chapter 12)
- Sprite subclasses extending `pygame.sprite.Sprite` (chapters 13+)

### 4. **Testing with pytest (Chapter 11)**
Tests follow naming convention `test_*.py` with functions like `test_*`:
```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

### 5. **Game Project Structure (Chapters 12-14)**
The Alien Invasion game evolves progressively with clear separation:
- **Chapter 12**: Basic `AlienInvasion` class with main game loop and `Settings` configuration
- **Chapter 13**: Sprite classes (`Ship`, `Alien`, `Bullet`) added; `pygame.sprite.Group` for managing game objects
- **Chapter 14**: Game state (levels, scoring) integrated into main class

Key pattern:
```python
class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(...)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Handle events, update, draw
```

## Data Visualization & File I/O

### Chapters 10: File I/O
Uses `pathlib.Path` for file operations:
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
```

### Chapters 15: Matplotlib Line & Scatter Plots
Basic charting with `matplotlib`:
```python
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.tick_params(labelsize=14)
plt.show()
```

### Chapter 16: CSV Data & Visualization
Combines CSV parsing with datetime handling:
```python
from pathlib import Path
import csv
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
```

## API Integration & Web Data

### Chapter 17: Working with APIs
Pattern for HTTP requests with error handling:
```python
import requests
import json

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
```

### Chapter 17+: Interactive Visualization with Plotly
Modern alternative to static plots:
```python
import plotly.express as px

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels)
fig.update_layout(title_font_size=28)
fig.show()
```

## Solution Files

Located in `solution_files/`, organized by chapter. Solutions follow these patterns:
- **Simple solutions** (chapters 2-5): Single files addressing specific exercises
- **Multi-file solutions** (chapters 9+): Complete implementations with proper class structure
- Example structure: `solution_files/chapter_02/famous_quote.py` solves chapter 2 exercise questions
- Solutions maintain same coding style as main chapter examples but are complete end-to-end implementations

## Running Code

- **Simple scripts**: `python filename.py`
- **Test files**: `pytest` or `python -m pytest` (requires pytest installation)
- **Game project** (chapter 12+): `python alien_invasion.py` from the chapter directory (requires `pygame`)
- **Data visualization** (chapter 15+): `python filename.py` (requires `matplotlib`; interactive plots with `plotly` open in browser)
- **API examples** (chapter 17+): `python filename.py` (requires `requests`; may need API rate limits)

## Important Notes for Contributors

1. **Preserve Educational Intent**: Changes should maintain the progressive, chapter-by-chapter learning path
2. **Keep Code Simple**: Avoid refactoring for efficiency if it obscures teaching concepts
3. **Maintain Docstrings**: Every class and method should have a descriptive docstring
4. **Separate Concerns**: Each file typically demonstrates one concept or project phase
5. **Test-Driven Approach** (Chapter 11+): Testing is introduced progressively; earlier chapters don't include tests
6. **Gradual Complexity**: Game project gets more complex (chapter 12 → 13 → 14); maintain this incremental growth

## Cross-File Dependencies

- `chapter_12+`: Importing from `settings.py` for game configuration (centralized approach)
- `chapter_09+`: File imports within same directory (e.g., `from car import Car`)
- `chapter_10+`: File I/O operations with data in local directories (e.g., `pi_digits.txt`)
- `chapter_13+`: Game project splits into multiple sprite classes; main class imports them
- `chapter_16+`: CSV files stored in subdirectories (e.g., `weather_data/`); use relative paths with `Path`
