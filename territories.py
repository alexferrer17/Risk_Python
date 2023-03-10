class Territories:

    def read_adjacency_list(self, filename):
        """
        Reads the adjacency list from a file and returns it as a dictionary.
        Parameters:
            filename (str): The name of the file to read.
        Returns:
            A dictionary representing the adjacency list. The keys are the names of
            territories and the values are lists of the names of adjacent territories.
        """
        adjacency_list = {}
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(':')
                if len(data) == 2:
                    territory = data[0]
                    adjacents = data[1].split(',')
                    adjacency_list[territory] = adjacents
        return adjacency_list

    def is_adjacent(self, territory1, territory2, adj_list):
        """
        Checks if territory1 is adjacent to territory2 based on the adjacency list.
        Args:
            territory1 (str): The name of the first territory.
            territory2 (str): The name of the second territory.
            adj_list (dict): The adjacency list data structure.
        Returns:
            bool: True if territory1 is adjacent to territory2, False otherwise.
        """
        if territory1 in adj_list and territory2 in adj_list[territory1]:
            return True
        elif territory2 in adj_list and territory1 in adj_list[territory2]:
            return True
        else:
            return False
    def get_adjacent_territories(self, filename, territory):
        """
        Returns a list of adjacent territories for the given territory based on the adjacency list.
        Args:
        territory (str): The name of the territory.
        Returns:
        A list of the names of adjacent territories.
        """
        return self.read_adjacency_list(filename).get(territory, [])
