n = int(input())

for i in range(1, n+1):
        print(" " * int(n-i) + "*" * i)
        


<문제>
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

<입력>
5
<출력>
    *
   **
  ***
 ****
*****

<해설>
4번 line 에서 공백 * int(n-i) 를 한 이유는 첫째 줄은 공백이 4칸이고 *이 마지막에 나오기 때문에 그 순서를 고려하여 작성함
