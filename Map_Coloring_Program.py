# Map Coloring Program using CSP Backtracking Algorithm
# This program reads a graph from an input file (graph.txt) and attempts to color the map
# using a minimum number of colors (up to 7) such that no two adjacent regions share the same color.

import sys

# List of available colors in the required order
AVAILABLE_COLORS = ["red", "green", "blue", "yellow", "violet", "gray", "orange"]

def can_color(vertex, color, adjacency, color_assignments):
    """
    Determines whether the given 'color' can be assigned to 'vertex'
    without violating the constraint that adjacent vertices must not share the same color.
    
    Parameters:
    - vertex: The current vertex we are trying to color.
    - color: The color we wish to assign.
    - adjacency: A dictionary mapping vertices to a list of adjacent vertices.
    - color_assignments: A dictionary mapping vertices that have already been colored.
    
    Returns:
    - True if 'color' can be assigned to 'vertex'; False otherwise.
    """
    for neighbor in adjacency[vertex]:
        if neighbor in color_assignments and color_assignments[neighbor] == color:
            return False  # Adjacent vertex already has this color
    return True

def backtrack(vertices, index, adjacency, color_assignments, max_colors):
    """
    Recursively assigns colors to vertices using a backtracking approach.
    
    Parameters:
    - vertices: List of all vertices (nodes) in the graph.
    - index: Current index in the vertices list to assign a color.
    - adjacency: Dictionary mapping each vertex to its list of adjacent vertices.
    - color_assignments: Dictionary holding the current color assignment for vertices.
    - max_colors: The maximum number of colors allowed (from AVAILABLE_COLORS).
    
    Returns:
    - True if a valid coloring is found; False if no valid assignment is possible.
    """
    # Base case: All vertices have been colored successfully.
    if index == len(vertices):
        return True

    vertex = vertices[index]
    # Try each color available up to the given max_colors
    for c in range(max_colors):
        color = AVAILABLE_COLORS[c]
        # Check if the current color is valid for the vertex
        if can_color(vertex, color, adjacency, color_assignments):
            color_assignments[vertex] = color  # Assign the color to the vertex
            # Recursively assign colors to the next vertex
            if backtrack(vertices, index + 1, adjacency, color_assignments, max_colors):
                return True
            # If not valid further down, remove the assignment (backtrack)
            del color_assignments[vertex]

    # No valid color assignment found for this vertex at the current max_colors level
    return False

def solve_map_coloring(filename="graph.txt"):
    """
    Reads the graph from the specified input file and attempts to color the map with the minimum number of colors.
    
    The program:
    - Reads the total number of vertices.
    - Constructs an adjacency dictionary representing the map.
    - Tries to color the graph with increasing numbers of colors (from 1 to 7).
    - Prints the vertex color assignments if a valid coloring is found.
    - If no solution is found using up to 7 colors, outputs "Not possible with 7 colors".
    
    Parameters:
    - filename: The name of the file containing the graph data.
    """
    try:
        # Open and read the input file
        with open(filename, "r") as file:
            # First line contains the total number of vertices
            total_vertices = int(file.readline().strip())
            adjacency = {}  # Dictionary to store the graph's adjacency list
            vertices = []   # List to store vertices in the order they appear

            # Read each subsequent line, each representing a vertex and its adjacent vertices
            for _ in range(total_vertices):
                line = file.readline().strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split()
                vertex = parts[0]
                vertices.append(vertex)
                # Remaining parts are the adjacent vertices; if none, assign an empty list
                adjacency[vertex] = parts[1:] if len(parts) > 1 else []

        # Try coloring using 1 to 7 colors; stop when a valid solution is found
        for color_count in range(1, 8):
            color_assignments = {}  # Dictionary to store the current color assignment for each vertex
            if backtrack(vertices, 0, adjacency, color_assignments, color_count):
                # Valid coloring found; print each vertex and its assigned color
                for v in vertices:
                    print(v, color_assignments[v])
                return  # Exit after successful coloring

        # If no valid coloring found with 7 colors, output appropriate message
        print("Not possible with 7 colors")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please verify the file exists in the project directory.")
    except ValueError:
        print("Error: Invalid input format. Ensure the file contains correct vertex and adjacency information.")

# Main execution: Run the map coloring solver when the script is executed directly
if __name__ == "__main__":
    solve_map_coloring("graph.txt")
