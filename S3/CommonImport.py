from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from botocore.exceptions import ClientError
disable_warnings(InsecureRequestWarning)
from pprint import pprint