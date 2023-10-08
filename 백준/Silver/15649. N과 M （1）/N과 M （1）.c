#include <stdio.h>

int arr[9]; // 숫자 출력할 배열
int used[9]; // 각 인덱스에 해당하는 숫자가 arr에 담겨져있는지 유무 판별
int n, m;
 
void backtracking(int idx) {
	if (idx == m) {
		for (int i = 0; i < m; i++)
			printf("%d ", arr[i]);
		printf("\n");
	}
 
	for (int i = 1; i <= n; i++) {
		if (used[i] == 0) { // if i not in s:
			arr[idx] = i;
			used[i] = 1;
			backtracking(idx + 1);
			used[i] = 0;
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);
	backtracking(0);
	return 0;
}
 