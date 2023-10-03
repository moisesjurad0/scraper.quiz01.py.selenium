# swagger_client.DefaultApi

All URIs are relative to */Prod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_ok_ok_get**](DefaultApi.md#test_ok_ok_get) | **GET** /ok | Test Ok
[**test_ok_test_get**](DefaultApi.md#test_ok_test_get) | **GET** /test | Test Ok

# **test_ok_ok_get**
> object test_ok_ok_get()

Test Ok

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Test Ok
    api_response = api_instance.test_ok_ok_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_ok_ok_get: %s\n" % e)
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

# **test_ok_test_get**
> object test_ok_test_get()

Test Ok

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Test Ok
    api_response = api_instance.test_ok_test_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_ok_test_get: %s\n" % e)
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

