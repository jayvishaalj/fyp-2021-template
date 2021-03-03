import sys


def check_bulkiness(response, threshold_size):
    original_size = sys.getsizeof(response)
    print(" Response is of Size ", original_size, " bytes")
    if(original_size > threshold_size):
        return None
    else:
        return response
