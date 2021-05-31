package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _11053 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int A = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());

		int arr[] = new int[1001];

		for (int i = 0; i < A; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int dp[] = new int[1001];
		int ans = 0;
		for (int i = 0; i < A; i++) {
			int max = 0;
			for (int j = 0; j <= i; j++) {
				if (arr[i] > arr[j]) {
					if (max <= dp[j]) {
						max = dp[j];
					}
				}
			}
			dp[i] = max + 1;
			if (ans < dp[i])
				ans = dp[i];
		}
		System.out.println(ans);

	}
}
