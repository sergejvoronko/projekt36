# projekt36-astro — Project Handover

BMW E36 build journal site. Astro on **Cloudflare Worker** (NOT Pages) — `main: @astrojs/cloudflare/entrypoints/server` with ASSETS binding.

## Stack & commands
- Build: `source ~/.nvm/nvm.sh && nvm use 22 && npm run build`
- Deploy: `npm run deploy` (build + wrangler deploy)
- Preview: `npm run preview` (build + wrangler dev)
- Secrets live in Cloudflare dashboard (e.g. `PRINTIFY_API_TOKEN`) — never in repo

## Content
- Scan translation pipeline: 002-en.webp done; 004/006/008/010 pending same pipeline (see memory `project_scans_pending.md`)

## Related project: OpenBMWDiag
`/home/sergej/Downloads/openbmwdiag` — handled in THIS session (related to the E36 work).

Self-hosted BMW K-line diagnostic platform: web UI, community ECU definition DB, Docker-based. Tested on E36/E34/E39/E46, Bosch Motronic 3.3/5.2/7.2/MS41, ATE MK20 ABS.
- Structure: `backend/`, `frontend/` (vanilla HTML/CSS/JS, nginx in Docker, no build step), `serial-adapter/`, `ecu-db/`, `grafana/`, `prometheus/`, `hardware/`
- `make dev` — mock mode, no cable; `make hw` — real hardware (K-line USB cable on `/dev/ttyUSB0`)
- Frontend aesthetic: dark cinematic, BMW amber instrument-cluster inspired
