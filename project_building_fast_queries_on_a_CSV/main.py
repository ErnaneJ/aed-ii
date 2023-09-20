import csv
from tabulate import tabulate

def row_price(row):
    """
    Helper function to extract the price from a row.
    
    Args:
        row (list): A list representing a laptop with attributes, where the last element is the price.
    
    Returns:
        int: The price of the laptop.
    """
    return row[-1]

class Inventory:
    def __init__(self, csv_filename):
        """
        Initialize the Inventory class with data from a CSV file.

        Args:
            csv_filename (str): The path to the CSV file containing laptop inventory data.
        """
        with open(csv_filename) as f:
            reader = csv.reader(f)
            rows = list(reader)

        # Extract the header and rows from the CSV file
        self.header = rows[0]
        self.rows = rows[1:]

        # Convert the last element (price) of each row to an integer
        for row in self.rows:
            row[-1] = int(row[-1])

        # Create a dictionary mapping laptop IDs to their corresponding rows
        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row

        # Create a set of unique laptop prices
        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])

        # Sort the rows by price for efficient searching
        self.rows_by_price = sorted(self.rows, key=row_price)

    def get_laptop_from_id(self, laptop_id):
        """
        Get laptop information by its ID using a linear search.

        Args:
            laptop_id (str): The ID of the laptop to retrieve.

        Returns:
            list or None: A list representing the laptop with attributes, or None if not found.
        """
        for row in self.rows:
            if row[0] == laptop_id:
                return row
        return None

    def get_laptop_from_id_fast(self, laptop_id):
        """
        Get laptop information by its ID using a dictionary lookup for faster retrieval.

        Args:
            laptop_id (str): The ID of the laptop to retrieve.

        Returns:
            list or None: A list representing the laptop with attributes, or None if not found.
        """
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):
        """
        Check if there is a laptop with a given price or a combination of two laptops' prices that equals the given dollars.

        Args:
            dollars (int): The target price to check.

        Returns:
            bool: True if a laptop or combination of laptops match the target price, False otherwise.
        """
        for row in self.rows:
            if row[-1] == dollars:
                return True
        for row1 in self.rows:
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False

    def check_promotion_dollars_fast(self, dollars):
        """
        Check if there is a laptop with a given price or a combination of two laptops' prices that equals the given dollars using a set for faster lookup.

        Args:
            dollars (int): The target price to check.

        Returns:
            bool: True if a laptop or combination of laptops match the target price, False otherwise.
        """
        if dollars in self.prices:
            return True
        for price in self.prices:
            if dollars - price in self.prices:
                return True
        return False

    def find_laptop_with_price(self, target_price):
        """
        Find the index of a laptop with the given target price using binary search.

        Args:
            target_price (int): The target price to search for.

        Returns:
            int: The index of the laptop in the sorted list, or -1 if not found.
        """
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:
                return range_middle
            elif value < target_price:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if self.rows_by_price[range_start][-1] != target_price:
            return -1
        return range_start

    def find_first_laptop_more_expensive(self, target_price):
        """
        Find the index of the first laptop with a price higher than the given target price using binary search.

        Args:
            target_price (int): The target price to search for.

        Returns:
            int: The index of the first laptop with a price higher than the target price, or -1 if not found.
        """
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:
            return -1
        return range_start

    def find_laptops_in_price_range(self, min_price, max_price):
        """
        Find laptops within a specified price range using binary search.

        Args:
            min_price (int): The minimum price of the price range.
            max_price (int): The maximum price of the price range.

        Returns:
            list: A list of laptops that are within the specified price range.
                  Each laptop is represented as a list of attributes, where the last
                  element of the list is the price.
        """
        laptops_in_range = []
        for laptop in self.rows_by_price:
            price = laptop[-1]
            if min_price <= price <= max_price:
                laptops_in_range.append(laptop)
            elif price > max_price:
                break

        return laptops_in_range

    def find_laptops_with_features(self, features, MAX_RESULTS=None):
        """
        Find laptops with specific features based on a dictionary of feature criteria.

        Args:
            features (dict): A dictionary of feature criteria, where keys are attribute names and values are desired values.

        Returns:
            list: A list of laptops that match the specified feature criteria.
                Each laptop is represented as a list of attributes, where the last
                element of the list is the price.
        """
        matching_laptops = []

        for row in self.rows:
            is_match = True
            for key, value in features.items():
                if key in self.header and str(row[self.header.index(key)]) != str(value):
                    is_match = False
                    break

            if is_match:
                matching_laptops.append(row)
                if(MAX_RESULTS) and len(matching_laptops) >= MAX_RESULTS:
                    break

        return matching_laptops

if __name__ == "__main__":
    inventory = Inventory("project_building_fast_queries_on_a_CSV/laptops.csv")

    min_price, max_price = 100, 200
    laptops_range = inventory.find_laptops_in_price_range(min_price, max_price)

    print(f"\n.:: {len(laptops_range)} laptops were found with prices between R$ {min_price} and R$ {max_price}.")
    print(f"\n{tabulate(laptops_range, headers=inventory.header)}\n")

    desired_features = { 
        'Ram': '8GB',
        'Memory': '256GB SSD',
    }

    matching_laptops = inventory.find_laptops_with_features(desired_features, 1)

    print(f"\n.:: {len(matching_laptops)} laptops were found with the reported configurations.")
    print(f"\n{tabulate(matching_laptops, headers=inventory.header)}\n")
