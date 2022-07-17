import requests
import json
import pandas as pd
import leetcode

leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTAyMzc4MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImFmN2E4YTIxZjBmZTBkMDQ5ZTliMmVkODAwZGUyNmM5MTEyYzBkZDIiLCJpZCI6MTAyMzc4MCwiZW1haWwiOiJtamdpbGw5ODRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJicm9uaWNrZWwiLCJ1c2VyX3NsdWciOiJicm9uaWNrZWwiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYnJvbmlja2VsL2F2YXRhcl8xNjEyNTc5NzQyLnBuZyIsInJlZnJlc2hlZF9hdCI6MTY1NzkzNDA5MiwiaXAiOiIyNjAzOjkwMDE6M2QwMzo0NDAwOjM4ODI6NDc3MTo2YjViOmQwOGYiLCJpZGVudGl0eSI6ImQ4OGEwM2YxMTc1ODQ2YzlhNjEwZGI5MjcxZjFiMTFiIiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwLCJzZXNzaW9uX2lkIjoyMzUzMjE5NH0.pPXaYberthaBQo-ww4zmVlosFiaSLZ8e3IWyprKQXXA"
csrf_token = "lTeQmmY091t8huZ4phpNAfnxCCdW68IpTEYHVFv6ixNZHCmD4tyHIVQrcyRgSb7W"
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

URL = "https://leetcode.com/graphql"
QUERY = """query questionOfToday {
	activeDailyCodingChallengeQuestion {
		date
		userStatus
		link
		question {
			acRate
			difficulty
			freqBar
			frontendQuestionId: questionFrontendId
			isFavor
			paidOnly: isPaidOnly
			status
			title
			titleSlug
			hasVideoSolution
			hasSolution
			topicTags {
				name
				id
				slug
			}
		}
	}
}"""

r = requests.post(URL, json={'query': QUERY}, headers={'Content-Type': 'application/json'})
print(r.status_code)
print(r.text)