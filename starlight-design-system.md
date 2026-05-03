# Starlight Design System — Brand Guide

> Machine-readable brand & design guide for **Starlight by Mainsail Industries**.
> Companion JSON: `starlight-design-system.json`.
> All binary assets (logos, star glyph, boot splash, 57 icon SVGs) live at **https://github.com/Mainsail-Industries/mainsail-assets** — filenames in §7 and §8 are relative to the repo root. Raw URLs use `https://raw.githubusercontent.com/Mainsail-Industries/mainsail-assets/main/<filename>`.

## 1. Brand

| Field | Value |
|---|---|
| Company | Mainsail Industries (ISV — we produce software, not a cloud) |
| Product | Starlight — software for running VMs, containers, and AI on your own infrastructure |
| Tagline | Run VMs, containers, and AI on one platform. |
| Voice | Clear, experienced, and insider. |
| Person | 2nd person for product. 1st-person-plural for marketing. Never "I". |
| Casing | Sentence case everywhere. Exceptions: proper product names, code/ENV vars. |
| Emoji | Never in product UI or marketing. Changelog only, sparingly. |
| Unicode | `→` leads-to · `·` separator · `—` aside. Never `-->` or `...`. |

**Banned words:** unlock, empower, supercharge, revolutionize, blazing fast, next-gen, journey.
**Preferred verbs:** ship, run, deploy, scale, boot, route.

**Off-brand (do not ship):** "🚀 Unlock next-gen compute!" · "Your AI journey starts here." · "One bill for all your compute." · "Sign up and boot a GPU in 40 seconds." · "The cloud, reimagined."

**Positioning guardrails.** Starlight is **software the customer installs and runs**, not a hosted service. Never imply Mainsail provides the infrastructure, billing, capacity, or uptime — the customer brings the hardware (bare metal, edge, air-gapped, or a cloud account they own) and Starlight is what runs on it. Avoid: "sign up", "on demand", per-second pricing, "one bill", SLA language, "the cloud", "hosted".

## 2. Color

### Brand core (canonical, from Mainsail spec)
| Name | Hex | Use |
|---|---|---|
| Starlight Blue | `#0047BB` | Primary accent. CTAs, links, focus, active. |
| Starlight Black | `#212020` | Product background base. Warm; never pure `#000`. |
| Starlight Grey | `#BFBFBF` | Silver from wordmark. Secondary text, dividers, disabled. |
| White | `#FFFFFF` | Primary text on dark, primary bg on light. |

### Blue scale
`50 #EAF0FC · 100 #C7D6F5 · 200 #8FACEB · 300 #5782E0 · 400 #2862D3 · 500 #0047BB ★ · 600 #003A99 · 700 #002D77 · 800 #001F55 · 900 #00112E`

### Neutral scale (cool-tinted)
`0 #FFFFFF · 50 #F5F6F8 · 100 #E7E9ED · 200 #C9CCD3 · 300 #9DA1AB · 400 #6B6F79 · 500 #4A4D55 · 600 #2F3238 · 700 #1E2025 · 800 #15171B · 900 #0B0D12 · 950 #06080B`

### Semantic — dark (default)
| Token | Value | Role |
|---|---|---|
| `bg-0` | `#0B0D12` | page / deepest |
| `bg-1` | `#15171B` | product surface |
| `bg-2` | `#1E2025` | raised cards |
| `bg-3` | `#2F3238` | popover, hovered row |
| `fg-1` | `#FFFFFF` | primary text |
| `fg-2` | `hsla(220 10% 98% / 0.78)` | secondary text |
| `fg-3` | `#BFBFBF` | tertiary, meta, labels |
| `fg-4` | `hsla(220 10% 80% / 0.42)` | muted, disabled |
| `border-1` | `hsla(0 0% 100% / 0.08)` | hairline |
| `border-2` | `hsla(0 0% 100% / 0.14)` | hover |
| `border-accent` | `hsla(218 100% 37% / 0.60)` | focus / active |
| `accent` / `accent-hover` / `accent-press` | `#0047BB` / `#1459D2` / `#002D77` | |

### Status
`success #2BD4A1 · warning #F5B544 · danger #FF5A5F · info #2862D3`
Tuned for dark surfaces — re-check contrast on white.

## 3. Typography

| Family | Use | Weights | Stack |
|---|---|---|---|
| **Manrope** | Display: H1–H3, eyebrows, stat numbers | 200–800 | `Manrope, ui-sans-serif, system-ui, …` |
| **Poppins** | Body: paragraphs, UI text, labels | 300–700 | `Poppins, ui-sans-serif, system-ui, …` |
| **JetBrains Mono ★** | Code, tabular | 400–600 | `'JetBrains Mono', ui-monospace, …` |

★ Mono is a substitution — brand spec did not name one. Confirm or swap.

### Scale (px)
`12 · 13 · 14 · 16 · 18 · 20 · 24 · 32 · 40 · 56 · 72 · 88`

### Headings
| Tag | px | Tracking | LH | Weight |
|---|---|---|---|---|
| h1 | 72 | -0.035em | 1.1 | 700 |
| h2 | 56 | -0.030em | 1.1 | 700 |
| h3 | 40 | -0.025em | 1.1 | 700 |
| h4 | 32 | -0.020em | 1.1 | 700 |
| h5 | 24 | -0.015em | 1.1 | 700 |
| h6 | 20 | -0.010em | 1.1 | 700 |

Body 16/1.5 weight 400. Eyebrow: Manrope 600 / 12px / 0.14em / UPPERCASE.

## 4. Spacing, radius, shadow

- **Spacing scale (px):** `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`
- **Section vertical:** desktop 96 · tablet 64 · mobile 48 · card padding 24
- **Radius:** `sm 6` (chips) · `md 10` (buttons, inputs) · `lg 16` (cards) · `xl 24` (hero panels) · `full 999` (pills, avatars). **Never mix radii on nested elements.**
- **Borders:** 1px hairline at `hsla(0 0% 100% / 0.08)` on dark. Focus → `border-accent`.
- **Shadows** (dark UI prefers borders + lightness over drop shadows):
  - `raised`: `0 1px 0 hsla(0 0% 100% / .06) inset, 0 1px 2px hsla(0 0% 0% / .4)`
  - `pop`: `0 20px 60px -20px hsla(220 50% 4% / .9), 0 1px 0 hsla(0 0% 100% / .06) inset`
  - `glow`: `0 0 0 1px hsla(218 100% 37% / .6), 0 0 40px -4px hsla(218 100% 37% / .4)`

## 5. Motion ("Miro-inspired")

- **Easing.** out `cubic-bezier(0.22, 1, 0.36, 1)` · inout `cubic-bezier(0.65, 0, 0.35, 1)`. No default linear.
- **Durations.** micro 120ms · sm 220ms · md 420ms · lg 700ms.
- **Cursor parallax (hero):** star drifts 1x · aurora 0.4x · secondary type 0.15x. Damped spring, not 1:1.
- **Buttons.** Hover translateY(-1px) + brightness +6%. Press translateY(0) scale(0.99) for 80ms.
- **Cards.** Border white/6% → white/14% on hover. No scale.
- **Loading.** Lens-flare loader: bokeh ghost stars + anamorphic streak around focal star glyph.
- **Skeleton.** 1px shimmer, 1.6s ease-in-out, left → right.

## 6. Background system

One base + one accent glow + one texture.

1. Solid `bg-0` base.
2. Soft blue radial aurora at ~55% opacity, blurred 40–120px, off-center. Cursor-reactive on hero.
3. 24–28px dot grid at 5% white. Product surfaces only.
4. Optional full-bleed star glyph at 4–8% opacity.

**Do not.** No 5-color gradient meshes. No diagonal stripes. No noise/grain.

## 7. Logos

> Hosted at **github.com/Mainsail-Industries/mainsail-assets** (repo root). Construct raw URLs as `https://raw.githubusercontent.com/Mainsail-Industries/mainsail-assets/main/<filename>`.

### Starlight (product)
| Asset | Filename in repo |
|---|---|
| Wordmark white | `starlight-logo-white.png` |
| Wordmark black | `starlight-logo-black.png` |
| Wordmark silver | `starlight-logo-silver.png` |
| Star glyph white | `starlight-star-b-white.png` |
| Star glyph black | `starlight-star-b.png` |
| Star symbol silver | `starlight-symbol-silver.png` |

Star glyph = eight-pointed M-star. Use for app icon, loader, auth, 404, empty global state. **Never inline with body copy.**

### Mainsail (parent company)
| Asset | Filename in repo |
|---|---|
| Wordmark blue | `mainsail-logo-blue.png` |
| Wordmark black | `mainsail-black-sm.png` |
| Wordmark white | `mainsail-white.png` |

Use for corporate endorsement only — About page, legal footer, investor materials. **Never co-lock with the Starlight wordmark on product surfaces.**

### Boot splash / hero
| Asset | Filename in repo |
|---|---|
| 1920×1080 | `starlight-grub-1920x1080.png` |
| 2560×1440 | `starlight-grub-2560x1440.png` |

GRUB / OS boot splash. Reusable for full-bleed marketing hero, loading screens, auth backgrounds.

## 8. Iconography

Official Starlight icon set — **57 SVGs**, 72×72 viewBox, **1.65px stroke**, `stroke-miterlimit: 10`. Recolor by rewriting strokes/fills to `currentColor` and setting `color` on the parent.

**Path template (in repo):** `starlight-icons-black-svg/<category folder>/<slug>.svg`

Category folder names contain spaces, ampersands, and one colon — **URL-encode** when building raw URLs (e.g. `edge%20%26%20connectivity`, `platform%3AOS`).

| Category | Folder name in repo | Slugs (each prefixed `icon-`) |
|---|---|---|
| Compute | `compute` | virtual-machine, container-pod, cpu-vcpu, inference-engine, live-migration, confidential-compute-enclave, workload-process |
| Networking | `networking` | network-tunnel, overlay-network, p2p-mesh, dns-discovery, firewall-access-policy, gatway-ingress, node-peer |
| Storage | `storage` | block-storage-volume, distributed-ojectstore, immutable-backup, replicated-data, s3-compatible-bucket |
| Security | `security` | attestation-verified-boot, certificate-identity, hardware-entropy-source, post-quantum-key, quantum-safe-tunnel, signing-sbom, zero-trust-policy |
| Orchestration & state | `orchestration & state` | cluster, scheduler, health-check, event-log-stream, gossip-state-propagation, node-authoritative |
| Edge & connectivity | `edge & connectivity` | edge-node, air-gapped-node, ddil-environment, satellite-link, reconnect-sync-recovery, disconnected-operation-mode |
| Infra topology | `infrastructure topology` | cloud-anchor, hub-and-spoke, full-mesh, multi-node-cluster, on-premise-rack, single-node, wan-link |
| Management & interfaces | `management & interfaces` | cli-terminal, api-endpoint, dashboard-desktop, ansible-playbook, terraform-block, operator-role |
| Platform / OS | `platform:OS` | ami-disk-image, container-image-registry, immutable-os-bootc, sbom, signed-artifact, software-update-ota |

Filename example: `starlight-icons-black-svg/compute/icon-virtual-machine.svg`.

**Recommended sizes (px):** 20, 24, 32, 48, 64. Below 20 the 1.65 stroke gets noisy.

**Rules.** Never restroke. Never combine with another icon library on the same surface. Default `#fff` on dark / `#212020` on light. Hover `#5782E0`. Active `#0047BB`.

## 9. Quick consumption notes (for LLMs / API)

- The JSON sibling (`starlight-design-system.json`) is the authoritative machine-readable form. Both files are stand-alone — no other files needed.
- Binary assets are fetched on demand from the GitHub repo. The two design-system files contain only the manifest.
- Icons are SVG — recolor by setting `color` on the parent and rewriting strokes/fills to `currentColor`.
- When generating new UI, default to dark palette + Manrope display + Poppins body + 1.5 leading + 96px sections + 16px card radius + hairline borders + bokeh/lens-flare loaders.
