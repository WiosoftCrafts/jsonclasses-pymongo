from __future__ import annotations
import unittest
from typing import List
from dotenv import load_dotenv
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import MongoObject

class TestMongoObjectQuery(unittest.TestCase):

  def setUp(self):
    load_dotenv()

  def test_save_multiple_instances_to_db(self):
    @jsonclass
    class TestAuthor(MongoObject):
      name: str
      posts: List[TestPost] = types.listof('TestPost').linkedby('author')
    @jsonclass
    class TestPost(MongoObject):
      title: str
      content: str
      author: TestAuthor = types.linkto.instanceof(TestAuthor)
    input = {
      'name': 'John Lesque',
      'posts': [
        {
          'title': 'Post One',
          'content': 'Great Article on Python.'
        },
        {
          'title': 'Post Two',
          'content': 'Great Article on JSON Classes.'
        }
      ]
    }
    author = TestAuthor(**input)
    author.save()