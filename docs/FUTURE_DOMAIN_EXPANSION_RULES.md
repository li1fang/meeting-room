# Future Domain Expansion Rules

Status: Draft

## Purpose

This document defines how future non-NC domains should enter `meeting-room` without recreating AGI-Nutshell-style drift.

The repository remains NC-first.
NP, PS, and TS are reserved expansion paths, not active schema lines in this round.

## Canonical placement

All future domains must use the same canonical root tree:

- `schemas/<domain>/`
- `samples/<topic>/`
- `tck/suites/<domain>/`
- `docs/`
- `common/registry/`

No mirrored `domains/**` tree is allowed.

## Minimum landing requirements

A future non-NC domain is not considered landed unless all of the following exist:

- one domain intro or boundary document
- one real schema
- one minimal sample
- one minimal TCK suite
- one registry entry
- matching updates in `README.md`, `docs/SCHEMA.md`, and `docs/ROADMAP_STATUS.md`

No fake placeholder schemas should be committed just to reserve names.
No fake registry entries should be committed before the first real schema exists.

## Domain introduction rule

Before the first schema for a new domain lands, the repository must carry a short boundary document that answers:

- what the domain owns
- what it does not own
- how it relates to NC baseline lines
- what remains explicitly out of scope for its first landing

## Registry expectations

When a new domain lands its first topic:

- add the topic to `genesis.contracts.yaml`
- add the topic to `common/registry/topics.yaml`
- add one sample directory under `samples/`
- add one TCK suite under `tck/suites/<domain>/`

The registry must only describe real topics that exist in the repository.

## Repository identity rule

`meeting-room` stays NC-first even after future domains arrive.
That means:

- NC baseline docs remain first-class entry points
- new domains do not redefine NC terms retroactively
- cross-domain additions must preserve existing NC formal lines

## Reserved path today

Current reserved domains are:

- `np`
- `ps`
- `ts`

In this round they remain reserved only.
No schemas are added for them yet.
