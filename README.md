# EPC — Event-Persistent Computation

Experimental Python prototypes of **Nothing → Idea of Nothing → Idea of Something → Something → Everything**.

- Nothing is absence, **not** numeric zero.
- Zero is off: no calculation.
- One / Something is an active computational event.
- Everything is the complete persistent state, **not** another trigger.
- Event-only implementations receive active event positions, skipping intervening off inputs.

Run `python epc_event_only_everything.py` and `python epc_thousand_values.py`.

Verified experiments: two active events update 10 → 20 → 40 while skipping one million zeros; 1,000-value Everything updates one value and preserves the other 999. These examples demonstrate selective computation, not a proven advantage over conventional event-driven systems or memory compression.
