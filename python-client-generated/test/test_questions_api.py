# coding: utf-8

"""
    QuestionsAPI

     QuestionsAPI helps you do operations with the scraped data. 🚀  ## Questions  You will be able to:  * **Put questions** (Create & Update & batch). * **Read questions**. * **Search questions**.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.questions_api import QuestionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestQuestionsApi(unittest.TestCase):
    """QuestionsApi unit test stubs"""

    def setUp(self):
        self.api = QuestionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_put_items_api_v1_questions_batch_put(self):
        """Test case for batch_put_items_api_v1_questions_batch_put

        Batch Put Items  # noqa: E501
        """
        pass

    def test_delete_item_api_v1_questions_id_answer_text_delete(self):
        """Test case for delete_item_api_v1_questions_id_answer_text_delete

        Delete Item  # noqa: E501
        """
        pass

    def test_get_all_items_api_v1_questions_get(self):
        """Test case for get_all_items_api_v1_questions_get

        Get All Items  # noqa: E501
        """
        pass

    def test_put_item_api_v1_questions_put(self):
        """Test case for put_item_api_v1_questions_put

        Put Item  # noqa: E501
        """
        pass

    def test_read_item_api_v1_questions_id_answer_text_get(self):
        """Test case for read_item_api_v1_questions_id_answer_text_get

        Read Item  # noqa: E501
        """
        pass

    def test_search_items_begins_with_api_v1_questions_search_begins_with_post(self):
        """Test case for search_items_begins_with_api_v1_questions_search_begins_with_post

        Search Items Begins With  # noqa: E501
        """
        pass

    def test_search_items_contains_api_v1_questions_search_contains_post(self):
        """Test case for search_items_contains_api_v1_questions_search_contains_post

        Search Items Contains  # noqa: E501
        """
        pass

    def test_search_items_query_eq_api_v1_questions_search_query_eq_post(self):
        """Test case for search_items_query_eq_api_v1_questions_search_query_eq_post

        Search Items Query Eq  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
