# Starlight — Edge-Native Infrastructure

> Machine-readable overview of **Starlight by Mainsail Industries**, distilled from the *Edge-Native Infrastructure* deck. Companion JSON: `starlight-overview.json`.

## TL;DR
**Starlight** is **Edge-Native Infrastructure** — a unified platform to run **virtual machines, containers, and AI workloads** directly at the edge, with security and autonomy embedded into the system itself.

- Tagline: **One platform. Every workload.**
- Built by **Mainsail Industries** (ISV — customers install on their own hardware).
- Three pillars: **Unified · Edge-first · Autonomous.**

## 1. Definition

A unified platform to run virtual machines, containers, and AI workloads directly at the edge — with security and autonomy embedded into the system itself.

| # | Pillar | Claim |
|---|---|---|
| 01 | **Unified** | VMs, containers, AI — one control plane. |
| 02 | **Edge-first** | Operates without central coordination. |
| 03 | **Autonomous** | Security & resilience built-in. |

## 2. Why now — built for scale, not for constraint

Two decades of datacenter infrastructure assumed reliable networks, abundant compute, and dedicated teams to operate complexity at scale. The world has moved to the edge, where those assumptions break down.

| Era | Tag | Wave | Detail | Axis |
|---|---|---|---|---|
| 2000s | Virtualization | Consolidation | Workloads consolidated in centralized environments. Assumed reliable networks and abundant compute. | Datacenter |
| 2010s | Cloud-native | Orchestration | Containers & Kubernetes scaled fleets to thousands of machines — built for constant coordination, not constraint. | Datacenter |
| 2020s | Intelligence | Modern AI | Inference moves close to users and data — where centralized assumptions about network, scale, and trust break down. | Edge |

**Edge reality:** one or two nodes · intermittent networks · constrained compute. The datacenter playbook breaks down.

## 3. Unified by design — one API, every workload

VMs, containers, and AI managed through one operational model. Desktop, CLI, or automation — all pointing at the same control plane.

- **Workloads:** Virtual machines · Containers · AI workloads
- **Interfaces:** Desktop app · CLI · Automation / API

| Shared | Detail |
|---|---|
| Identity | Same auth, same roles, across every workload type. |
| Policy | One enforcement model — VMs, containers, and AI alike. |
| Lifecycle | Deploy, observe, and retire with one set of primitives. |

## 4. VMware take-out — off VMware, on a modern platform

Replace the VMware stack with a platform that runs the same VMs — plus containers and AI — under pricing you can predict and a license you can understand.

| Axis | Today, on VMware | On Starlight |
|---|---|---|
| Pricing | Repriced; double-digit increases common | Predictable, per-node — no surprise uplifts |
| Licensing | Core / socket-pair counting, SKU sprawl | No core or socket-pair counting |
| Renewal | Forced bundles; features you don't use | One SKU. What you run is what you pay for |
| Scope | VMs only — containers & AI elsewhere | VMs, containers, and AI on one platform |

- **Workload compatible.** Existing VMs — Windows and Linux — run on Starlight. Bring images as-is.
- **Feature compatible.** Live migration, HA, snapshots, networking — the feature set teams rely on, natively.
- **Move at your pace.** Run both during transition. Consolidate when you're ready — no forklift required.

## 5. Containers — without Kubernetes complexity

An entirely new orchestration model. Every node is autonomous — it tracks its own resources and shares state peer-to-peer with the cluster. No brittle central control plane.

| Topology | Shape | Behavior |
|---|---|---|
| Kubernetes | Star — every node depends on the control plane | If the control plane is unreachable, the cluster drifts. |
| **Starlight** | **Peer mesh — every node autonomous, state shared by protocol** | Each node runs on its own. The cluster stays consistent. |

- **No control plane to maintain.** No etcd, no scheduler, no operator sprawl. Less to run, less to break.
- **Runs disconnected.** Nodes operate independently when the network drops. State reconverges on its own.
- **Same artifacts.** Existing OCI images run as-is. Helm charts and K8s workloads replatform incrementally.

## 6. AI — batteries included

Models, drivers, protocols, and agent control — shipped as part of the platform. No separate AI stack. No glue work. Deploy inference the same way you deploy any workload.

| Capability | Title | Detail |
|---|---|---|
| Models as containers | Ship AI like you ship apps. | Models are delivered as OCI container images. Same packaging, same lifecycle, same primitives as every other workload — from dev to edge. |
| Drivers included | Ready on first boot. | GPU drivers, accelerator runtimes, and inference toolchains preconfigured and version-matched. No driver hell, no kernel-module roulette. |
| MCP server | Agents speak natively. | A built-in Model Context Protocol server exposes Starlight to AI agents, so tools and models can interact with the platform over a standard interface. |
| Agents control infra | AI operates Starlight. | Use agents to deploy, observe, and manage infrastructure — not just workloads. Control plane is programmable end-to-end. |

**Models are untrusted code. Starlight enforces that.**
- Sandboxed execution with resource limits
- Data paths & egress controlled by policy
- Full observability on every run

## 7. Built for the edge — autonomy, not central control

Each location operates on its own. Workloads keep running during disconnection. Systems synchronize state when connectivity returns.

| Metric | Name | Detail |
|---|---|---|
| **2-node** | High availability | First-class HA without a three-node cluster. Matches edge reality — not datacenter baseline. |
| **0-ops** | Disconnected operation | Nodes function independently when the network drops. No dependency on a central system to keep workloads alive. |
| **1×** | Platform, every scale | Single node to distributed fleet — same operating model. Start small and expand without rework. |

## 8. Security — part of the architecture

Integrated identity, policy enforcement, a hardened OS foundation, and runtime protection for every workload — including AI.

| Layer | Title | Items |
|---|---|---|
| Foundation | Verified & immutable. | Image-based OS, read-only root · Signed builds with full attestation · No runtime drift from deployment · DISA STIG & FIPS 140-3 alignment |
| Runtime | Enforced, not observed. | Process-level visibility & control · Filesystem & network policy · Capability & syscall controls · Identity-driven, real-time |
| Advanced | Ready for what's next. | Confidential computing support · Quantum-resilient cryptography · AI workloads sandboxed by default · Data & egress path controls |

## 9. Adoption — bring your workloads with you

Most teams aren't starting from scratch. Starlight is a new operating model — not a rewrite of the one you already run.

- Existing container images run as-is
- Kubernetes workloads replatform incrementally
- Helm charts adapt without rewriting apps
- CI/CD keeps delivering the same artifacts
- Run both models during transition
- Standardize when you're ready

**Positioning.** Starlight is built by Mainsail Industries for organizations operating where infrastructure must function with limited resources, unreliable networks, and no room for failure.

## 10. Glossary

- **MCP** — Model Context Protocol. Interface that lets AI agents drive Starlight directly.
- **OCI** — Open Container Initiative. Container image standard.
- **STIG** — Security Technical Implementation Guide. DoD security configuration standard.
- **FIPS 140-3** — U.S. federal cryptographic module standard.
- **Two-node HA** — High availability with only two nodes; first-class target for edge sites.

---

*Source: Starlight — Edge-Native Infrastructure deck. Mainsail Industries · mainsailindustries.com*
