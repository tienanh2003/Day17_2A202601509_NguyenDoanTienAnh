from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # Step 1: Prime the eval thread with the current query
        prime_eval_thread(self.client, user_id, thread_id, query)

        # Step 2: Get user context from the thread
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # Step 3: Bonus - append fact search with validity ranges
        # NOTE: limit>=20 to avoid missing deadline/open-loop facts
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        from .utils import join_nonempty
        return join_nonempty([context_block, fact_text], sep="\n\n")

    # def retrieve_episodic(self, user_id: str, query: str) -> str:
    #     # Search for episodic memories (past sessions/experiences)
    #     # Tip: episode_char_cap=180 keeps more distinct episodes within budget
    #     try:
    #         results = self.client.graph.search(
    #             user_id=user_id,
    #             query=cap_query(query),
    #             scope="episodes",
    #             limit=15,
    #         )
    #     except Exception:
    #         return ""

    #     return render_graph_search(results, episode_char_cap=180)
    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # Golden queries can be longer than Zep's 400-char search limit.
        # Preserve both the beginning and the tail because the tail may contain
        # an important episodic sub-question.
        if len(query) > 400:
            search_query = f"{query[:190]} ... {query[-190:]}"
        else:
            search_query = query

        try:
            results = self.client.graph.search(
                user_id=user_id,
                query=cap_query(search_query),
                scope="episodes",
                limit=15,
            )
        except Exception:
            return ""

        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # Search the standalone semantic graph (not user-specific)
        # scope="episodes" keeps literal markers like PAYMENT-RULE-3
        # Avoid "auto" scope as it drops literal codes
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Compatibility fallback: try scope="nodes"
            try:
                results = self.client.graph.search(
                    graph_id=graph_id,
                    query=q,
                    scope="nodes",
                    limit=8,
                )
            except Exception:
                return ""

        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order
        return self.budget.assemble(layers)
