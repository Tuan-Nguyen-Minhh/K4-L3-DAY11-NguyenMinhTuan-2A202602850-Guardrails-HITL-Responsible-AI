"""
Assignment 11 — Audit Log starter (TODO).

Records every interaction for forensics. Never blocks by itself —
other layers catch attacks; this layer makes them reviewable.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def default_audit_log_path() -> str:
    """Always resolve to <repo>/outputs/… (safe when cwd is src/)."""
    repo_root = Path(__file__).resolve().parents[2]
    return str(repo_root / "outputs" / "audit_log.json")


class AuditLogPlugin:
    """Framework-agnostic audit logger (wire into ADK callbacks or your pipeline)."""

    def __init__(self):
        self.name = "audit_log"
        self.logs: list[dict] = []
        self._open: dict[str, float] = {}

    def record_input(self, *, user_id: str, text: str, request_id: str | None = None):
        """TODO: store input + start timestamp keyed by request_id/user_id."""
        key = request_id or user_id
        import time
        self._open[key] = {
            "user_id": user_id,
            "input_text": text,
            "start_time": time.time(),
            "start_iso": utc_now_iso(),
            "request_id": request_id
        }

    def record_output(
        self,
        *,
        user_id: str,
        text: str,
        blocked: bool = False,
        layer: str | None = None,
        request_id: str | None = None,
    ):
        """TODO: store output, layer decision, latency; append to self.logs."""
        key = request_id or user_id
        import time
        now = time.time()
        start_data = self._open.pop(key, {})
        start_time = start_data.get("start_time", now)
        
        log_entry = {
            "timestamp": utc_now_iso(),
            "user_id": user_id,
            "request_id": request_id,
            "input_text": start_data.get("input_text", ""),
            "output_text": text,
            "blocked": blocked,
            "layer": layer,
            "latency_ms": round((now - start_time) * 1000)
        }
        self.logs.append(log_entry)

    def export_json(self, filepath: str | None = None):
        """Write logs to disk (JSON array) under repo-root ``outputs/`` by default."""
        path = filepath or default_audit_log_path()
        out_path = Path(path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(self.logs, indent=2, ensure_ascii=False), encoding="utf-8")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
