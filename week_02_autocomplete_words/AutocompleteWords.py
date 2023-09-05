import AVLNode

import re
import os
import nltk
import time
from nltk.corpus import stopwords

# nltk.download('stopwords')

class AutocompleteWords:
  """
  AutocompleteWords class that allows searching for words in a text corpus.

  Args:
    file_path (str): The path to the corpus text file.

  Attributes:
    _file_path (str): The path to the corpus text file.
    _corpus (str): The content of the text corpus.
    _file_size (int): The size of the corpus file.
    _words (list): A list of unique words in the corpus after preprocessing.
    _execution_time (float): The execution time of word search operations.

  Methods:
    get_corpus(): Returns the content of the text corpus.
    get_result(): Returns a dictionary containing information about the search.
    search(target, prefix): Performs a search for words starting with the specified prefix.
    _performance(executor, target, prefix): Measures the execution time of an executor function.
    _preprocess(): Performs preprocessing of the text corpus, including removing stopwords and special characters.
    _search_in_avl_tree(node, prefix): Performs a search in an AVL tree of words.
    _search_in_array_list(array_list, prefix): Performs a search in a list of words.

  """

  def __init__(self, file_path):
    """
    Initializes an instance of AutocompleteWords with the path of the corpus file.

    Args:
      file_path (str): The path to the corpus text file.
    """
    self._file_path = file_path
    self._corpus = open(file_path).read()
    self._file_size = os.path.getsize(file_path)
    self._words = []
    self._execution_time = 0.0
    self._preprocess()

  def get_corpus(self):
    """
    Returns the content of the text corpus.

    Returns:
      str: The content of the text corpus.
    """
    return self._corpus

  def get_result(self):
    """
    Returns a dictionary containing information about the search.

    Returns:
      dict: A dictionary containing information about the search, including found words, word count,
            file path, corpus content, file size, and execution time.
    """
    return {
        'words': self._words,
        'count_words': len(self._words),
        'file_path': self._file_path,
        'corpus': self._corpus,
        'file_size': self._file_size,
        'execution_time': self._execution_time
    }

  def search(self, target, prefix):
    """
    Performs a search for words starting with the specified prefix.

    Args:
      target (AVLNode.AVLNode or list): The target of the search, which can be an AVL tree or a list of words.
      prefix (str): The prefix to be used in the search.

    Returns:
      dict: A dictionary containing information about the search, including found words, word count,
            file path, corpus content, file size, and execution time.
    """
    if type(target) is AVLNode.AVLNode:
      self._performance(self._search_in_avl_tree, target, prefix)
    elif type(target) is list:
      self._performance(self._search_in_array_list, target, prefix)
    else:
      print(f"Invalid type ({type(target)})")
    return self.get_result()

  def _performance(self, executor, target, prefix):
    """
    Measures the execution time of an executor function.

    Args:
      executor (function): The function to be executed.
      target (object): The search target.
      prefix (str): The prefix to be used in the search.
    """
    start_time = time.time()
    executor(target, prefix)
    self._execution_time = time.time() - start_time

  def _preprocess(self):
    """
    Performs preprocessing of the text corpus, including removing stopwords and special characters.
    """
    self._corpus = self._corpus.lower()
    self._corpus = re.sub(r'[^\w\s]', '', self._corpus)

    words = self._corpus.split()

    stop_words = set(stopwords.words('portuguese'))
    self._corpus = set([word for word in words if word not in stop_words])

  def _search_in_avl_tree(self, node, prefix):
    """
    Performs a search in an AVL tree of words.

    Args:
      node (AVLNode.AVLNode): The AVL tree node to be searched.
      prefix (str): The prefix to be used in the search.
    """
    if node is None:
      return
    if node.value.startswith(prefix):
      self._words.append(node.value)
      self._search_in_avl_tree(node.left_child, prefix)
      self._search_in_avl_tree(node.right_child, prefix)
    elif prefix < node.value:
      self._search_in_avl_tree(node.left_child, prefix)
    else:
      self._search_in_avl_tree(node.right_child, prefix)

  def _search_in_array_list(self, array_list, prefix):
    """
    Performs a search in a list of words.

    Args:
      array_list (list): The list of words to be searched.
      prefix (str): The prefix to be used in the search.

    Returns:
      list: A list of words that start with the specified prefix.
    """
    result = [word for word in array_list if word.startswith(prefix)]
    return result
