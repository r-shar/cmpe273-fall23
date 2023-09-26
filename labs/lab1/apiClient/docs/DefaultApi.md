# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_item_id_get**](DefaultApi.md#items_item_id_get) | **GET** /items/{item_id} | 


# **items_item_id_get**
> ItemsItemIdGet200Response items_item_id_get(item_id)



Returns itemId passed as path parameter.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.int import Int
from openapi_client.models.items_item_id_get200_response import ItemsItemIdGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    item_id = openapi_client.Int() # Int | Id of item to get

    try:
        api_response = api_instance.items_item_id_get(item_id)
        print("The response of DefaultApi->items_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->items_item_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**Int**](.md)| Id of item to get | 

### Return type

[**ItemsItemIdGet200Response**](ItemsItemIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object containing itemId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

