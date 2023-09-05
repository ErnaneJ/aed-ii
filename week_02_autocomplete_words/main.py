from AVLTree import AVLTree
from AutocompleteWords import AutocompleteWords
import time

def build_structures(autocomplete):
  """
  Builds data structures for autocomplete functionality.

  Args:
    autocomplete (AutocompleteWords): An instance of the AutocompleteWords class.

  Returns:
    tuple: A tuple containing an array list of words and an AVL tree.
  """
  array_list = []
  avl_tree = AVLTree()

  corpus = autocomplete.get_corpus()
  for word in corpus:
    array_list.append(word)
    avl_tree.add(word)

  return array_list, avl_tree
  

if __name__ == "__main__":
  """
  Initializes the autocomplete functionality and performs search operations.
  """
  autocomplete = AutocompleteWords('week_02_autocomplete_words/assets/holy_bible.txt')
  array_list, avl_tree = build_structures(autocomplete)

  prefix = "a"
  
  avl_tree_results = autocomplete.search(avl_tree.root, prefix)
  print(".:: Searching the AVL tree")
  print(f"    => prefix: '{prefix}'")
  print(f"    => count_words: {avl_tree_results['count_words']} words found")
  print(f"    => file_path: '{avl_tree_results['file_path']}'")
  print(f"    => file_size: {avl_tree_results['file_size'] / (1024 * 1024)} MB")
  print(f"    => execution_time: {avl_tree_results['execution_time']} seconds")
  print(".:: Search ended.\n")

  array_list_results = autocomplete.search(array_list, prefix)
  print(".:: Searching the Array List")
  print(f"    => prefix: '{prefix}'")
  print(f"    => count_words: {array_list_results['count_words']} words found")
  print(f"    => file_path: '{array_list_results['file_path']}'")
  print(f"    => file_size: {array_list_results['file_size'] / (1024 * 1024)} MB")
  print(f"    => execution_time: {array_list_results['execution_time']} seconds")
  print(".:: Search ended.")

  print("\n.:: Comparing search results")
  print(f"    => best_structure: {'AVL Tree' if avl_tree_results['execution_time'] < array_list_results['execution_time'] else 'Array List'}")
  print(f"    => time_difference: {(array_list_results['execution_time'] - avl_tree_results['execution_time'])} seconds")
  print(".:: Comparison ended.")