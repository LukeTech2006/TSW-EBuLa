import requests, json, sys, argparse

def main() -> int:
    parser = argparse.ArgumentParser('DS100 Resolver')
    parser.add_argument('code')
    args = parser.parse_args()
    request_code = args.code
    reqHandler = requests.get(f'https://zudis.de/generic/API_IRIS.php?action=search&input={request_code.lower()}')
    request_json = json.loads(reqHandler.text)
    try: print(f'Name: {request_json['name']}\nRil 100: {request_json['ds100']}')
    except Exception as e: exception = e
    return 1 if 'exception' in locals() else 0

if __name__ == '__main__':
    code = main()
    sys.exit(code)