import argparse

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법')

# 입력받을 인자값 등록
# parser.add_argument('--src', '--s', required=True, help='src ip address')
parser.add_argument('--src', '--s', metavar='src input', type=str, required=True, help='src ip address')
parser.add_argument('--target', '--t', metavar='target input', type=str, required=True, help='target ip address')

# parser객체의 인자들 파싱
args = parser.parse_args()

# === 변수에 입력 ===
# 입력받은 인자값을 args에 저장
src_ip = args.src
target_ip = args.target

# 입력받은 인자값 출력
print(f"source ip: {args.src}, target ip: {args.target}")
print(f"source ip: {src_ip}, target ip: {target_ip}")
