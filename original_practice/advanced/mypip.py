from vbvstatus import check
import json

cc_data = "4000050000000000|12|25|123" 
result = check(cc_data)


print(json.dumps(result, indent=4))