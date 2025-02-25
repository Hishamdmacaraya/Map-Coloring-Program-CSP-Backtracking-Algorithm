# Map Coloring CSP Project

## Overview

This project implements a **Constraint Satisfaction Problem (CSP) solver** for the classic map coloring problem using a **backtracking algorithm** in Python. The goal is to assign the minimum number of colors (from a fixed set of seven: red, green, blue, yellow, violet, gray, orange) to the regions (vertices) of a map so that no two adjacent regions share the same color. The program reads a graph from an input file (`graph.txt`), represents the map as an adjacency list, and then uses backtracking with constraint checking to find a valid coloring. If the map cannot be colored using 7 colors, the program outputs "Not possible with 7 colors."

## Project Structure

- **graph.txt**: The input file containing the graph data.
  - The first line indicates the total number of vertices.
  - Each subsequent line lists a vertex followed by its adjacent vertices, separated by spaces.
- **map_coloring.py**: The main Python script that implements the CSP backtracking algorithm.
- **README.md**: This file, providing an overview and instructions for the project.

## Requirements

- Python 3.x
- A text editor or IDE for viewing/editing the Python code
- The `graph.txt` input file must be placed in the same directory as `map_coloring.py` (or modify the file path accordingly).

## How to Run

1. **Ensure Python is installed on your system.**  
   Check your Python version by running:
   ```bash
   python --version

2. Place graph.txt in the same directory as map_coloring.py.

3. Run the script from the command line:
   
```
python map_coloring.py
```

The program will read the graph from graph.txt, attempt to color it using a backtracking algorithm, and print the color assigned to each vertex. If the map cannot be colored with 7 colors, it will output:

```
Not possible with 7 colors
```


Input File Format
The input file (graph.txt) must be structured as follows:

First Line: A single integer representing the total number of vertices (e.g., 5).

Subsequent Lines: Each line represents a vertex and its adjacent vertices, separated by spaces.

Example

```
5
A B C D
B A C
C A B D
D A C
E
```

- Vertex A is adjacent to B, C, and D.
- Vertex B is adjacent to A and C.
- Vertex C is adjacent to A, B, and D.
- Vertex D is adjacent to A and C.
- Vertex E has no adjacent vertices.


Output
If a valid coloring is found:
The program prints each vertex along with its assigned color, one per line. For example:

```
A red
B green
C blue
D green
E red
```

If the map cannot be colored with 7 colors:
The program outputs:
```
Not possible with 7 colors
```

CSP Backtracking Algorithm
The project uses a backtracking algorithm to solve the map coloring CSP. The key steps include:

Reading the Input:
The program reads the graph from graph.txt and creates an adjacency dictionary.

Constraint Checking:
For each vertex, the algorithm checks whether a proposed color is valid (i.e., it does not conflict with adjacent vertices).

Recursive Assignment:
Colors are assigned recursively using a backtracking approach. If an assignment leads to a conflict, the algorithm backtracks and tries a different color.

Output Generation:
Once a valid solution is found or all possibilities are exhausted (up to 7 colors), the program outputs the results accordingly.

References
Poole, D. L., & Mackworth, A. K. (2017). Artificial Intelligence: Foundations of Computational Agents. Cambridge University Press. Retrieved from https://artint.info/2e/html/ArtInt2e.html










