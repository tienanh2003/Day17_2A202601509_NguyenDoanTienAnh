# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **15/20**
- Evidence hit rate: **75.0%**
- Average retrieval latency: **987.3 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **0/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.4 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G08 | long_term | PASS | 1667.4 | 870 | 0.0% |  |
| G09 | long_term | PASS | 1364.8 | 1575 | 0.0% |  |
| G12 | semantic | PASS | 293.5 | 418 | 8.9% |  |
| G14 | semantic | PASS | 228.1 | 270 | 30.2% |  |
| G15 | semantic | PASS | 241.9 | 270 | 41.2% |  |
| G19 | mixed | PASS | 1433.3 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1506.2 | 1491 | 0.0% |  |
| G04 | long_term | PASS | 1917.0 | 1469 | 0.0% |  |
| G05 | long_term | PASS | 1445.7 | 1457 | 0.0% |  |
| G10 | episodic | PASS | 243.4 | 519 | 0.0% |  |
| G11 | episodic | PASS | 240.1 | 517 | 0.0% |  |
| G13 | semantic | PASS | 230.4 | 416 | 26.4% |  |
| G16 | mixed | PASS | 1672.2 | 581 | 0.0% |  |
| G18 | mixed | FAIL | 550.5 | 500 | 11.5% | missing=ClientSession |
| G20 | mixed | FAIL | 1994.1 | 831 | 0.0% | missing=ClientSession |
| G06 | long_term | FAIL | 1450.7 | 1523 | 0.0% | missing=BLUEBIRD-42, TypeScript, NestJS |
| G07 | long_term | FAIL | 1493.3 | 1526 | 0.0% | missing=BLUEBIRD-42, TypeScript, NestJS |
| G17 | mixed | FAIL | 1773.4 | 581 | 8.1% | missing=TypeScript, NestJS |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan Tran is planning the architecture for their private product, LOTUS-88. They are prioritizing Java and Spring Boot for the backend and will not use Python for backend examples. They are also looking into implementing retry logic for a payment service within their product and need to present technology choices to partners.  For their private product, LOTUS-88, Lan Tran prefers Java and Spring Boot, and does not want Python examples for the backend. They are seeking code examples that match their chosen stack for implementing payment retries and applying general payment policies when initiating a transaction.  Lan Tran has instructed the AI to use Java and Spring Boot for bac`

### G09 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27.  For company projects, Minh uses TypeScript with NestJS for backend development and avoids Python for the BLUEBIRD-42 project. For personal projects, Minh prefers Python, as demonstrated by the ORCHID-27 demo project. Minh also works on debugging async HTTP requests and setting up development environments for personal coding.  Minh prefers Python for personal projects and individual coding sessions, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values accuracy and carefulness, especially when cataloging personal projects to avoid misattribution. Minh also prioritizes adherence to official `

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan Tran is planning the architecture for their private product, LOTUS-88. They are prioritizing Java and Spring Boot for the backend and will not use Python for backend examples. They are also looking into implementing retry logic for a payment service within their product and need to present technology choices to partners.  For their private product, LOTUS-88, Lan Tran prefers Java and Spring Boot, and does not want Python examples for the backend. They are seeking code examples that match their chosen stack for implementing payment retries and applying general payment policies when initiating a transaction.  Lan Tran has instructed the AI to use Java and Spring `

### G03 - long_term

`<USER_SUMMARY> Minh uses Python for personal projects and demos. For company projects, specifically BLUEBIRD-42, the backend must use TypeScript with NestJS. Minh also has an open loop benchmark report due by Friday at 16:00 for LAB-REPORT-1600. Minh is debugging async HTTP requests and has attempted increasing the timeout to 60s.  Minh prefers Python for personal projects and demos, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values clear explanations with short code examples when learning new concepts. When explaining, Minh prefers explanations presented in a way that aids retention, such as using visual aids for abstract concepts like corouti`

### G04 - long_term

`<USER_SUMMARY> Minh uses Python for personal projects and demos. For company projects, specifically BLUEBIRD-42, the backend must use TypeScript with NestJS. Minh also has an open loop benchmark report due by Friday at 16:00 for LAB-REPORT-1600. Minh is debugging async HTTP requests and has attempted increasing the timeout to 60s.  Minh prefers Python for personal projects and demos, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values clear explanations with short code examples when learning new concepts. When explaining, Minh prefers explanations presented in a way that aids retention, such as using visual aids for abstract concepts like corouti`

### G05 - long_term

`<USER_SUMMARY> Minh uses Python for personal projects and demos. For company projects, specifically BLUEBIRD-42, the backend must use TypeScript with NestJS. Minh also has an open loop benchmark report due by Friday at 16:00 for LAB-REPORT-1600. Minh is debugging async HTTP requests and has attempted increasing the timeout to 60s.  Minh prefers Python for personal projects and demos, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values clear explanations with short code examples when learning new concepts. When explaining, Minh prefers explanations presented in a way that aids retention, such as using visual aids for abstract concepts like corouti`

### G10 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600`

### G11 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Minh dang ngoi mot minh viet cho xong cai ham retry cho `

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh uses Python for personal projects and demos. For company projects, specifically BLUEBIRD-42, the backend must use TypeScript with NestJS. Minh is debugging async HTTP requests and has attempted increasing the timeout to 60s, and identified connection churn as the primary issue rather than timeout thresholds for the ASYNC-FIX-20 incident. Minh also has an open loop benchmark report due by Friday at 16:00 for LAB-REPORT-1600.  Minh prefers Python for personal projects and demos, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values clear explanations with short code examples when learning new concepts. When explaining,`

### G18 - mixed

`<EPISODIC> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Toi nay min`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh uses Python for personal projects and demos. For company projects, specifically BLUEBIRD-42, the backend must use TypeScript with NestJS. Minh is debugging async HTTP requests and has attempted increasing the timeout to 60s, and identified connection churn as the primary issue rather than timeout thresholds for the ASYNC-FIX-20 incident. Minh also has an open loop benchmark report due by Friday at 16:00 for LAB-REPORT-1600.  Minh prefers Python for personal projects and demos, and dislikes Java. For company projects, the backend must use TypeScript with NestJS. Minh values clear explanations with short code examples when learning new concepts. When explaining,`

### G06 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27. They are currently learning about async/await and sometimes confuse coroutines with Tasks. They are also debugging async HTTP requests and have encountered issues with connection churn, which were resolved by reusing aiohttp ClientSession and setting concurrency to 20. A specific incident related to this was labeled ASYNC-FIX-20.  The user is working on a company project that requires standardizing the backend. They are also tasked with adding a retry payment function to this company project's backend, following company-mandated technology standards. The user also has a personal demo project for which they prefer Python.  The use`

### G07 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27. They are currently learning about async/await and sometimes confuse coroutines with Tasks. They are also debugging async HTTP requests and have encountered issues with connection churn, which were resolved by reusing aiohttp ClientSession and setting concurrency to 20. A specific incident related to this was labeled ASYNC-FIX-20.  The user is working on a company project that requires standardizing the backend. They are also tasked with adding a retry payment function to this company project's backend, following company-mandated technology standards. The user also has a personal demo project for which they prefer Python.  The use`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27. They are learning about async/await and sometimes confuse coroutines with Tasks. They have encountered issues with connection churn in async HTTP requests, which were resolved by reusing aiohttp ClientSession and setting concurrency to 20. A specific incident related to this was labeled ASYNC-FIX-20.  The user is standardizing the backend for a company project and is adding a retry payment function to it, adhering to company technology standards. They also have a personal demo project.  The user prefers Python and dislikes Java. For code explanations, they prefer short examples. When explaining async/await concepts li`
