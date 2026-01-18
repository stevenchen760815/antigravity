# Hidden Risks Analysis: The "Invisible Bombs"
> **Context**: We have designed a robust "Federal System" (3 Agents, 8 Skills, Recursive Forking).
> **Question**: "Where are the hidden bombs?"
> **Verdict**: The bombs are no longer in *Code*, they have moved to *Time* and *Communication*.

## 💣 Bomb 1: The "Mock Drift" (Desynchronized Reality)
> *The Map is not the Territory.*

*   **The Mechanism**: 
    1.  Architect defines `Contract v1`.
    2.  Tech Lead spins up `Mock v1`.
    3.  Frontend Team builds against `Mock v1`.
    4.  Backend Team (Sub-Project) starts building `Real v1`, but discovers a fatal flaw (e.g., circular dependency).
    5.  Backend Team changes logic to `Real v2`.
*   **The Explosion**: 
    *   Backend ships `Real v2`.
    *   Frontend ships `UI v1`.
    *   **Result**: Integration Failure at runtime. The "Perfect Mock" hid the "Evolving Reality".
*   **Fix**: **"Contract Integrity Lock"**.
    *   Backend Team *cannot* change the Contract unilaterally. They must trigger a "Contract Amendment Request" back to the Architect. The Mock must be updated *before* the Backend continues.

## 💣 Bomb 2: The "Zombie Sub-Project" (Context Divergence)
> *While you were working, the world changed.*

*   **The Mechanism**:
    1.  L1 Task "Campaign System" forks L5 "Targeting Engine".
    2.  L5 Team goes into a "Deep Dive" (Sub-Session) for 3 days.
    3.  Day 2: User tells L1 Architect: "Actually, cancel the Campaign System, we want a simple Discount System."
*   **The Explosion**: 
    *   L5 Team continues burning tokens/money on a dead feature.
    *   They merge back a massive "feature" that is now garbage.
*   **Fix**: **"Context Heartbeat"**.
    *   Sub-Projects must ping the Parent Session daily: "Is `[Campaign Task]` still Active?"
    *   If Parent says "Cancelled", Sub-Project self-destructs immediately.

## 💣 Bomb 3: The "Ivory Tower" Architect (Feasibility Gap)
> *It works in theory.*

*   **The Mechanism**:
    1.  Architect (who is banned from coding) defines a "Perfect Schema" for L10.
    2.  It looks elegant.
    3.  Builder (at L10) realizes: "This Schema requires joining 5 tables with 100M rows. It will take 30 seconds to query."
*   **The Explosion**: 
    *   Builder is stuck. The Architect's "Law" is physically impossible to implement performantly.
    *   Builder tries to hack it (violating rules) or halts (deadlock).
*   **Fix**: **"Tracer Bullet Probe"**.
    *   Before freezing the Contract, the Builder is allowed to run a "Dirty Prototype" (Timebox: 30 mins) to prove feasibility.
    *   Only *verified* contracts get locked.

## 💣 Bomb 4: The "Not My Job" Void (UX Gap)
> *Everyone built the brick, nobody built the wall.*

*   **The Mechanism**:
    *   Architect: "Schema is valid."
    *   Tech Lead: "Security is valid."
    *   Builder: "Code compiles."
*   **The Explosion**: 
    *   The Product ships.
    *   User tries to use it. "Why do I have to click 50 times to create a coupon?"
    *   **Cause**: No Agent owns "Usability". The structure sliced the "Experience" into isolated "Functions".
*   **Fix**: **"The 4th Agent: Product Owner"** (Future Scope).
    *   Or, mandate the **Architect** to perform a "Walkthrough Simulation" (Mental Replay) of the user flow before technical decomposition.

---

## 🛡️ Summary of Defenses

| Bomb | Defense Strategy | Mechanism |
| :--- | :--- | :--- |
| **Mock Drift** | **Contract Locking** | Backend cannot change Interface without Architect approval. |
| **Zombie Child** | **Heartbeat Sync** | Child Session checks Parent Task Status before starting work. |
| **Ivory Tower** | **Tracer Probes** | Builder runs "Feasibility Check" before Contract Freeze. |
| **UX Void** | **Flow Simulation** | Architect must generate `user_journey_walkthrough.md`. |
