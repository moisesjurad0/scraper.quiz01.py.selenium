# coding: utf-8

"""
    QuestionsAPI

     QuestionsAPI helps you do operations with the scraped data. 🚀  ## Questions  You will be able to:  * **Put questions** (Create & Update & batch). * **Read questions**. * **Search questions**.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class QuestionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_put_items_api_v1_questions_batch_put(self, body, **kwargs):  # noqa: E501
        """Batch Put Items  # noqa: E501

        Updates multiple questions in DynamoDB using a batch write item request.  Args:     items: A list of Question objects.  Returns:     None.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_put_items_api_v1_questions_batch_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[QuestionModel] body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_put_items_api_v1_questions_batch_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_put_items_api_v1_questions_batch_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def batch_put_items_api_v1_questions_batch_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Batch Put Items  # noqa: E501

        Updates multiple questions in DynamoDB using a batch write item request.  Args:     items: A list of Question objects.  Returns:     None.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_put_items_api_v1_questions_batch_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[QuestionModel] body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_put_items_api_v1_questions_batch_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_put_items_api_v1_questions_batch_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/batch', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_item_api_v1_questions_id_answer_text_delete(self, id, answer_text, **kwargs):  # noqa: E501
        """Delete Item  # noqa: E501

        _summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_api_v1_questions_id_answer_text_delete(id, answer_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str answer_text: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_item_api_v1_questions_id_answer_text_delete_with_http_info(id, answer_text, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_item_api_v1_questions_id_answer_text_delete_with_http_info(id, answer_text, **kwargs)  # noqa: E501
            return data

    def delete_item_api_v1_questions_id_answer_text_delete_with_http_info(self, id, answer_text, **kwargs):  # noqa: E501
        """Delete Item  # noqa: E501

        _summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_item_api_v1_questions_id_answer_text_delete_with_http_info(id, answer_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str answer_text: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'answer_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_item_api_v1_questions_id_answer_text_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_item_api_v1_questions_id_answer_text_delete`")  # noqa: E501
        # verify the required parameter 'answer_text' is set
        if ('answer_text' not in params or
                params['answer_text'] is None):
            raise ValueError("Missing the required parameter `answer_text` when calling `delete_item_api_v1_questions_id_answer_text_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'answer_text' in params:
            path_params['answer_text'] = params['answer_text']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/{id}/{answer_text}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_items_api_v1_questions_get(self, **kwargs):  # noqa: E501
        """Get All Items  # noqa: E501

        _summary_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_items_api_v1_questions_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_items_api_v1_questions_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_items_api_v1_questions_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_items_api_v1_questions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Items  # noqa: E501

        _summary_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_items_api_v1_questions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_items_api_v1_questions_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_item_api_v1_questions_put(self, body, **kwargs):  # noqa: E501
        """Put Item  # noqa: E501

        _summary_  Args:     item (Question): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_item_api_v1_questions_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_item_api_v1_questions_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_item_api_v1_questions_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_item_api_v1_questions_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Put Item  # noqa: E501

        _summary_  Args:     item (Question): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_item_api_v1_questions_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_item_api_v1_questions_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_item_api_v1_questions_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_item_api_v1_questions_id_answer_text_get(self, id, answer_text, **kwargs):  # noqa: E501
        """Read Item  # noqa: E501

        _summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_item_api_v1_questions_id_answer_text_get(id, answer_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str answer_text: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_item_api_v1_questions_id_answer_text_get_with_http_info(id, answer_text, **kwargs)  # noqa: E501
        else:
            (data) = self.read_item_api_v1_questions_id_answer_text_get_with_http_info(id, answer_text, **kwargs)  # noqa: E501
            return data

    def read_item_api_v1_questions_id_answer_text_get_with_http_info(self, id, answer_text, **kwargs):  # noqa: E501
        """Read Item  # noqa: E501

        _summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_item_api_v1_questions_id_answer_text_get_with_http_info(id, answer_text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str answer_text: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'answer_text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_item_api_v1_questions_id_answer_text_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `read_item_api_v1_questions_id_answer_text_get`")  # noqa: E501
        # verify the required parameter 'answer_text' is set
        if ('answer_text' not in params or
                params['answer_text'] is None):
            raise ValueError("Missing the required parameter `answer_text` when calling `read_item_api_v1_questions_id_answer_text_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'answer_text' in params:
            path_params['answer_text'] = params['answer_text']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/{id}/{answer_text}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_items_begins_with_api_v1_questions_search_begins_with_post(self, body, **kwargs):  # noqa: E501
        """Search Items Begins With  # noqa: E501

        _summary_  Args:     item (QuestionSearchContainsModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_begins_with_api_v1_questions_search_begins_with_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionScanModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_items_begins_with_api_v1_questions_search_begins_with_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.search_items_begins_with_api_v1_questions_search_begins_with_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def search_items_begins_with_api_v1_questions_search_begins_with_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search Items Begins With  # noqa: E501

        _summary_  Args:     item (QuestionSearchContainsModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_begins_with_api_v1_questions_search_begins_with_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionScanModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_items_begins_with_api_v1_questions_search_begins_with_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `search_items_begins_with_api_v1_questions_search_begins_with_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/search/begins_with', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_items_contains_api_v1_questions_search_contains_post(self, body, **kwargs):  # noqa: E501
        """Search Items Contains  # noqa: E501

        _summary_  Args:     item (QuestionSearchBeginsWithModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_contains_api_v1_questions_search_contains_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionScanModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_items_contains_api_v1_questions_search_contains_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.search_items_contains_api_v1_questions_search_contains_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def search_items_contains_api_v1_questions_search_contains_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search Items Contains  # noqa: E501

        _summary_  Args:     item (QuestionSearchBeginsWithModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_contains_api_v1_questions_search_contains_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionScanModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_items_contains_api_v1_questions_search_contains_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `search_items_contains_api_v1_questions_search_contains_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/search/contains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_items_query_eq_api_v1_questions_search_query_eq_post(self, body, **kwargs):  # noqa: E501
        """Search Items Query Eq  # noqa: E501

        _summary_  Args:     item (QuestionSearchQueryModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_query_eq_api_v1_questions_search_query_eq_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionQueryModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_items_query_eq_api_v1_questions_search_query_eq_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.search_items_query_eq_api_v1_questions_search_query_eq_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def search_items_query_eq_api_v1_questions_search_query_eq_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search Items Query Eq  # noqa: E501

        _summary_  Args:     item (QuestionSearchQueryModel): _description_  Returns:     _type_: _description_  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_items_query_eq_api_v1_questions_search_query_eq_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionQueryModel body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_items_query_eq_api_v1_questions_search_query_eq_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `search_items_query_eq_api_v1_questions_search_query_eq_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/questions/search/query_eq', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
