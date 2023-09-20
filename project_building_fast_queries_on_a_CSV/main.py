import csv
import re

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def row_price(row):
    return row[-1]

class Inventory():                    
    def __init__(self, csv_filename):
      with open(csv_filename) as f: 
        reader = csv.reader(f)
        rows = list(reader)
      self.header = rows[0]        
      self.rows = rows[1:]
      for row in self.rows:              
        row[-1] = int(row[-1])
      self.id_to_row = {}                        
      for row in self.rows:                       
        self.id_to_row[row[0]] = row
      self.prices = set()                          
      for row in self.rows:                        
        self.prices.add(row[-1])
      self.rows_by_price = sorted(self.rows, key=row_price)

      self.all_features = {}
      for key in self.header:
        self.all_features[key] = [str(row[self.header.index(key)]).lower() for row in self.rows_by_price]
    
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:                 
            if row[0] == laptop_id:
                return row
        return None   
    
    def get_laptop_from_id_fast(self, laptop_id):  
        if laptop_id in self.id_to_row:           
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):    
        for row in self.rows:                   
            if row[-1] == dollars:
                return True
        for row1 in self.rows:                  
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False                        
    
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:                   
            return True
        for price in self.prices:                    
            if dollars - price in self.prices:
                return True
        return False                                
    
    def find_laptop_with_price(self, target_price):
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
    
    def find_first_laptop_more_expensive(self, target_price): # Step 2
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
      Finds laptops within a specified price range. With binary Search.

      Args:
          min_price (float): The minimum price of the price range.
          max_price (float): The maximum price of the price range.

      Returns:
          list: A list of laptops that are within the specified price range.
                Each laptop is represented as a list of attributes, where the last
                element of the list is the price.
      """
        
      laptops_in_range = []
      range_start = 0
      range_end = len(self.rows_by_price) - 1
      
      while range_start <= range_end:
          range_middle = (range_end + range_start) // 2
          laptop = self.rows_by_price[range_middle]
          price = laptop[-1]
          
          if min_price <= price <= max_price:
              laptops_in_range.append(laptop)
          
          if price < min_price:
              range_start = range_middle + 1
          else:
              range_end = range_middle - 1
      
      return laptops_in_range
    
    def find_laptops_with_features(self, features):
      """
      Finds laptops with specific features.

      Args:
          features (dict): A dictionary specifying the desired laptop features.
                          Supported keys: ['Id', 'Company', 'Product', 'TypeName', 'Inches',
                          'ScreenResolution', 'Cpu', 'Ram', 'Memory', 'Gpu', 'OpSys',
                          'Weight', 'Price']. Any other keys are ignored.

      Returns:
          list: A list of laptops that match the specified features. Each laptop is represented
                as a list of attributes, where the last element of the list is the price.
      """
      matching_laptops = []  # Initialize a list to store laptops that match the features
      range_start = 0        # Initialize the start of the search range
      range_end = len(self.rows_by_price) - 1  # Initialize the end of the search range
      
      while range_start <= range_end:
          range_middle = (range_end + range_start) // 2  # Calculate the midpoint of the range
          laptop = self.rows_by_price[range_middle]     # Get the laptop at the midpoint
          price = laptop[-1]                            # Get the price of the laptop
          
          # Check if the laptop matches the specified features efficiently
          match = all(key in self.header and laptop[self.header.index(key)] == value for key, value in features.items())
          
          # If the laptop matches the features, add it to the list
          if match:
              matching_laptops.append(laptop)
          
          # Update the search range boundaries based on the laptop's price
          if price < laptop[-1]:
              range_start = range_middle + 1
          else:
              range_end = range_middle - 1
      
      return matching_laptops  # Return the list of laptops that match the specified features

    def get_desired_features_by_str(self, sentence):
      stop_words = set(stopwords.words('portuguese'))

      sentence = sentence.lower()
      words.replace(" ssd", "-ssd")

      words = sentence.split(' ')
      filtered_words = [word for word in words if word not in stop_words]

      desired_features = {}

      print(self.rows_by_price[0])
      print(filtered_words)

      for feature in self.header:
        for word in filtered_words:
            if(word in self.all_features[feature]):
                desired_features[feature] = word

      print(desired_features)
      

inventory = Inventory('project_building_fast_queries_on_a_CSV/laptops.csv')

desired_features = {
  'Company': 'Acer',
}

print(inventory.get_desired_features_by_str('computador acer com 256gb de ram e 1TB HD'))