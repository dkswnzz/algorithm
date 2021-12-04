import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		BigInteger dp[] = new BigInteger[N + 2];

		dp[0] = BigInteger.ZERO;
		dp[1] = BigInteger.ONE;

		for (int i = 2; i <= N; i++) {
			dp[i] = dp[i - 1].add(dp[i - 2]);
		}
		System.out.print(dp[N]);
	}
}
