from AutocompleteWords import AutocompleteWords
from AVLTree import AVLTree

def build_structures(autocomplete):
  array_list = []
  avl_tree = AVLTree()

  corpus = autocomplete.get_corpus()
  for word in corpus:
    array_list.append(word)
    avl_tree.add(word)

  return array_list, avl_tree

def init():
  autocomplete = AutocompleteWords('autocomplete_words/cinco_minutos.txt')
  array_list, avl_tree = build_structures(autocomplete)

  prefix = "a"
  
  print(".:: Searching the AVL tree")
  avl_tree_results = autocomplete.search(avl_tree.root, prefix)
    
  print(f"    => prefix: {prefix}")
  print(f"    => count_words: {avl_tree_results['count_words']}")
  print(f"    => file_path: {avl_tree_results['file_path']}")
  print(f"    => file_size: {avl_tree_results['file_size']}")
  print(f"    => execution_time: {avl_tree_results['execution_time']}")
  print(".:: Search ended.\n")
  
  array_list_results = autocomplete.search(array_list, prefix)
  print(".:: Searching the Array List")
  print(f"    => prefix: {prefix}")
  print(f"    => count_words: {avl_tree_results['count_words']}")
  print(f"    => file_path: {avl_tree_results['file_path']}")
  print(f"    => file_size: {avl_tree_results['file_size']}")
  print(f"    => execution_time: {avl_tree_results['execution_time']}")
  print(".:: Search ended.")
  
init()