import AVLTree
import AVLNode
import Node

import re
import os
import nltk
import time
from nltk.corpus import stopwords

# nltk.download('stopwords')

class AutocompleteWords:
  def __init__(self, file_path):
    self._file_path = file_path
    self._corpus    = open(file_path).read()
    self._file_size = os.path.getsize(file_path)
    
    self._words     = []
    self._execution_time = 0.0

    self._preprocess()

  def get_corpus(self):
    return self._corpus

  def get_result(self):
    return {
      'words':          self._words,
      'count_words':    len(self._words),
      'file_path':      self._file_path,
      'corpus':         self._corpus,
      'file_size':      self._file_size,
      'execution_time': self._execution_time
    }
    
  def search(self, target, prefix):
    if type(target) is AVLNode.AVLNode:
      self._performance(self._search_in_avl_tree, target, prefix)
    elif type(target) is list:
      self._performance(self._search_in_array_list, target, prefix)
    else:
      print(f"Tipo ({type(target)}) inválido")
    return self.get_result()

  def _performance(self, executor, target, prefix):
    start_time = time.time()
    executor(target, prefix)
    self._execution_time = time.time() - start_time

  def _preprocess(self):
    self._corpus = self._corpus.lower()
    self._corpus = re.sub(r'[^\w\s]', '', self._corpus)

    words = self._corpus.split()
    
    stop_words = set(stopwords.words('portuguese'))
    self._corpus = set([word for word in words if word not in stop_words])

  def _search_in_avl_tree(self, node, prefix):
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
    result = [word for word in array_list if word.startswith(prefix)]
    return result
