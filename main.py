import feedparser, time

URL="https://dkswnkk.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=10

markdown_text = """

## 백준
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=dkswnkk)](https://solved.ac/dkswnkk/)

[유용한 문법 정리](https://dkswnkk.tistory.com/483?category=549172)
--
1. [String split 함수](https://dkswnkk.tistory.com/476?category=549172)
2. [특정문자 치환 regex_replace](https://dkswnkk.tistory.com/479?category=549172)
3. [문자열 대소문자 변환](https://dkswnkk.tistory.com/483?category=549172)
4. [String to CharArray](https://dkswnkk.tistory.com/249?category=549172)
5. [upper_bound, lower_bound](https://dkswnkk.tistory.com/533)
6. [비트마스킹](https://dkswnkk.tistory.com/650)
7. [배열 돌리기와 달팽이 배열](https://dkswnkk.tistory.com/660?category=549172)

## 템플릿 코드
1. [플로이드-와샬](https://dkswnkk.tistory.com/535)
2. [에라토스테네스의 체](https://dkswnkk.tistory.com/490?category=549172)
3. [다익스트라](https://dkswnkk.tistory.com/546)
4. [유니온파인드](https://dkswnkk.tistory.com/627)

## ✅ 최근 푼 문제

""" # list of blog posts will be appended here
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        tags = feed['tags'][0]['term']
        if tags == '백준(BOJ)' or tags == '프로그래머스(Programmers)' or tags == 'Leetcode' or tags == 'Note':
            feed_date = feed['published_parsed']
            markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        f = open("README.md", mode="w", encoding="utf-8")
        f.write(markdown_text)
        f.close()
