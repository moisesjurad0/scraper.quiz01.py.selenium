# swagger_client.QuestionsApi

All URIs are relative to */Prod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_put_items_api_v1_questions_batch_put**](QuestionsApi.md#batch_put_items_api_v1_questions_batch_put) | **PUT** /api/v1/questions/batch | Batch Put Items
[**delete_item_api_v1_questions_id_answer_text_delete**](QuestionsApi.md#delete_item_api_v1_questions_id_answer_text_delete) | **DELETE** /api/v1/questions/{id}/{answer_text} | Delete Item
[**get_all_items_api_v1_questions_get**](QuestionsApi.md#get_all_items_api_v1_questions_get) | **GET** /api/v1/questions/ | Get All Items
[**put_item_api_v1_questions_put**](QuestionsApi.md#put_item_api_v1_questions_put) | **PUT** /api/v1/questions/ | Put Item
[**read_item_api_v1_questions_id_answer_text_get**](QuestionsApi.md#read_item_api_v1_questions_id_answer_text_get) | **GET** /api/v1/questions/{id}/{answer_text} | Read Item
[**search_items_begins_with_api_v1_questions_search_begins_with_post**](QuestionsApi.md#search_items_begins_with_api_v1_questions_search_begins_with_post) | **POST** /api/v1/questions/search/begins_with | Search Items Begins With
[**search_items_contains_api_v1_questions_search_contains_post**](QuestionsApi.md#search_items_contains_api_v1_questions_search_contains_post) | **POST** /api/v1/questions/search/contains | Search Items Contains
[**search_items_query_eq_api_v1_questions_search_query_eq_post**](QuestionsApi.md#search_items_query_eq_api_v1_questions_search_query_eq_post) | **POST** /api/v1/questions/search/query_eq | Search Items Query Eq

# **batch_put_items_api_v1_questions_batch_put**
> object batch_put_items_api_v1_questions_batch_put(body)

Batch Put Items

Updates multiple questions in DynamoDB using a batch write item request.  Args:     items: A list of Question objects.  Returns:     None.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
body = [swagger_client.QuestionModel()] # list[QuestionModel] | 

try:
    # Batch Put Items
    api_response = api_instance.batch_put_items_api_v1_questions_batch_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->batch_put_items_api_v1_questions_batch_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[QuestionModel]**](QuestionModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_api_v1_questions_id_answer_text_delete**
> object delete_item_api_v1_questions_id_answer_text_delete(id, answer_text)

Delete Item

_summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
id = 'id_example' # str | 
answer_text = 'answer_text_example' # str | 

try:
    # Delete Item
    api_response = api_instance.delete_item_api_v1_questions_id_answer_text_delete(id, answer_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->delete_item_api_v1_questions_id_answer_text_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **answer_text** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_items_api_v1_questions_get**
> object get_all_items_api_v1_questions_get()

Get All Items

_summary_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()

try:
    # Get All Items
    api_response = api_instance.get_all_items_api_v1_questions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->get_all_items_api_v1_questions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_item_api_v1_questions_put**
> object put_item_api_v1_questions_put(body)

Put Item

_summary_  Args:     item (Question): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
body = swagger_client.QuestionModel() # QuestionModel | 

try:
    # Put Item
    api_response = api_instance.put_item_api_v1_questions_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->put_item_api_v1_questions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionModel**](QuestionModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_item_api_v1_questions_id_answer_text_get**
> object read_item_api_v1_questions_id_answer_text_get(id, answer_text)

Read Item

_summary_  Args:     id (str): _description_     answer_text (str): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
id = 'id_example' # str | 
answer_text = 'answer_text_example' # str | 

try:
    # Read Item
    api_response = api_instance.read_item_api_v1_questions_id_answer_text_get(id, answer_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->read_item_api_v1_questions_id_answer_text_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **answer_text** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items_begins_with_api_v1_questions_search_begins_with_post**
> object search_items_begins_with_api_v1_questions_search_begins_with_post(body)

Search Items Begins With

_summary_  Args:     item (QuestionSearchContainsModel): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
body = swagger_client.QuestionScanModel() # QuestionScanModel | 

try:
    # Search Items Begins With
    api_response = api_instance.search_items_begins_with_api_v1_questions_search_begins_with_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->search_items_begins_with_api_v1_questions_search_begins_with_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionScanModel**](QuestionScanModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items_contains_api_v1_questions_search_contains_post**
> object search_items_contains_api_v1_questions_search_contains_post(body)

Search Items Contains

_summary_  Args:     item (QuestionSearchBeginsWithModel): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
body = swagger_client.QuestionScanModel() # QuestionScanModel | 

try:
    # Search Items Contains
    api_response = api_instance.search_items_contains_api_v1_questions_search_contains_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->search_items_contains_api_v1_questions_search_contains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionScanModel**](QuestionScanModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_items_query_eq_api_v1_questions_search_query_eq_post**
> object search_items_query_eq_api_v1_questions_search_query_eq_post(body)

Search Items Query Eq

_summary_  Args:     item (QuestionSearchQueryModel): _description_  Returns:     _type_: _description_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuestionsApi()
body = swagger_client.QuestionQueryModel() # QuestionQueryModel | 

try:
    # Search Items Query Eq
    api_response = api_instance.search_items_query_eq_api_v1_questions_search_query_eq_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->search_items_query_eq_api_v1_questions_search_query_eq_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionQueryModel**](QuestionQueryModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

