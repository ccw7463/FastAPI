import re

def check_yes(text):
    if re.search(r'yes', text, re.IGNORECASE):
        return "YES"
    else:
        return "NO"
    
def extract_python_code(text):
    python_code_pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)
    match = python_code_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return ""
    
def extract_python_pyplot_code(text):
    python_code_pattern = re.compile(r'```python\n(.*?)\nplt.show()', re.DOTALL)
    match = python_code_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return "" 
       
def extract_python_plotly_code(text):
    python_code_pattern = re.compile(r'```python\n(.*?)\nfig.show()', re.DOTALL)
    match = python_code_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return ""
    
def format_number(x):
    '''
        Des:
            숫자형 데이터 comma로 구분
    '''
    if isinstance(x, (int, float)):  # 숫자형 데이터인지 확인
        return "{:,}".format(x)
    else:
        return x