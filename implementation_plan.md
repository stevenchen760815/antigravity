# Implementation Plan - Phase 2 (AR & Deity Expansion)

## Goal Description
Enhance the "Chen Zhen Fang ERP" with:
1.  **Accounts Receivable (AR)**: Track unpaid orders, allow Boss to mark as paid (auto-generating Income tranasction), and view total debt.
2.  **Deity Expansion**: Move hardcoded seed data to `data/deities.json` and add 10+ major Taiwanese deities.

## Proposed Changes

### [Data]
#### [NEW] [data/deities.json](file:///c:/antigravity/專案/chen-zhen-fang-bot/data/deities.json)
- JSON file containing 10+ deities (Name, Lunar Birthday, Offerings, Description).

### [Services]
#### [MODIFY] [services/erp_service.py](file:///c:/antigravity/專案/chen-zhen-fang-bot/services/erp_service.py)
- `get_unpaid_orders(user_id=None)`: List pending orders.
- `mark_order_paid(order_id)`:
    1. Update Order status to 'paid'.
    2. Create `Transaction` (Income) automatically.
    3. Return success status.
- `get_ar_summary()`: Total unpaid amount across all users.

#### [MODIFY] [init_db.py](file:///c:/antigravity/專案/chen-zhen-fang-bot/init_db.py)
- Remove hardcoded seeding.
- Add `load_deities_from_json()` logic.

### [Bot]
#### [MODIFY] [app.py](file:///c:/antigravity/專案/chen-zhen-fang-bot/app.py)
- **Admin Commands**:
    - `!欠款`: Show total AR and list of Debtors.
    - `!入帳 [Order_ID]`: Mark an order as paid.
- **Customer Commands**:
    - `我的帳單`: Show my unpaid orders.

## Verification Plan
- **Test AR**: Create Order -> Check AR (should increase) -> Mark Paid -> Check AR (decrease) & Check Transaction (Income created).
- **Test JSON Load**: Run `init_db.py` and query `Deity.query.count()`.
