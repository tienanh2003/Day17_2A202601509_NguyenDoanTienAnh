# Lab 17 Submission

**Student:** Nguyen Doan Tien Anh  
**Date:** 2026-08-17

---

## 1. Memory layer quan trọng nhất

**Long-term memory (Context Block)** là layer quan trọng nhất trong bộ test này.

Lý do: Bộ đánh giá gồm 11 test cases với phân bố đa dạng (short-term, long-term, episodic, semantic, mixed). Trong đó, long-term chiếm tỷ trọng lớn nhất vì nó lưu trữ preferences, open loops, và deadline — những thông tin cần persist qua nhiều sessions. Context Block của Zep cung cấp relevant context từ historical threads mà không cần quản lý thủ công Redis keys như baseline.

Episodic và semantic đều quan trọng nhưng chỉ hoạt động khi long-term context đã được thiết lập đúng cách. Short-term dùng buffer đơn giản nên ít rủi ro nhất.

---

## 2. Trade-off: Zep Context Block vs Redis + Qdrant

| Khía cạnh | Zep Context Block | Redis + Qdrant |
|-----------|------------------|----------------|
| **Setup** | Managed service, config qua API key | Cần tự deploy và scale |
| **Context relevance** | Tự động relevance scoring | Cần vector search thủ công |
| **Latency** | ~1000ms (network + inference) | ~50ms local |
| **Cost** | API subscription | Infrastructure cost |
| **Data ownership** | Third-party | Full control |

**Khi nào dùng Zep:** Rapid prototyping, không muốn quản lý infra, chấp nhận latency cao hơn.

**Khi nào dùng Redis + Qdrant:** Production cần low latency, data sovereignty requirements, chi phí có thể kiểm soát được.

---

## 3. Guardrails chống memory poisoning

1. **Consent verification:** Chỉ ingest messages khi user đã opt-in qua `require_memory_consent()`. Không bao giờ ingest mà không có consent record.

2. **PII minimization:** Sanitize email, phone trước khi ghi vào Zep qua `minimize_pii()`. Không lưu raw PII vào memory graph.

3. **Source validation:** Chỉ ingest từ verified sessions trong `sessions.json`. Không accept arbitrary user input làm memory source.

4. **TTL/Expiration:** Áp dụng TTL cho episodic memories. Không giữ vĩnh viễn những episode cũ không còn relevant.

5. **Write review:** Với `episodic_maintenance`, không delete episodes một cách blind. Cần retention policy và human approval trước khi destructive operations.

6. **Input filtering:** Trong baseline `local_baseline.py`, input được parsed qua structured schema (JSON), không phải raw user text.

7. **Audit trail:** Ghi log mọi write operations để trace nếu có poisoning attempt.
