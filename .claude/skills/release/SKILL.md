---
name: rust-release
description: Prepare a crate release in this workspace
---
1. Ask which crate(s) and the new version.
2. Bump version in Cargo.toml and all intra-workspace dependents.
3. Move CHANGELOG `## [unreleased]` items into a dated version section. Use a PLAIN tag link, not a compare link. Do NOT add version constraints to unpublished crates.
4. Verify LICENSE files and Cargo.toml metadata (description, repository, categories, keywords).
5. Run: cargo build --workspace && cargo clippy --workspace --all-features -- -D warnings && cargo fmt --check && just docs
6. Show a proposed commit message. Do NOT commit or switch branches without approval.
